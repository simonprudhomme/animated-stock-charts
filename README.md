# Stock Market Visualization

## Overview
This project provides animated charts of stocks value over time. 
By generating an animated charts, users can observe the growth and trend of selected stocks, allowing for easy comparison between different companies.

## Features
- Create a line chart visualization comparing two stocks or more.
- Animate the line chart to show progression over time.
- Save the animation as a GIF for easy sharing and presentation.

## Prerequisites
1. Python 3.11, which can be installed using Homebrew:
   ```bash
    brew install python@3.11
    ```
2. ffmpeg (for saving the animation as a GIF or Video), which can be installed using Homebrew:
   ```bash
    brew install ffmpeg
    ```

## Installation

Clone the repository and install the required packages using the following commands:
```bash
git clone https://github.com/simonprudhomme/animated-stock-charts
cd animated-stock-charts
```

Create a virtual environment and install the required packages:
```bash
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Usage
Run the CLI 
```bash
python stock_animation_cli.py --tickers GOOGL MSFT NVDA --period 6mo
```
The generated animation will be saved in the `output` directory.

## Roadmap
- Improve the CLI to reflect the notebook and with option, logs and error handling
- add key event from SerpAPI for each stock
- Improve the visualization by adding more features and options.
