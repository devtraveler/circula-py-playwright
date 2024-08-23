from po.base_page import BasePage

class SignUp(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.page = page
    
        # Locate web elements here
        self.country_input = page.locator('input[aria-expanded="false"]')
        self.sweden_option = page.locator('text=Sweden')
    
    # Define methods that are related to the Web Elements above

    def click_country_input(self,country_input):
        self.country_input.click()

    def scroll_to_country_input(self, country_input):
        self.country_input.scroll_into_view_if_needed()

    def select_sweden(self,sweden_option):
        self.sweden_option.click()
    

