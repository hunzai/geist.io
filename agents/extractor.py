# agents/extractor.py

from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

class MarketPlace:

    async def extract_data_multiple(self, urls, schema):
        async with AsyncWebCrawler(verbose=True) as crawler:
            results = await crawler.arun_many(
                urls=urls,
                js_code="window.scrollTo(0, document.body.scrollHeight);",
                wait_for="footer"
            )

        if not results[0].success: #todo
            raise RuntimeError(f"Failed to crawl the page: {urls}")

        extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)
        # return result
        data = []
        for result in results:
            content = extraction_strategy.extract('', result.html)
            data.append({'url': result.url, 'data': content})
        return data
   
    async def extract_data(self, url, schema):
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(
                url=url,
                js_code="window.scrollTo(0, document.body.scrollHeight);",
                wait_for="footer"
            )

        if not result.success:
            raise RuntimeError(f"Failed to crawl the page: {url}")

        extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)
        return extraction_strategy.extract('', result.html)
