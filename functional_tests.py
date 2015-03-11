from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new to-do app. She checks out its home
        # page
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        # assert 'To-Do' in browser.title, "Browser title was " + browser.title
        self.assertIn('To Do', self.browser.title)
        self.fail("Finish the test!")

        # She is invited to enter a to-do item right away

        # She types "Buy peacock feathers" into a text box as it's her hobby

        # When she hits Enter, the page updates, and the now the page lists:
        # "1: Buy peacoock feathers" as an item in to-do list.

        # There is still a text box inviting her to make another input. She
        # inputs:
        # "Use peacock feathers to make a fly"

        # The page updates again and not mentions both the items in to-do list

        # Edith wonders whether the site will remember her to-do list. Then
        # she sees that site generated a unique URL for her - there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep


if __name__ == "__main__":
    unittest.main(warnings='ignore')
