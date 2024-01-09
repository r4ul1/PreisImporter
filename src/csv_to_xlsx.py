import pandas as pd

def convert_csv_to_xlsx(csv_file_path, xlsx_file_path, exchange_rate):
    df = pd.read_csv(csv_file_path, sep=',', names=['Stock Name', 'Epoch Time', 'Price', 'Currency', 'Market'])
    df['Market'] = df['Market'].str.replace(';', '').str.strip()
    df['Currency'] = df['Currency'].str.strip()

    df['Price'] = df.apply(lambda row: row['Price'] if row['Currency'] == 'EUR' else row['Price'] * exchange_rate, axis=1)

    df['Date'] = pd.to_datetime(df['Epoch Time'], unit='s')
    df.drop(columns=['Epoch Time', 'Currency'], inplace=True)

    df.to_excel(xlsx_file_path, index=False)

if __name__ == "__main__":
    convert_csv_to_xlsx('src/stock_data.csv', 'src/stock_data.xlsx', exchange_rate=0.9)
