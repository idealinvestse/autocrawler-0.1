from bs4 import BeautifulSoup

class MyParser:
    def parse_html(self, html_content: str):
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            data = self.extract_data(soup)
            return data
        except Exception as e:
            raise Exception(f"Failed to parse HTML: {str(e)}")

    def extract_data(self, soup):
        try:
            # Example extraction logic
            data = {
                "url": soup.find("meta", property="og:url")["content"],
                "title": soup.title.string,
                "metadata": soup.find_all("meta"),
                # Add other common elements extraction here
            }
            return data
        except Exception as e:
            raise Exception(f"Failed to extract data: {str(e)}")
