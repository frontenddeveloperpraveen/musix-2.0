'''
'''

from . import constants

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

def browse_hotlist(self: object) -> dict:
    '''
    '''

    return self.browse \
    (
        browse_id = constants.BROWSE_ID_HOTLIST,
    )
