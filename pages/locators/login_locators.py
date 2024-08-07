from selenium.webdriver.common.by import By

email_locator = (By.ID, 'email')
password_locator = (By.ID, 'pass')
button_locator = (By.ID, 'send2')
error_alert_locator = (By.CSS_SELECTOR,
                       ".message-error"
                       )