CMS Detector 🚀

🔍 Overview

CMS Detector is a powerful Python-based tool that can scan and detect 30+ CMS platforms with high accuracy. Whether you're performing security analysis or just curious about a website's backend technology, this tool has you covered!

✨ Features

🚀 Detects 30+ CMS platforms including WordPress, Joomla, Drupal, Magento, Shopify, Wix, and many more.

📂 Supports scanning a single URL or multiple URLs from a file.

📊 Multiple output formats: TXT, CSV, JSON.

🔎 Uses advanced fingerprinting techniques with BeautifulSoup and regex for precise detection.

📌 Requirements

Python 3.x

Required libraries:

pip install requests beautifulsoup4

⚡ Usage

🔹 Scan a Single URL

python cms_detector.py -u <URL>

Example:

python cms_detector.py -u https://example.com

🔹 Scan Multiple URLs from a File

python cms_detector.py -l urls.txt

📂 urls.txt should contain a list of URLs, one per line.

🔹 Output in Different Formats

python cms_detector.py -u <URL> -o <format>

✅ Supported formats: txt, csv, json

Example:

python cms_detector.py -u https://example.com -o json

📜 Example Output

URL: https://example.com, Detected CMS: WordPress

📁 Files Included

cms_detector.py → Main script for detecting CMS.

cms_detection.csv → Output file (if selected).

cms_detection.json → Output file (if selected).

cms_detection.txt → Output file (if selected).

👨‍💻 Author

Chirag Mistry

🚀 Start scanning today and discover the CMS behind any website!
