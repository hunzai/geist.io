import json
import asyncio
from crawl4ai import AsyncWebCrawler
import asyncio
from crawl4ai.async_crawler_strategy import AsyncPlaywrightCrawlerStrategy
from playwright.async_api import Browser, Page

async def on_browser_created(browser: Browser):
    print("[HOOK] on_browser_created")
    context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
    # context.add_cookies(cookies=cookies)
    page = await context.new_page()
    await page.close()
    await context.close()

async def after_goto(page: Page):
    print("[HOOK] after_goto")
    # await page.get_by_test_id("gdpr-banner-accept").dblclick(force=True)
    await page.screenshot(path="screenshots/load.png")
    print("type")
    await page.type("#site-search-query", "dji mini pro")
    await page.click("#site-search-submit")

    # await page.close()
    # await context.close()

async def main():
    crawler_strategy = AsyncPlaywrightCrawlerStrategy(verbose=True, headless=False)
    crawler_strategy.set_hook('on_browser_created', on_browser_created)
    crawler_strategy.set_hook('after_goto', after_goto)

    async with AsyncWebCrawler(verbose=True, crawler_strategy=crawler_strategy) as crawler:
        result = await crawler.arun(
            url="https://www.kleinanzeigen.de/stadt/berlin/",
            # js_code="window.scrollTo(0, document.body.scrollHeight);",
            # wait_for="footer"
            screenshot=True, 
        )

        print(result.session_id)
    # print(result)

asyncio.run(main())