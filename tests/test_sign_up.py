# This file will contain the tests that are related to the sign-up process
import sys
import os
import pytest

# Add the project root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from po.landing_page import LandingPage
from po.login_page import LoginPage
from po.signup_page import SignUp
from playwright.sync_api import sync_playwright

@pytest.mark.select_sweden_option
def test_select_sweden_option():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Instantiate the page objects with the page context
        landing_page = LandingPage(page)
        login_page = LoginPage(page)
        signup_page = SignUp(page)

        # Navigate to the Circula Website
        page.goto("https://www.circula.com/en")

        # Verify the title of the Circula Website
        landing_page.verify_title_of_landing_page()

        # Click the login link on the landing page
        landing_page.click_login_link(landing_page.login_button)

        # Locate and click the "Accept All" button for cookies
        accept_all_button = page.get_by_test_id('uc-accept-all-button')
        accept_all_button.click()

        # Click the "Free Trial" button on the login page
        login_page.click_free_trial(login_page.free_trial_button)

        # Locate and click the "Accept All" button for cookies
        accept_all_button = page.get_by_test_id('uc-accept-all-button')
        accept_all_button.click()

        # Scroll to the country input field on the sign-up page and select Sweden
        signup_page.scroll_to_country_input(signup_page.country_input)
        signup_page.click_country_input(signup_page.country_input)
        signup_page.select_sweden(signup_page.sweden_option)

        # Verify that Sweden is selected
        assert signup_page.country_input.input_value() == "Sweden"
        
        print("Sweden has been successfully selected in the dropdown.")

        # Close the browser
        browser.close()


