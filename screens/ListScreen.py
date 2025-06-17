from config import *

from screens.SecondaryScreen import SecondaryScreen

class ListScreen(SecondaryScreen):
    def __init__(self):
        LOG.info("instantiating ListScreen")
        super().__init__()
