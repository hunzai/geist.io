# main.py
import asyncio
from agents.kleineanzeigen import Kleinanzeigen
from agents.utils import Util

async def main():
    base_url = ""
    
    # Paths to your schema files
    category_schema_file = "agents/schemas/kleinanzeigen.de/links.json"
    product_schema_file = "agents/schemas/kleinanzeigen.de/product.json"

    # Initialize Kleinanzeigen with schema file paths
    kleinanzeigen = Kleinanzeigen(category_schema_file, product_schema_file)

    # Run the extraction process
    final_data = await kleinanzeigen.run(base_url)
    Util.save_to_file(final_data, "data/products.json")

if __name__ == "__main__":
    asyncio.run(main())
