from po.base import BasePage

class LandingPage(BasePage):
    
    # Locate web elements here
    landing_header = '#landing_header'

    # Define methods that are related to the Web Elements above
    def is_landing_page_displayed(self):
        return self.page.is_visible(self.landing_header)

    def click_login_link(self):
        self.page.get_by_role('link', name="Login").click()