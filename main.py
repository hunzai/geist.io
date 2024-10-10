# main.py
import asyncio
from agents.best_sold import BestSold
from agents.utils import Util
import argparse

async def main(url):
    # Paths to your schema files
    category_schema_file = "agents/schemas/kleinanzeigen.de/links.json"
    product_schema_file = "agents/schemas/kleinanzeigen.de/product.json"

    # Initialize BestSold with schema file paths
    best_sold_items = BestSold(category_schema_file, product_schema_file)

    # Run the extraction process
    final_data = await best_sold_items.run(base_url)
    Util.save_to_file(final_data, "data/products.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="params")
    parser.add_argument("--url", type=str, help="--url is missing",  required=True)

    base_url = parser.parse_args().url
    asyncio.run(main(base_url))
