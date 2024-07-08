import requests
from parser import Parser
from storage import Storage

class Crawler:
    def __init__(self, url: str, depth: int):
        self.url = url
        self.depth = depth
        self.parser = Parser()
        self.storage = Storage()

    def start_crawl(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            content = response.text
            self.parse_content(content)
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch URL {self.url}: {str(e)}")

    def parse_content(self, content: str):
        try:
            data = self.parser.parse_html(content)
            self.save_results(data)
        except Exception as e:
            raise Exception(f"Failed to parse content: {str(e)}")

    def save_results(self, data):
        try:
            self.storage.save_to_db(data)
        except Exception as e:
            raise Exception(f"Failed to save results: {str(e)}")
