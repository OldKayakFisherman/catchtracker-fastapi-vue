from dotenv import load_dotenv
from collections import namedtuple
import os
import sys


class SettingsResult:

    def __init__(self) -> None:
        
        load_dotenv()
        self.__sqlite_connection = f"sqlite:///{sys.path[0]}{os.sep}catchtracker.sqlite"     
        
    
    @property
    def sqlite_connection(self):
        return self.__sqlite_connection
    
    @property
    def project_name(self):
        return "Catch Tracker"

def get_settings():
    return SettingsResult()
