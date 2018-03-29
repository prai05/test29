from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def teatDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Prai go to homepage
        self.browser.get('http://localhost:8000')

        # page title 
        self.assertIn('Quiz', self.browser.title)
        self.fail('Finish the test!')

        # questions and ans

        # score true false

if __name__ == '__main__':
    unittest.main(warnings='ignore')
