import requests

# Assuming the Parser class is defined elsewhere and needs to be imported
from parser_1 import Parser
from storage import Storage

class Crawler:
    def __init__(self, url: str, depth: int):
        self.url = url
        self.depth = depth
        self.parser = Parser()  # Ensure Parser is correctly initialized
        self.storage = Storage()

    def start_crawl(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Checks for HTTP request errors
            content = response.text
            self.parse_content(content)
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch URL {self.url}: {str(e)}") from e

    def parse_content(self, content: str):
        try:
            data = self.parser.parse_html(content)  # Parses the HTML content
            self.save_results(data)
        except Exception as e:
            raise Exception(f"Failed to parse content: {str(e)}") from e

    def save_results(self, data):
        try:
            self.storage.save_to_db(data)  # Saves parsed data to the database
        except Exception as e:
            raise Exception(f"Failed to save results: {str(e)}") from e