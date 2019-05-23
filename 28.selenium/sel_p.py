import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class CheckPythonSite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_python_site(self):
        self.driver.get("http://www.python.org")
        assert "python" in self.driver.title
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source
        self.driver.find

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

Keys.F1