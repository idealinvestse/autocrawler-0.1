import unittest
from main import initialize_crawler, run_crawl, process_results

class TestMainFunctions(unittest.TestCase):

    def test_initialize_crawler(self):
        config = {"url": "http://example.com", "depth": 2}
        result = initialize_crawler(config)
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, dict))

    def test_run_crawl(self):
        result = run_crawl()
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, dict))

    def test_process_results(self):
        raw_data = {"html": "<html><body>Sample Content</body></html>"}
        result = process_results(raw_data)
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, dict))

if __name__ == '__main__':
    unittest.main()
