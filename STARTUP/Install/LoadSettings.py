import json


class SettingsLoader(object):

    def __init__(self, path):
        self.path = path

    def fetch_settings(self):
        f = open(self.path, 'r')
        settings = json.load(f)
        f.close()
        return settings
