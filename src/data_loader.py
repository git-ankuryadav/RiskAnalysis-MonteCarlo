import yfinance as yf
import numpy as np

def download_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    return data

if __name__ == "__main__":
    df = download_stock_data("COALINDIA.NS", "2020-01-01", "2023-12-30")
    df_cleaned = df[df['Open'].notnull()]
    df_cleaned.rename(columns={'Close': 'Closing_Price'}, inplace=True)
    df_cleaned = df_cleaned[['Closing_Price']].reset_index()
    df_cleaned['Log_Return'] = np.log(df_cleaned['Closing_Price'] / df_cleaned['Closing_Price'].shift(1))
    df_cleaned = df_cleaned.dropna().reset_index(drop=True)
    df_cleaned.to_csv("../data/historicalData.csv")
