from po.base_page import BasePage

class LandingPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.page = page
        self.title_of_landing_page = "SMEs manage employee expenses with Circula | Circula"


        # define and locate web elements below
        self.login_button = page.get_by_role('link', name="Login")    
   

    # Define methods that are related to the Web Elements above
    def is_landing_page_displayed(self):
        return self.page.is_visible(self.landing_header)

    def click_login_link(self, login_button):
        self.login_button.click()