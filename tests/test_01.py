import sys
import unittest
import pandas as pd
import os

sys.path.append('src')
from csv_to_xlsx import convert_csv_to_xlsx

class TestConvertCsvToXlsx(unittest.TestCase):
    def setUp(self):
        self.csv_file_path = 'test_data/test_stock_data.csv'
        self.xlsx_file_path = 'test_data/test_stock_data.xlsx'
        self.exchange_rate = 0.9

    def test_csv_to_xlsx_conversion(self):
        convert_csv_to_xlsx(self.csv_file_path, self.xlsx_file_path, self.exchange_rate)
        self.assertTrue(os.path.exists(self.xlsx_file_path))

        df = pd.read_excel(self.xlsx_file_path)
        expected_columns = ['Stock Name', 'Price', 'Market', 'Date']
        self.assertListEqual(list(df.columns), expected_columns)

if __name__ == '__main__':
    unittest.main()
