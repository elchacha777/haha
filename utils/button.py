import time

from envs import get_logger

logger = get_logger('google_reviews')
# Rezension schreiben




def get_button(buttons):
    attempts = 20
    for i in range(attempts):
        logger.info('start function get_button')

        try:
            for button in buttons:
                review = button.get_attribute('data-value')
                logger.info(f'get attribute {review}')
                if review == 'Оставить отзыв':
                    time.sleep(1)
                    return button
                elif review == 'Write a review':
                    time.sleep(1)
                    return button

        except Exception as e:
            logger.info(f'{e}')
            attempts -= 1
            time.sleep(1)
    return


def click_on_button(driver, button):

    attempts = 20
    while attempts:
        try:

            driver.execute_script("var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);", button)

            return True
        except Exception as e:
            logger.info(f'{e}')
            attempts -= 1
            time.sleep(1)
    raise 'Cant click on button'