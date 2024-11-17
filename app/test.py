from website_scrape import page_scraper as scraper
from crawl_website import depth, crawl_helpers
from helpers import params
# from agents import invoke_agents
from pdf_parser import download_pdf, parse_pdf
import asyncio

url = params.scrape_url

# Test website_scrape - Single Page

scrap_obj = scraper.ScrapePage(url=url)
scrap_out = asyncio.run(scrap_obj.scrape_page())


pdf_links = []
for x in scrap_out["links"]["internal"]:
    if 'pdf' in x['href']:
        print(x)
        if x["href"] not in pdf_links:
            pdf_links.append(x["href"])


# Download PDF
for pdflink in pdf_links:
    if download_pdf.is_arxiv_pdf(pdflink):
        download_pdf
