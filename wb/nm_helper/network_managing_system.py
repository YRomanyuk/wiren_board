class ParseError(Exception):
    pass

class NetworkManagingSystem(object):
    """
    The base interface provides functions to read or create interfaces for specific network manager system.
    """
    @staticmethod
    def probe():
        pass

    def apply(self, interfaces):
        pass

    def read(self):
        pass

    def get_wifi_ssids(self):
        return []
    
    def add_devices(self, devices):
        return []
