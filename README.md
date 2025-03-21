# owspace-img

A tool to download daily calendar images from the single calendar website (单向历).

## About

This project downloads calendar images from http://img.owspace.com/ starting from 2015-02-18. The images are organized by year and date in a structured folder hierarchy.

## Features

- Concurrent downloading for improved performance
- Configurable date ranges and concurrency level
- GitHub Actions workflow for automated downloads
- Organized image storage

## Installation

This project uses Poetry for dependency management:

```bash
# Clone the repository
git clone https://github.com/jihuayu/owspace-img.git
cd owspace-img

# Install dependencies
poetry install
```

## Usage

### Local execution

```bash
# With default settings (2015-02-18 to 2025-12-31)
poetry run python main.py

# With custom date range and concurrency
START_DATE=2020-01-01 END_DATE=2020-12-31 MAX_WORKERS=30 poetry run python main.py
```

### Using GitHub Actions

1. Go to the Actions tab in your repository
2. Select the "Download Calendar Images" workflow
3. Click "Run workflow"
4. Enter your desired parameters:
   - Start date (YYYY-MM-DD format)
   - End date (YYYY-MM-DD format)
   - Maximum concurrent downloads
5. Click "Run workflow"
6. When the workflow completes, download the artifact containing the images

## Configuration

The script can be configured using the following environment variables:

- `START_DATE`: Starting date in YYYY-MM-DD format (default: 2015-02-18)
- `END_DATE`: Ending date in YYYY-MM-DD format (default: 2025-12-31)
- `MAX_WORKERS`: Maximum number of concurrent downloads (default: 20)

## Output Structure

Images will be saved in the following structure:
```
img
└── YYYY
    └── MMDD.jpg
```

Example: `./img/2015/0218.jpg`
```