from config import *

from screens.SecondaryScreen import SecondaryScreen

class EchoBoxScreen(SecondaryScreen):
    def __init__(self):
        LOG.info("instantiating EchoBoxScreen")
        super().__init__()
