import time

from appium import webdriver

def test_launchGoogleChrome():
    caps =  dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android',
        browserName='Chrome'
    )

    driver = webdriver.Remote("http://127.0.0.1:4723",desired_capabilities=caps)
    driver.get("https://google.com")
    print(driver.title)
    time.sleep(3)
    driver.quit()
    
