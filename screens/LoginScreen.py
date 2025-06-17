from config import *

from screens.SecondaryScreen import SecondaryScreen

class LoginScreen(SecondaryScreen):
    def __init__(self):
        LOG.info("instantiating LoginScreen")
        super().__init__()
