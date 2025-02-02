#!/usr/bin/env python3
import sys
import warnings
warnings.filterwarnings('ignore', category=Warning)  # 抑制所有警告

try:
    import requests
    import urllib3
    try:
        import OpenSSL
    except ImportError:
        print("請安裝 pyOpenSSL：", file=sys.stderr)
        print("pip3 install pyOpenSSL", file=sys.stderr)
        sys.exit(1)
except ImportError as e:
    print(f"請安裝必要的套件：{str(e)}", file=sys.stderr)
    print("pip3 install requests beautifulsoup4 pyOpenSSL", file=sys.stderr)
    sys.exit(1)

from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urlparse
import json

def get_page_info(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 清理和轉義文字
        def clean_text(text):
            if not text:
                return ''
            # 移除換行符並替換為空格
            text = ' '.join(text.split())
            # 轉義雙引號
            text = text.replace('"', '&quot;')
            return text
            
        title = clean_text(soup.title.string if soup.title else '')
        
        description = ''
        desc_meta = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', attrs={'property': 'og:description'})
        if desc_meta:
            description = clean_text(desc_meta.get('content', ''))
            
        image = ''
        img_meta = soup.find('meta', attrs={'property': 'og:image'})
        if img_meta:
            image = img_meta.get('content', '')
            
        date = datetime.now().strftime('%Y-%m-%d')
        
        shortcode = f'''{{{{< link-preview-card 
    url="{url}"
    title="{title.strip()}"
    description="{description.strip()}"
    image="{image}"
    date="{date}"
>}}}}'''
        
        return {
            "alfredworkflow": {
                "arg": shortcode,
                "variables": {
                    "url": url,
                    "title": title.strip(),
                    "description": description.strip(),
                    "image": image,
                    "date": date
                }
            }
        }
        
    except Exception as e:
        return {
            "alfredworkflow": {
                "arg": str(e),
                "variables": {
                    "error": str(e)
                }
            }
        }

query = "{query}"
result = get_page_info(query)
print(json.dumps(result)) 