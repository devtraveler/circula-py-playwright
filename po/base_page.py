from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # Example of the functions in this page
    def navigate(self, url: str):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()
