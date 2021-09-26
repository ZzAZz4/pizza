from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from src.page.gmail_login_popup import GmailLoginPopup
from src.page.landing_page import LandingPage
from src.page.confirm_address_page import SelectAddressPage

from src.data.credentials import Credentials

import time

def main():
    credentials = Credentials.from_file('secret/info.json')
    with Chrome(ChromeDriverManager().install()) as driver:
        main_window = driver.current_window_handle
        
        driver.get("https://papajohns.com.pe")
        
        landing_page = LandingPage(driver)
        landing_page.go_to_login()
        
        login_popup = GmailLoginPopup(driver)
        popup_window = login_window_handle(driver, main_window)
        driver.switch_to.window(popup_window)
        login_popup.login(credentials.email, credentials.password)
        driver.switch_to.window(main_window)
        
        confirm_address = SelectAddressPage(driver)
        confirm_address.select_address()
        
        
        time.sleep(1000)

def login_window_handle(driver, main_window):
    
    for handle in driver.window_handles:
        if handle != main_window:
            return handle

if __name__ == '__main__':
    main()