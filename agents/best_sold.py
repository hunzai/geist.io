# agents/best_sold.py
from common.crawler import Crawler
from agents.utils import Util

class BestSold:
    def __init__(self, category_schema_file, product_schema_file):
        # Store file paths for the schemas
        self.category_schema_file = category_schema_file
        self.product_schema_file = product_schema_file

        self.marketplace = Crawler()
        # Load the schemas from the provided files
        self.category_schema = Util.load_schema(self.category_schema_file)
        self.product_schema = Util.load_schema(self.product_schema_file)

    async def get_links(self, url):
        """Fetch category links asynchronously from a marketplace website."""
       
        data = await self.marketplace.extract_data(url, self.category_schema)
        return data

    async def get_products(self, links):
        """Fetch product data asynchronously from the category listing links."""
        urls = [item['url'] for item in links]
        print(f'{urls}')

        product_data = await self.marketplace.extract_data_multiple(urls, self.product_schema)
        return product_data

    async def run(self, base_url):
        """Run the process of extracting category and product data asynchronously."""
        links = await self.get_links(base_url)
 
        full_urls = Util.prepend_base_url(links, base_url)
        product_data = await self.get_products(full_urls)
        return product_data
