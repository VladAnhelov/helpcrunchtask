import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class HelpCrunch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("C:\\Users\\владон\\PycharmProjects\\HelpcrunchTest\\Task2\\site0001\\test.html")
        print("Page is load")
        time.sleep(2)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME,"iframe"))
        print("Frame is switched")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"svg").click()
        print("Element is found")
        time.sleep(2)
        driver.find_element_by_id("helpcrunchChatTextarea")
        print("Element is clicked")
        time.sleep(1)
        driver.find_element_by_id("helpcrunchChatTextarea").send_keys("Hello World")
        time.sleep(1)
        driver.find_element_by_class_name("helpcrunch-chat-send-btn").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='Name']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='Name']").send_keys("James")
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='Email']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("jamesbond@gmail.com")
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='Phone number']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='Phone number']").send_keys("0635550007")
        time.sleep(1)
        driver.find_element_by_xpath("//span[@class='checkbox']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(5)
        print("Message is sending and test is complete")
        driver.switch_to.default_content()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)