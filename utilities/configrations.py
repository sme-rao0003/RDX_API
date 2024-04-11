
import configparser

def getConfigration():
    config = configparser.ConfigParser()
    config.read(r'C:\Users\RAO0003\Documents\RDX_API_AUTOMATION\RDX_API_Automation\utilities\properties.ini')
    return config

