import unittest
from main import create_folder, check_folder, failure_function


class TestYandexApi(unittest.TestCase):
    def test_create_folder(self):
        resp_code = 201
        res = create_folder()
        self.assertEqual(res, resp_code)

    def test_check_folder(self):
        resp_code = 200
        res = check_folder()
        self.assertEqual(res, resp_code)

    @unittest.expectedFailure
    def test_is_folder_exist(self):
        resp_code = 201
        res = create_folder()
        self.assertEqual(res, resp_code, 'Такая папка уже существует. status code 409')

    @unittest.expectedFailure
    def test_invalid_data(self):
        resp_code = 201
        res = failure_function()
        self.assertEqual(res, resp_code, 'Некорректные данные. status code 400')