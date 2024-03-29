import argparse
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
import yfinance as yf
import loguru

# Set up logging
loguru.logger.add('stock_animation.log')

def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate stock progression animation for specified tickers.')
    parser.add_argument('--tickers', nargs='+', help='Ticker symbols for the stocks', required=True)
    parser.add_argument('--period', type=str, default='12mo', help='Period over which to fetch the data (e.g., 1mo, 3mo, 6mo, 12mo, ytd)')
    args = parser.parse_args()
    if len(args.tickers) < 2:
        parser.error("At least two tickers are required")
    return args

def download_stock_data(tickers, period):
    try:
        data = yf.download(tickers, period=period)
        if 'Adj Close' not in data:
            raise ValueError("Data does not contain 'Adj Close' prices")
        if data['Adj Close'].isnull().values.any():
            loguru.logger.warning("Data contains missing values")
        return data['Adj Close'].reset_index()
    except Exception as e:
        print(f"Failed to download data: {e}")
        exit(1)

def prepare_animation(data, tickers):
    fig, ax = plt.subplots(figsize=(16, 10))
    
    def update(frame):
        loguru.logger.debug(f'Frame: {frame} / {len(data["Date"])}')
        ax.clear()
        for ticker in tickers:
            ax.plot(data['Date'][:frame], data[ticker][:frame], label=ticker)
            ax.text(data['Date'][frame], data[ticker][frame], f'${data[ticker][frame]:.2f}', ha='left', va='center', bbox=dict(facecolor='white', alpha=1, edgecolor='none', boxstyle='round,pad=0.2'))
        ax.set_title(f'{" Vs ".join(tickers)},\n $USD per share')
        ax.set_ylabel('$USD per share')
        ax.legend(loc='upper left')

    ani = FuncAnimation(fig, update, frames=len(data['Date']), repeat=False)
    return ani

def main():
    args = parse_arguments()
    data = download_stock_data(args.tickers, args.period)
    ani = prepare_animation(data, args.tickers)
    
    # Determine file name based on input parameters
    min_date, max_date = data['Date'].min().strftime('%Y-%m-%d'), data['Date'].max().strftime('%Y-%m-%d')
    filename = f'stock_progression_{"_vs_".join(args.tickers)}_{min_date}_to_{max_date}.mp4'
    
    # Save the animation
    writer = FFMpegWriter(fps=30)
    file_output = f'./output/{filename}'
    os.makedirs(os.path.dirname(file_output), exist_ok=True)
    ani.save(file_output, writer=writer)
    plt.close()
    loguru.logger.info(f'Animation saved to {file_output}')

if __name__ == '__main__':
    main()
