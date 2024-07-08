from crawler import Crawler

def initialize_crawler(url: str, depth: int):
    return Crawler(url, depth)

def run_crawl(crawler: Crawler):
    crawler.start_crawl()

def process_results(raw_data):
    # Process the raw data if needed
    pass
