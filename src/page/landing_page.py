from ..browser.clickable_elem import ClickableElem
from ..browser.web_page import WebPage
from .locators import LandingPageLocators
import time

    
class LandingPage(WebPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.address_selection_link = AddressSelectionLink(self)
        self.google_login_button = GoogleLoginButton(self)
        
    def go_to_login(self):
        self.address_selection_link.click(timeout=5)
        time.sleep(1)
        self.google_login_button.click(timeout=5)   

class AddressSelectionLink(ClickableElem):
    locator = LandingPageLocators.ADDRESS_SELECT
    
    
class GoogleLoginButton(ClickableElem):
    locator = LandingPageLocators.LOGIN_BUTTON
            