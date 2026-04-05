import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("user, pwd, exp", [("standard_user", "secret_sauce", True), ("wrong", "wrong", False), ("standard_user", "wrong_sauce", False), ("wrong_user", "secret_sauce", False)])

def test_login(setup, user, pwd, exp):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.login(user, pwd)

    if exp:
        assert "inventory" in driver.current_url
    else:
        assert login.get_error() is True

