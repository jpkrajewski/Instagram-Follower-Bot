from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
import time

ALLOW_COOKIES_XPATH = '/html/body/div[4]/div/div/button[1]'
LOGIN_BUTTON_XPATH = '//*[@id="loginForm"]/div/div[3]/button'
TURN_OFF_NOTIFICATIONS_XPATH = '/html/body/div[5]/div/div/div/div[3]/button[2]'
SEARCHBAR_SELECTOR = "input[placeholder='Szukaj']"
FOLLOWERS_LINK_XPATH = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
FOLLOWERS_POPUP_XPATH = '/html/body/div[6]/div/div/div/div[2]/ul/div/html/body/div[6]/div/div/div/div[2]/ul/div'
CANCEL_BUTTON_XPATH = '/html/body/div[7]/div/div/div/div[3]/button[2]'


class InstagramAutomatedFollowing:

    def __init__(self, driver_path: str):
        self.driver_path = driver_path
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service)

    def login(self, username: str, password: str):
        self.driver.get('https://www.instagram.com/')
        self.driver.find_element(by=By.XPATH, value=ALLOW_COOKIES_XPATH).click()
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value='username').send_keys(username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(password)
        self.driver.find_element(by=By.XPATH, value=LOGIN_BUTTON_XPATH).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=TURN_OFF_NOTIFICATIONS_XPATH).click()

    def find_followers(self, similar_account: str):
        search = self.driver.find_element(by=By.CSS_SELECTOR, value=SEARCHBAR_SELECTOR)
        search.send_keys(similar_account)
        time.sleep(5)
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=FOLLOWERS_LINK_XPATH).click()
        time.sleep(5)
        followers_list = self.driver.find_element(by=By.CLASS_NAME, value='isgrP')

        for i in range(20):
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                followers_list)
            time.sleep(1)

    def follow(self):
        buttons = self.driver.find_elements(by=By.CSS_SELECTOR, value='li button')
        for button in buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value=CANCEL_BUTTON_XPATH)
                cancel_button.click()
