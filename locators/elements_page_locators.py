
class PageLocators:

    FULL_NANE = ('xpath', '//input[@id="userName"]')
    EMAIL = ('xpath', '//input[@id="userEmail"]')
    CURRENT_ADDRESS = ('xpath', '//*[@id="currentAddress"]')
    PERMANENT_ADDRESS = ('xpath', '//*[@id="permanentAddress"]')
    SUBMIT = ('xpath', "//button[@id='submit']")

    CREATED_FULL_NAME = ('xpath', '#output #name')
    CREATED_EMAIL = ('xpath', '#output #name')
    CREATED_CURRENT_ADDRESS = ('xpath', '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = ('xpath', '#output #permanentAddress')
