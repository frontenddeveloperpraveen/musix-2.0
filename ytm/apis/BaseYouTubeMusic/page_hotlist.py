'''
'''

from . import constants

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

def page_hotlist(self: object) -> dict:
    '''
    '''

    return self._get_page \
    (
        endpoint = constants.ENDPOINT_YTM_HOTLIST,
    )
