# import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#
# print(BASE_DIR)
#
# int2 = 2
# int1 = 0
# _id = 1
# while True:
#     try:
#         int1 / int2
#         print(_id)
#
#         print('asdkljajsd')
#         _id+=1
#     except:
#         print('cant make it')

#
# def find_frame(self):
#     for i in range(21):
#         try:
#             frame = self.driver.find_element(By.NAME, "goog-reviews-write-widget")
#             return frame
#             break
#         except:
#             logger.info('cant change to frame')
#
#
# def find_button(self, by, element):
#     for i in range(21):
#         try:
#             button = self.driver.find_element(by, element)
#             return button
#             break
#         except:
#             logger.info('cant change to frame')
#
#
# def find_buttons(self, by, element):
#     for i in range(21):
#         try:
#             button = self.driver.find_element(by, element)[-1]
#             return button
#             break
#         except:
#             logger.info('cant change to frame')
#             time.sleep(1)
#
#
# def wait_element_for_click_1(self, element):
#     attempts = 20
#     while attempts:
#         try:
#             input_email = self.driver.find_element(element)
#             input_email.click()
#             logger.info('Click on button')
#             return True
#         except Exception as e:
#             logger.info(f'{e}')
#             attempts -= 1
#             time.sleep(1)
#     return
#
#
# def open_review(self):
#     cookie_accept_btn = cookie_accept_btn_exists(self.driver)
#
#     if cookie_accept_btn:
#         click_on_button(self.driver, cookie_accept_btn)
#         logger.info(f'cookie_accept_btn pressed {cookie_accept_btn}')
#         time.sleep(7)
#         self.get_review_page()
#     else:
#         logger.info(f'NO COOKIE BUTTON!!!')
#
#     time.sleep(5)
#     buttons = self.driver.find_elements(By.XPATH, '//div[@class="TrU0dc kdfrQc"]/button')[-1]
#     logger.info(f'{buttons}')
#     time.sleep(10)
#
#     logger.info('Open google maps')
#
#     time.sleep(10)
#     time.sleep(5)
#     click_on_button(self.driver, buttons)
#     logger.info(f'{buttons} to click')
#     # click_on_button(button)
#     logger.info('Click on button to leave review')
#     time.sleep(25)
#
#     # frame = self.driver.find_element(By.NAME, "goog-reviews-write-widget")
#     frame = self.find_frame()
#     time.sleep(10)
#     # self.driver.switch_to.frame(frame)
#     switch_to_iframe(self.driver, frame)
#     logger.info(f'switched to frame')
#     time.sleep(20)
#     # button = self.driver.find_elements(By.CLASS_NAME, 's2xyy')
#
#     b = self.find_button(By.XPATH, '//*[@id="kCvOeb"]/div[1]/div[3]/div/div[2]/div/div[5]')
#     logger.info('found button star')
#     time.sleep(10)
#     self.wait_element_for_click_1(b)
#     # for i in range(21):
#     #     try:
#     #         b.click()
#     #     except:
#     #         self.driver.execute_script("var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);", b)
#
#     logger.info('web driver wait')
#
#     time.sleep(20)
#     # parent = self.driver.find_element(By.ID, 'ZRGZAf')
#     child = self.find_buttons(By.CLASS_NAME, 'VfPpkd-RLmnJb')
#     # child = parent.find_element(By.CLASS_NAME, 'VfPpkd-RLmnJb')
#     logger.info(f'{child}')
#
#     time.sleep(10)
#     self.wait_element_for_click_1(child)
#     # self.driver.execute_script("var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);", child)
#
#     logger.info('Review created')
