from config import *

from screens.SecondaryScreen import SecondaryScreen

class PhotoScreen(SecondaryScreen):
    def __init__(self):
        LOG.info("instantiating PhotoScreen")
        super().__init__()
