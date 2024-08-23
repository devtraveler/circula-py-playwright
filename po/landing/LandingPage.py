from po.base import BasePage

class LandingPage(BasePage):
    
    # Locate web elements here
    DASHBOARD_HEADER = '#dashboard-header'

    # Define methods that are related to the Web Elements above
    def is_dashboard_displayed(self):
        return self.page.is_visible(self.DASHBOARD_HEADER)

    def click_login_link(self):
        self.page.get_by_role('link', name="Login").click()