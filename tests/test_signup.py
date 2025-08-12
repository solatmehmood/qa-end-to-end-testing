from pages.register import Register

def test_signup(driver):
    register = Register(driver)         # create Register page object
    register.open_signup_page()         # open the signup page
    register.fill_signupForm()          # fill the signup form
    register.submit_form()               # submit the form

    # Assert that after signup the user is redirected to a URL containing 'login'
    assert "login" in driver.current_url, "Signup Failed"
