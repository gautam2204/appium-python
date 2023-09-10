import os
import time

from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
# Step 1 : Import Appium Service class
from appium.webdriver.appium_service import AppiumService
 
def test_RunServerProgRam():
    
    filePath = str(os.path.abspath('Android_Demo_App.apk'))
    # Step 2 : Create object for Appium Service class
    appium_service = AppiumService()
    # Step 3 : Call Start method by using Appium Service class object
    appium_service.start()
    
    # Step 4 : Create "Desired Capabilities"
    
    capabilities = {
    "platformName": "Android",
    "appium:options": {
        "automationName": "UiAutomator2",
        "platformVersion": "13",
        "app": filePath,
        "appPackage":"com.code2lead.kwad",
        "appActivity" : "com.code2lead.kwad.MainActivity",
        "noReset": True,
        # "fullReset":True
    }
}

    
    driver =webdriver.Remote("http://127.0.0.1:4723",capabilities)
    
    ele_id = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue")
    ele_id.click()
    
    time.sleep(5)
    driver.quit()
    
    # Step 5 : Call stop method by using Appium Service class object
    appium_service.stop()
    