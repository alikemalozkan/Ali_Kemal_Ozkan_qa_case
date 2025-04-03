import unittest
from selenium import webdriver

class InsiderTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://useinsider.com")

    def test_title(self):
        self.assertIn("Insider", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
