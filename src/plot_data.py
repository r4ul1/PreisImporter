import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def read_data(xlsx_file_path):
    return pd.read_excel(xlsx_file_path)

def visualize_data(df):
    plt.figure(figsize=(12, 8))
    for stock in df['Stock Name'].unique():
        stock_data = df[df['Stock Name'] == stock]
        plt.plot(stock_data['Date'], stock_data['Price'], label=stock, marker='o')

    plt.xlabel('Date')
    plt.ylabel('Price in EUR')
    plt.title('Stock Price Over Time')
    plt.legend()
    plt.grid(True)
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()

    plt.show()

if __name__ == "__main__":
    df = read_data('src/stock_data.xlsx')
    visualize_data(df)
