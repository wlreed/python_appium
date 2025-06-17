from config import *

from screens.SecondaryScreen import SecondaryScreen

class GeolocationScreen(SecondaryScreen):
    def __init__(self):
        LOG.info("instantiating GeolocationScreen")
        super().__init__()
