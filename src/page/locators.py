from selenium.webdriver.common.by import By


class LandingPageLocators(object):
    """"""
    
    ADDRESS_SELECT = By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/section/div[2]/header/div/div/div[3]/div[2]/a'
    LOGIN_BUTTON = By.CLASS_NAME, 'google'
    


class GmailPageLocators(object):
    """A class for gmail login page locators"""
    
    EMAIL_FIELD = (By.XPATH, '//*[@id="identifierId"]')
    PASSW_FIELD = (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    

class AddressPageLocators(object):
    """"""
    
    CONTINUE = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div/div/div[5]/button')
    ADDRESS = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div/div/div[4]/button')
    
    
    
