from selenium import webdriver
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def teatDown(self):
        self.browser.quit()

    def test_can_select_choice_for_question(self):
        # ศรัณย์เข้าเว็บ http://localhost:8000
        self.browser.get('http://localhost:8000')

        # ศรัณย์เห็น title Quiz
        self.assertIn('Quiz', self.browser.title)

        # ศรัณย์ กด Start link ไปหน้า http://localhost:8000/question/
        start = self.browser.find_element_by_link_text('Start')
        self.assertEqual(start.get_attribute('href'), 'http://localhost:8000/question/')
        start.click()
        time.sleep(1)

        # ศรัณย์ เห็นคำถามข้อแรก
        question_text1 = self.browser.find_element_by_name('question1').text
        self.assertIn('1+1=2?', question_text1)

        # ศรัณย์ กดเลือก True
        choice1 = self.browser.find_element_by_tag_name('input')
        self.assertEqual(choice1.get_attribute('name'), 'choice1')
        choice1.click()
        time.sleep(1)

        # ศรัณย์ กด Submit
        submit1 = self.browser.find_element_by_name('submit')
        self.assertEqual(submit1.get_attribute('value'), 'Submit')
        submit1.click()

        # ศรัณย์ เห็นคะแนน
        results = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Results =  1 / 3', results)
        time.sleep(2)

        # ศรัณย์ กด Quiz again เพื่อย้อนกลับไปทำใหม่
        quiz_again = self.browser.find_element_by_link_text('Quiz again?')
        self.assertEqual(quiz_again.get_attribute('href'), 'http://localhost:8000/question/')
        quiz_again.click()
        time.sleep(1)

        # ศรัณย์ ตอบคำถามทุกข้อ
        choice1 = self.browser.find_element_by_name('choice1')
        self.assertEqual(choice1.get_attribute('value'), 'True')
        choice1.click()
        time.sleep(1)

        question_text2 = self.browser.find_element_by_name('question2').text
        self.assertIn('5+10=14?', question_text2)

        choice2 = self.browser.find_element_by_name('choice2')
        self.assertEqual(choice2.get_attribute('value'), 'True')
        choice2.click()
        time.sleep(1)

        question_text3 = self.browser.find_element_by_name('question3').text
        self.assertIn('4/2=2?', question_text3)

        choice3 = self.browser.find_element_by_name('choice3')
        self.assertEqual(choice3.get_attribute('value'), 'True')
        choice3.click()
        time.sleep(1)

        # ศรัณย์ กด Submit
        submit2 = self.browser.find_element_by_name('submit')
        self.assertEqual(submit2.get_attribute('value'), 'Submit')
        submit2.click()
        time.sleep(1)

        # ศรัณย์ เห็นคะแนน
        results = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Results =  2 / 3', results)


        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
