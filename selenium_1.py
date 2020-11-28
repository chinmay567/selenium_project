from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import smtplib


cwd = r"C:\Users\Asus\Downloads"
chromedriver_path = f"{cwd}\chromedriver.exe"

# Options for Headless driver
chrome_options = Options()
chrome_options.add_argument("--headless")
# driver Location
# try:
URL = "https://www.amazon.in/ap/signin?_encoding=UTF8&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1"

driver = webdriver.Chrome(
    executable_path=chromedriver_path, chrome_options=None)  # chrome_options
driver.maximize_window()
driver.get(URL)

username = driver.find_element_by_id(
    "ap_email")
username.send_keys("dora.chinmay567@gmail.com")
submit = driver.find_element_by_id("continue")
submit.click()
password = driver.find_element_by_id("ap_password")
password.send_keys("Chinu567..")
login = driver.find_element_by_id("signInSubmit")
login.click()
time.sleep(5)

searchbox = driver.find_element_by_id("twotabsearchtextbox")
searchbox.send_keys("mackbook pro")
search = driver.find_element_by_xpath(
    "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
search.click()

product_url = "https://www.amazon.in/Apple-MacBook-Pro-8th-Generation-Intel-Core-i5/dp/B0883KXHG3/ref=sr_1_1_sspa?dchild=1&keywords=macbook+pro&qid=1604928666&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFERDJLWjkzOUZYR08mZW5jcnlwdGVkSWQ9QTA4MTM2NTkyNEVCWFpYT1dSSExNJmVuY3J5cHRlZEFkSWQ9QTA1NDk0MzMyQ1FLNVEzRkxTT0U3JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
driver.get(product_url)
cart = driver.find_element_by_id("add-to-cart-button")
cart.click()
for_buy = driver.find_elements_by_xpath(
    "/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div/div[4]/div/div/div/span[2]/span/a")
for_buy.click()
driver.quit()

# for sending mail


def sending_mail():
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()
    mail.login('login mail', 'password')
    content = "hi this is chinmay"
    mail.sendmail('mail if form',
                  'mail id for to', content)
    mail.close()
    print("Sent")


sending_mail()
# except Exception as e:
#     print("messege not send!!!")
#     print(e)
