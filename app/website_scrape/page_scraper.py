import asyncio
from crawl4ai import AsyncWebCrawler
from copy import deepcopy



class ScrapePage:
    """
    Simply takes a url and scrapes the page and returns urls and scraped content for the page.
    Can be made more complex but making a simple version for now
    """

    def __init__(self, url=None) -> None:
        self.url = url 

    def update_url(self, new_url):
        self.url = new_url

    async def scrape_page(self):
        """
        Returns a dictionary based on the current url
        Treat it like an invoker 
        
        {
            "page_content":,
            "internal_links":,
            "external_links":,
            "raw":
        }

        """
        output = {
                    "page_content":None,
                    "internal_links":None,
                    "external_links":None,
                    "raw":None

                  }
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(url=self.url,    
                                        # magic=True,
                                        # headless=False,
                                        # simulate_user=True,
                                        # override_navigator=True,
                                        # js_code="window.scrollTo(0, document.body.scrollHeight);",
                                        # wait_for="css:.lazy-content",
                                        # delay_before_return_html=2.0
                                        )
            
            markdown_result = result.markdown
            links = result.links

            # internal_links = result.links["internal"]
            # external_links = result.links["external"]

            output["page_content"] = deepcopy(markdown_result)
            output["links"] = links
            output["raw"] = deepcopy(result)

        
        return output

            
        