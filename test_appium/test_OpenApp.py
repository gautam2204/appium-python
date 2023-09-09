import time

from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver

def test_openingApp():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android',
        appActivity=' com.code2lead.kwad',
        mainActivity='com.code2lead.kwad.MainActivity'
    )

    
    appium_server_url = 'http://localhost:4723'
    driver = webdriver.Remote(appium_server_url, capabilities)
    el = driver.find_element(by=AppiumBy.ID, value='com.code2lead.kwad:id/EnterValue')
    el.click()
    time.sleep(3)
    driver.back()
    driver.quit()
