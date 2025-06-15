import yaml
from .Singleton import Singleton
from .Logger import Logger as LOG

class Settings(metaclass=Singleton):
    configs = {}
    def __call__(self):
        if (self.configs == {}):
            with open('resources/config.yml', 'r') as file:
                self.configs = yaml.safe_load(file)
        return self.configs        
