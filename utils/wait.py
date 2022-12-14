from selenium.common import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import time
from envs import get_logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
logger = get_logger('google_reviews')


def wait_element_for_send(driver, by, element, data):
    attempts = 20
    while attempts:
        try:
            input_email = driver.find_element(by, element)
            input_email.send_keys(data)
            logger.info('Send data')
            return True
        except Exception as e:
            logger.info(f'{e}')
            attempts -= 1
            time.sleep(1)
    raise 'Error while wait_element_for_send'

def wait_element_for_click(driver, by, element):
    attempts = 20
    while attempts:
        try:
            input_email = driver.find_element(by, element)
            input_email.click()
            logger.info('Click on button')
            return True
        except Exception as e:
            logger.info(f'{e}')
            attempts -= 1
            time.sleep(1)
    return

def switch_to_iframe(driver,frame):
    attempts = 20
    while attempts:
        try:
            driver.switch_to.frame(frame)
            logger.info('Switch to frame')
            return True
        except Exception as e:
            logger.info(f'{e}')
            attempts -= 1
            time.sleep(1)
    raise 'Error while switch_to_iframe'





