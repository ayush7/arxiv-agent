import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url="https://www.nbcnews.com/business",    
                                    magic=True,
                                    headless=False,
                                    simulate_user=True,
                                    override_navigator=True,
                                    js_code="window.scrollTo(0, document.body.scrollHeight);",
                                    wait_for="css:.lazy-content",
                                    delay_before_return_html=2.0)
        # print(result.markdown)
        # print(result)
        # Access internal and external links
        internal_links = result.links["internal"]
        external_links = result.links["external"]

        print(internal_links)
        print(len(internal_links))

        for link in internal_links:
            print(link)

if __name__ == "__main__":
    asyncio.run(main())