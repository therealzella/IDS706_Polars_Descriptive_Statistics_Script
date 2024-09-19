# IDS706_Polars_Descriptive_Statistics_Script

This is a repository for the IDS706 course's Polars Descriptive Statistics Script assignment. The file `camera_dataset.csv` is used for descriptive statistics python script.

![CI](https://github.com/therealzella/IDS706-python-github-template/actions/workflows/ci.yml/badge.svg)

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Makefile Commands](#makefile-commands)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This repository is a Python project template designed for the IDS706 course. It includes:
- A `main.py` file with the core functionality.
- A `main_test.py` file with unit tests for the project.
- A `Makefile` for automating common tasks like formatting, linting, and testing.
- A `.gitignore` file to keep unnecessary files out of your repository.
- A `requirements.txt` file to manage dependencies.
- A `stats_script.py` file for the homework requirement.
- A `summary_report.pdf`, `price_histogram.png`, and `descriptive_stats.csv` for the results after running the .py file.

The script will output:
- `price_histogram.png` - A histogram visualizing the distribution of camera prices.
- `summary_report.pdf` - A PDF document containing the descriptive statistics.

## Installation
To set up this project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/IDS706_Polars_Descriptive_Statistics_Script.git
    ```

2. Navigate to the project directory:
    ```sh
    cd IDS706_Polars_Descriptive_Statistics_Script
    ```

3. Create a virtual environment (optional but recommended):
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required packages:
    ```sh
    make install
    ```

## Usage
You can run the main script using:
```sh
python main.py

```

## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change. Please ensure to update tests as appropriate.
