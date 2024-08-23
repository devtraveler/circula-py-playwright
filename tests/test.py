from playwright.sync_api import sync_playwright

def test_select_country_and_verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navigate the Circula Website
        page.goto("https://www.circula.com/en")

        # Locate a Login web Element by using text
        login_button = page.get_by_role('link', name="Login")
        login_button.click()

        # Locate the Accept All Button
        accept_all_button = page.get_by_test_id('uc-accept-all-button')
        accept_all_button.click()

        # Locate the start a free trial link
        free_trial_button = page.get_by_role('link', name='Start a free trial')
        free_trial_button.click()

        # Locate the Accept All Button
        accept_all_button = page.get_by_test_id('uc-accept-all-button')
        accept_all_button.click()
        
        # Locate the input and click on it to reveal options
        country_input = page.locator('input[aria-expanded="false"]')

        # Scroll to the input element
        country_input.scroll_into_view_if_needed()

        # Click to expand the input element
        country_input.click()

        # Select Sweden from the input options by text
        sweden_option = page.locator('text=Sweden')
        sweden_option.click()

        # Verify that Sweden is selected
        assert country_input.input_value() == "Sweden"
        
        print("Sweden has been successfully selected in the dropdown.")
        
        # Close the browser
        browser.close()

# Run the test
test_select_country_and_verify()