import json


class InstallProjects(object):

    def __init__(self, path, project=None):
        self.path = path
        if project is None:
            self.project = []
        else:
            self.project = [project]

    def factory_settings(self):
        if len(self.project) == 0:
            f = open(self.path, 'w')
            json.dump(self.project, f)
            f.close()
        else:
            f = open(self.path, 'r')
            tmp = json.load(f)
            if self.project[0] not in tmp:
                tmp.append(*self.project)
            f.close()
            f = open(self.path, 'w')
            json.dump(tmp, f)
            f.close()
