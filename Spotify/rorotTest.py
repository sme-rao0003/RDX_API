
from robot.libraries.BuiltIn import BuiltIn

def start_chrome_for_testing_example():
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium import webdriver

    opts = Options()
    opts.add_argument("--no-sandbox")
    opts.add_argument("--start-maximized")

    opts.binary_location = r'C:\opt\chrome_for_testing\chrome-win64\chrome.exe'
    chromedriver = r"C:\opt\chrome_for_testing\chromedriver-win64\chromedriver.exe"
    browser = webdriver.Chrome(options=opts, service=Service(chromedriver))

    selenium_library = BuiltIn().get_library_instance("SeleniumLibrary")
    selenium_library._drivers.register(browser, 'chrome')