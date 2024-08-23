from po.base import BasePage

class SignUp(BasePage):
    
    # Locate web elements here

    # Define methods that are related to the Web Elements above

    def click_country_input(self):
        self.page.locator('input[aria-expanded="false"]').click()


    def scroll_to_Element(self, element):
        self.element.scroll_into_view_if_needed()

    def select_Sweden(self):
        self.page.locator('text=Sweden').click()
    

