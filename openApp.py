import time

from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, capabilities)
el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Apps"]')
el.click()
time.sleep(3)
driver.quit()
