# CMS Detector

## Description
This is an advanced CMS (Content Management System) detection script written in Python. It uses multiple fingerprinting techniques to identify the CMS used by a website based on common signatures found in its source code, metadata, and URLs.

## Features
- Detects various CMS platforms, including WordPress, Joomla, Drupal, Magento, Shopify, Wix, and more.
- Supports scanning a single URL or a list of URLs from a file.
- Outputs results in CSV, JSON, or TXT format.
- Uses BeautifulSoup and regular expressions for improved detection.

## Requirements
- Python 3.x
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `argparse`

You can install the required dependencies using:
```bash
pip install requests beautifulsoup4
```

## Usage

### Detect CMS for a single URL
```bash
python cms_detector.py -u <URL>
```
Example:
```bash
python cms_detector.py -u https://example.com
```

### Detect CMS for multiple URLs from a file
```bash
python cms_detector.py -l urls.txt
```
`urls.txt` should contain a list of URLs, one per line.

### Specify output format
```bash
python cms_detector.py -u <URL> -o <format>
```
Supported formats: `txt`, `csv`, `json`.

Example:
```bash
python cms_detector.py -u https://example.com -o json
```

### Example Output
```
URL: https://example.com, Detected CMS: WordPress
```

## Files
- `cms_detector.py`: Main script for detecting CMS.
- `cms_detection.csv`: Output file in CSV format (if selected).
- `cms_detection.json`: Output file in JSON format (if selected).
- `cms_detection.txt`: Output file in TXT format (if selected).

## Author
Chirag Mistry 
[Linkdin](https://www.linkedin.com/in/chirag-mistry-/)
[X- Twitter](https://x.com/mistry4592)
[Medium](https://medium.com/@mistry4592)
