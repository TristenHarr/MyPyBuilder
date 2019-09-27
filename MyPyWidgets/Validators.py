import os


class Validator(object):

    @staticmethod
    def file_namify(data):
        removal = [' ', ',', '"', "'", '\\', '/', '-', '.', '[', ']', '(', ')']
        if data[0].isalpha():
            for item in removal:
                data = data.replace(item, '')
            return data.lower().capitalize()
        else:
            return False

    @staticmethod
    def is_int(data, default=0):
        if data.lstrip('-').isdigit():
            if int(data) >= default:
                return int(data)
            else:
                return False
        else:
            return False

    @staticmethod
    def is_alpha(data, index=0):
        if data[index].isalpha():
            return data.strip()
        else:
            return False

    @staticmethod
    def not_empty(data):
        if data is not '':
            return data
        else:
            return False

    @staticmethod
    def field_retrieve(form, fields, validators, validator_args):
        form_data = {'_valid': True}
        for i, validator in enumerate(validators):
            if validator is None:
                form_data[fields[i]] = form[fields[i]].get()
            else:
                form_data[fields[i]] = validator(form[fields[i]].get(), *validator_args[i])
                if form_data[fields[i]] is False:
                    form_data['_valid'] = False
        return form_data

    @staticmethod
    def is_path(data):
        if os.path.exists(data):
            return data
        else:
            return False
