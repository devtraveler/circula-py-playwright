from po.base_page import BasePage
from playwright.sync_api import sync_playwright, expect


class LandingPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.page = page
        self.title_of_landing_page = "SMEs manage employee expenses with Circula | Circula"

        # define and locate web elements below
        self.login_button = page.get_by_role('link', name="Login")    
   

    # Define methods that are related to the Web Elements above
    def verify_title_of_landing_page(self):
        expect(self.page).to_have_title(self.title_of_landing_page)

    def click_login_link(self, login_button):
        self.login_button.click()