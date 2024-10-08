# agents/utils.py

import json
from urllib.parse import urljoin

class Util:
    @staticmethod
    def load_schema(schema_file):
        with open(schema_file, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_to_file(data, file_path):
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)
        print(f"Data saved to {file_path}")

    @staticmethod
    def extract_links(data):
        return [item.get('url') for item in data.get('links', []) if item.get('url')]

    @staticmethod
    def extract_products(data):
        return data.get('items', [])

    @staticmethod
    def prepend_base_url(links, base_url):
        return [{'url': urljoin(base_url, link['url'])} for link in links]
