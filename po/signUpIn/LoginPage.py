from po.base import BasePage

class LoginPage(BasePage):
    
    # Locate web elements here
    USERNAME_INPUT = '#username'
    PASSWORD_INPUT = '#password'
    LOGIN_BUTTON = '#login'

    # Define methods that are related to the Web Elements above
    def enter_username(self, username: str):
        self.page.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.page.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.page.click(self.LOGIN_BUTTON)

    def click_free_trial(self):
        self.page.get_by_role('link', name='Start a free trial').click()
