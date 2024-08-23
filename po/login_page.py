from po.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.page = page
    
        # Locate web elements here
        self.free_trial_button = page.get_by_role('link', name='Start a free trial')

        USERNAME_INPUT = '#username'
        PASSWORD_INPUT = '#password'
        LOGIN_BUTTON = '#login'

    # Define methods that are related to the Web Elements above

    def click_free_trial(self, free_trial_button):
        self.free_trial_button.click()
