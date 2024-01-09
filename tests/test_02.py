import sys
import unittest

sys.path.append('src')
from plot_data import read_data, visualize_data

class TestVisualizeData(unittest.TestCase):
    def test_visualize_data(self):
        xlsx_file_path = 'test_data/test_stock_data.xlsx'
        df = read_data(xlsx_file_path)
        try:
            visualize_data(df)
            test_passed = True
        except Exception as e:
            test_passed = False
        self.assertTrue(test_passed)

if __name__ == '__main__':
    unittest.main()
