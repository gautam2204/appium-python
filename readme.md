##
Appium Architecture :-
<p>
 Client (Our system with the programming language eg appium-python-client) sends a request to the appium server which we have installed in our machine and running in some port. Server reads those commands and convert those commands to the device which is connected. With UIAutomator2 (For ANdroid) XCUITest(for IOS) it generates an io.appium.settings.apk file in our connected device. Device is connected via 'adb'.
 Appium server reads up the responses produced by the device and logs the same to the appium server port. Background runs selenium task on mobile UI.   

 adb install /path/Android_Demo_App.apk
</p>

Setup:-
<p>
1. On Phone :-

    - Switch to developers mode
    - Switch Mobile to mobile threatering 
    - In developers options turn ON USB Debugging
    - Chines Phone (Disable Permission monitoring) 

2. Install the app to the phone which needs to be tested
    - adb install /path/Android_Demo_App.apk
3.  Open app on home page type below command to get the details of the app
    - adb shell dumpsys window windows
    
    
</p>
