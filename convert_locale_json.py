import json
import os
from convert_locale_exceptions import CustomFileError, CustomJsonError


class ConvertLocale:
    def __init__(self, path: str):
        self.path = path
        self.data = {}
        self.result = {}

    def validate_file_path(self):
        """ Check if file path is valid """
        if not os.path.exists(self.path):
            return False, f'Path does not exist: {self.path}'
        if not os.path.isfile(self.path):
            return False, f'Given path is not a file: {self.path}'
        return True, ''

    def initialise_data(self):
        """ Load json from file and set in self.data """
        f_status, message = self.validate_file_path()
        if f_status:
            try:
                with open(self.path, 'r') as fr:
                    self.data = json.load(fr)
            except ValueError:
                raise CustomJsonError(f'Error in JSON decoding')
        else:
            raise CustomFileError(message)

    def set_result(self):
        """ Convert the locale json into proper format and set result in self.result """
        for prop_name, prop_dict in self.data.items():
            for prop_k, prop_v in prop_dict.items():
                temp_dict = self.result.get(prop_k, {})
                temp_dict[prop_name] = prop_v
                self.result[prop_k] = temp_dict

    def get_result(self) -> str:
        """ return self.result """
        if not bool(self.result):
            self.set_result()
        return json.dumps(self.result)


if __name__ == '__main__':
    file_path = 'properties.json'
    conv = ConvertLocale(file_path)
    conv.initialise_data()
    print(conv.get_result())
