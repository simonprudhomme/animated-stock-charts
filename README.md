# Stock Market Capitalization Visualization

## Overview
This project provides a visual representation of the market capitalization of stocks over time. By generating an animated line chart, users can observe the growth and trends in market capitalization of selected stocks, allowing for easy comparison between different companies.

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
git clone <repo>
cd <repo>
```

Create a virtual environment and install the required packages:
```bash
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Usage
Run the notebook under `notebooks/app.ipynb`.
The generated GIF will be saved in the `output` directory.

## Roadmap
- Add support to load data from sources.
- Improve the visualization by adding more features and options.
- Create a CLI to genereate the visualization from a command line.