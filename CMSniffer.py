import requests
from bs4 import BeautifulSoup
import re
import argparse
import json
import csv

def detect_cms(url):
    """Advanced CMS detection using multiple fingerprinting techniques."""
    cms_signatures = {
        'WordPress': ['wp-content', 'wp-includes', 'xmlrpc.php', 'wp-json', 'wp-login.php', 'generator:wordpress', 'powered by wordpress'],
        'Joomla': ['Joomla!', 'Joomla CMS', 'com_content', 'administrator/components', 'generator:joomla', 'powered by joomla'],
        'Drupal': ['drupal.js', 'sites/all/modules', 'generator:drupal', 'drupal-settings', 'powered by drupal'],
        'Magento': ['Mage.Cookies', 'varien/js', 'generator:magento', 'adminhtml/default', 'powered by magento'],
        'Shopify': ['cdn.shopify.com', 'shopify-checkout', 'generator:shopify', 'shopify-section'],
        'Wix': ['wix.com', 'X-Wix-Request-Id', 'generator:wix', 'powered by wix'],
        'Squarespace': ['squarespace.com', 'generator:squarespace', 'powered by squarespace'],
        'TYPO3': ['typo3temp/', 'typo3conf/', 'generator:typo3', 'typo3_src'],
        'PrestaShop': ['prestashop', 'generator:prestashop', 'js/jquery/plugins/jquery.easing.js'],
        'BigCommerce': ['cdn.bigcommerce.com', 'bigcommerce.js', 'stencil-cli'],
        'Blogger': ['blogger.com', 'generator:blogger', 'blogspot.com'],
        'OpenCart': ['index.php?route=', 'generator:opencart', 'catalog/view/theme'],
        'Bitrix': ['bitrix/templates', 'generator:bitrix', 'bx-core'],
        'Ghost': ['ghost.js', 'generator:ghost', 'powered by ghost'],
        'osCommerce': ['osCommerce', 'oscommerce.js', 'admin/login.php'],
        'Concrete5': ['concrete/js', 'generator:concrete5', 'ccm_basePath'],
        'ExpressionEngine': ['ExpressionEngine', 'generator:expressionengine', 'exp:channel'],
        'SilverStripe': ['SilverStripe', 'generator:silverstripe', 'framework/core'],
        'Weebly': ['weebly.com', 'generator:weebly', 'powered by weebly'],
        'Django': ['X-Powered-By: Django', 'django-admin', 'csrfmiddlewaretoken'],
        'Flask': ['X-Powered-By: Flask', 'werkzeug.debug', 'flask.session'],
        'MediaWiki': ['generator:mediawiki', 'Special:Version', 'mw-config'],
        'vBulletin': ['vBulletin', 'generator:vbulletin', 'vb_login'],
        'phpBB': ['phpBB', 'phpbb.js', 'viewtopic.php'],
        'XenForo': ['xenforo', 'generator:xenforo', 'xf_user'],
        'Moodle': ['Moodle', 'generator:moodle', 'theme/yui_combo.php'],
        'Zyro': ['zyro.com', 'generator:zyro', 'powered by zyro'],
        'MODX': ['MODX', 'generator:modx', 'connectors/index.php'],
        'Contao': ['contao', 'generator:contao', 'system/modules'],
        'Umbraco': ['Umbraco', 'generator:umbraco', 'umbraco_client'],
        'Plone': ['plone.app', 'portal_css', 'generator:plone'],
        'Kentico': ['Kentico', 'CMSPages', 'generator:kentico'],
        'Sitefinity': ['Sitefinity', 'Telerik.Sitefinity', 'generator:sitefinity'],
        'Liferay': ['Liferay', 'generator:liferay', 'portal_normal.vm']
    }

    paths = ['', 'robots.txt', 'sitemap.xml', 'readme.html', 'license.txt', 'admin', 'login', 'wp-admin', 'joomla/administrator', 'user/login', 'index.php', 'config.php', 'CHANGELOG.txt', 'admin/config', 'admin/index.php', 'install.php', 'sites/default/settings.php', 'adminer.php', 'phpinfo.php', 'feed', 'install', 'LICENSE', 'SECURITY.txt', 'UPGRADE.txt', 'version.txt']
    found_cms = None
    
    try:
        for path in paths:
            full_url = f"{url.rstrip('/')}/{path}"
            response = requests.get(full_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            meta_generator = soup.find('meta', attrs={'name': 'generator'})
            
            for cms, signatures in cms_signatures.items():
                if any(re.search(sig, response.text, re.IGNORECASE) for sig in signatures):
                    found_cms = cms
                    break
                if meta_generator and any(re.search(sig, meta_generator.get('content', ''), re.IGNORECASE) for sig in signatures):
                    found_cms = cms
                    break
            
            if found_cms:
                break
        
        return found_cms if found_cms else "CMS not detected"
    
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def output_result(data, output_format):
    """Output the result in the specified format."""
    if output_format == 'csv':
        with open('cms_detection.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['URL', 'Detected CMS'])
            writer.writerows(data)
    elif output_format == 'json':
        with open('cms_detection.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
    else:
        with open('cms_detection.txt', 'w') as txtfile:
            for url, cms in data:
                txtfile.write(f"URL: {url}, Detected CMS: {cms}\n")

def main():
    parser = argparse.ArgumentParser(description="Detect CMS from a website.")
    parser.add_argument('-u', '--url', type=str, help="Single URL to detect CMS")
    parser.add_argument('-l', '--list', type=str, help="File with list of URLs to detect CMS")
    parser.add_argument('-o', '--output', choices=['csv', 'txt', 'json'], default='txt', help="Output format")

    args = parser.parse_args()
    
    if args.url:
        try:
            result = detect_cms(args.url)
            print(f"URL: {args.url}, Detected CMS: {result}")
            output_result([(args.url, result)], args.output)
        except Exception as e:
            print(f"Error processing URL {args.url}: {e}")
    
    if args.list:
        try:
            with open(args.list, 'r') as file:
                urls = file.readlines()
            data = []
            for url in urls:
                url = url.strip()
                result = detect_cms(url)
                print(f"URL: {url}, Detected CMS: {result}")
                data.append((url, result))
            output_result(data, args.output)
        except FileNotFoundError:
            print(f"Error: The file '{args.list}' was not found.")
        except Exception as e:
            print(f"Error processing the list of URLs: {e}")

if __name__ == "__main__":
    main()
