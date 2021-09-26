from .locators import AddressPageLocators
from ..browser.web_page import WebPage
from ..browser.clickable_elem import ClickableElem


class ContinueButton(ClickableElem):
    locator = AddressPageLocators.CONTINUE


class AddressSelection(ClickableElem):
    locator = AddressPageLocators.ADDRESS
    
class SelectAddressPage(WebPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.address_selection = AddressSelection(self)
        self.continue_button = ContinueButton(self)
        
    def select_address(self):
        self.address_selection.click()
        self.continue_button.click()