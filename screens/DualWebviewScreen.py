from config import *

from screens.SecondaryScreen import SecondaryScreen

class DualWebviewScreen(SecondaryScreen):
    def __init__(self):
        LOG.info("instantiating DualWebviewScreen")
        super().__init__()
