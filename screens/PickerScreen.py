from config import *

from screens.SecondaryScreen import SecondaryScreen

class PickerScreen(SecondaryScreen):
    def __init__(self):
        LOG.info("instantiating PickerScreen")
        super().__init__()
