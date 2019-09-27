import json


class DeleteProject(object):

    def __init__(self, path, project=None):
        self.path = path
        if project is None:
            self.project = None
        else:
            self.project = project

    def factory_settings(self):
        if self.project is not None:
            f = open(self.path, 'r')
            tmp = json.load(f)
            f.close()
            tmp_list = []
            for item in tmp:
                if item != self.project:
                    tmp_list.append(item)
            f = open(self.path, 'w')
            json.dump(tmp_list, f)
            f.close()
