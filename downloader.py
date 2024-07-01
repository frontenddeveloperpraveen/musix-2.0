import telebot
from pytube import YouTube
import ytm
import subprocess
import os
bot = telebot.TeleBot('6348897063:AAExtb7SP-9mYr9xO1IEfN2vACFdknppeec')
api = ytm.YouTubeMusic()

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, f'''Hi {message.from_user.first_name} 👋
Welcome to the Musix Bot Updated Version 2.5.2
Send a Song name with the /song command to download and listen.
Eg:
/song snowman 
/song Chinna chinna kangal
/song Lungi Dance
Made with ❤️ - Praveen                     
''')

@bot.message_handler(commands=['song'])
def handle_song(message):
    if message.text.startswith('/song'):
        try:
            prompt = message.text.split(' ', 1)[1]
        except IndexError:
            bot.send_message(message.chat.id, "Please provide a valid song name.")
            return
        
        songs = api.search_songs(prompt)['items'][0]
        
        description = f'''Song : {songs['name']}
Singer : {songs['artists'][0]['name']}
Album : {songs['album']['name']}
        '''
        bot.send_message(message.chat.id, description)
        
        url = 'https://music.youtube.com/watch?v=' + str(songs['id'])
        
        try:
            yt = YouTube(url=url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            filename = songs['name'] 
            mp3_name = filename  + '.mp3' 
            audio_stream.download(output_path='downloads', filename=mp3_name)
            audio_file_path = os.path.join('downloads', mp3_name)
            print(audio_file_path)
            try:
                print('ok')
                with open(audio_file_path, 'rb') as audio_file:
                    bot.send_audio(message.chat.id, audio_file)
                os.remove(audio_file_path)
            except Exception as e:
                pass

            print("done")
                # elif message.text == 'Lossless FLAC - High Quality':
                #     lossLess_name = filename + ".flac"
                #     command = f'ffmpeg -i {mp3_name} -vcodec copy {lossLess_name}'
                #     subprocess.run(command)
                #     input()
                    
                # else:
                #     bot.send_message(message.chat.id, "Please choose a valid option.")
                #     return
                
                # filename = f"{songs['name']} - {songs['artists'][0]['name']}.mp3"
                # audio_stream.download(output_path='downloads', filename=filename)
                # audio_file_path = os.path.join('downloads', filename)
                
                # with open(audio_file_path, 'rb') as audio_file:
                #     bot.send_audio(message.chat.id, audio_file)
                
                # os.remove(audio_file_path)
                
                # # Remove the temporary handler to avoid multiple callbacks
                # bot.remove_message_handler(handle_audio_choice)
        
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")

# @bot.message_handler(commands=['flac'])
# def handle_song(message):
#     if message.text.startswith('/flac'):
#         try:
#             prompt = message.text.split(' ', 1)[1]
#         except IndexError:
#             bot.send_message(message.chat.id, "Please provide a valid song name.")
#             return
        
#         songs = api.search_songs(prompt)['items'][0]
        
#         description = f'''
#         Song : {songs['name']}
#         Singer : {songs['artists'][0]['name']}
#         Album : {songs['album']['name']}
#         '''
#         bot.send_message(message.chat.id, description)
        
#         url = 'https://music.youtube.com/watch?v=' + str(songs['id'])
        
#         try:
#             yt = YouTube(url=url)
#             audio_stream = yt.streams.filter(only_audio=True).first()
#             filename = str(message.text.replace("/song",'').replace('/','',11).replace("\\",'',11)).title() + ' - '+ str("Praveen".replace('/','',11).replace("\\",'',11)).title() 
#             mp3_name = filename  + '.mp3' 
#             audio_stream.download(output_path='downloads', filename=mp3_name)
#             audio_file_path = os.path.join('downloads', mp3_name)
#             print("done")
#             lossless_name = os.path.join('downloads', f"{songs['name']} - {songs['artists'][0]['name']}.flac")
#             command = f'.\\ffmpeg -i "{audio_file_path}" -vn -acodec flac -y "{lossless_name}"'
#             result = subprocess.run(command, shell=True, capture_output=True, text=True)
#             if result.returncode != 0:
#                 raise Exception(f'FFmpeg error: {result.stderr}')
#             print("process over")
#             print("<Loc> : ",lossless_name)
#             with open(lossless_name, 'rb') as f:
#                 print('Sending audio file...')
#                 bot.send_audio(message.chat.id, f,timeout=10000)
#                     # os.remove(audio_file_path)
#             # os.remove(lossless_name)
#         # Remove the temporary handler to avoid multiple callbacks


#         except Exception as e:
#             bot.send_message(message.chat.id, f"Error: {e}")





@bot.message_handler(func=lambda message: True)
def handle_invalid(message):
    bot.send_message(message.chat.id, "Invalid Command. Please use /start to know about the bot or /song download song.")

if __name__ == "__main__":
    print("[BOT] : Running")
    bot.polling(none_stop=True)
