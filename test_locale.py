import json
import unittest
from convert_locale_json import ConvertLocale


class TestLocale(unittest.TestCase):
    def test_validate_file_path(self):
        file_path = 'invalid_path.json'
        obj = ConvertLocale(file_path)
        status, message = obj.validate_file_path()
        self.assertEqual(status, False)

    def test_all_ok(self):
        file_path = 'sample_file.json'
        sample_dict = {'msiPropertyName1': {'it_IT': 'value1', 'en_US': 'value2'},
                       'msiPropertyName2': {'it_IT': 'value3', 'en_US': 'value4'}}
        expected_result = {'it_IT': {'msiPropertyName1': 'value1', 'msiPropertyName2': 'value3'},
                           'en_US': {'msiPropertyName1': 'value2', 'msiPropertyName2': 'value4'}}

        with open(file_path, 'w') as fw:
            json.dump(sample_dict, fw)

        obj = ConvertLocale(file_path)
        obj.initialise_data()
        result = obj.get_result()
        self.assertEqual(result, json.dumps(expected_result))
