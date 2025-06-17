from config import *

from screens.SecondaryScreen import SecondaryScreen

class WebviewScreen(SecondaryScreen):
    def __init__(self):
        LOG.info("instantiating WebviewScreen")
        super().__init__()
