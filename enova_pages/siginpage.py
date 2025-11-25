from utils.helpers import input_value, click_on
from utils.locators import SigninPage
from utils.vpn_activity import *


def check_homepage(driver):

    text = match_element(driver,HomePage.home_page_check)

    if 'disconnected' in text :
          return True


def validate_signin_with_email_password(driver, email , password ):
    print("Testing the login file ")
    #input email
    input_value(driver,SigninPage.email_input_field,email)
    input_value(driver,SigninPage.password_input_field,password)
    click_on(driver,SigninPage.signin_button)

    return check_homepage(driver)



def validate_signin_with_gmail(driver):

    click_on(driver,SigninPage.social_login_button)

    click_on(driver,SigninPage.gmail_account)
    return check_homepage(driver)

def validate_signin_with_activation_code(driver,code):

    click_on(driver,SigninPage.activation_code_button)

    input_value(driver,SigninPage.activation_code_input_field,code)

    click_on(driver,SigninPage.activation_code_continue_button)
    return check_homepage(driver)



def validate_signin_as_guest(driver):

    click_on(driver,SigninPage.guest_login_button)
    return check_homepage(driver)

