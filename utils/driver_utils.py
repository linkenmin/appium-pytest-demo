from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

def setup_driver(platform: str):
    if platform.lower() == "android":
        opts = UiAutomator2Options()
        opts.platform_name = "Android"
        opts.device_name = "emulator-5554"
        opts.automation_name = "UiAutomator2"
        return webdriver.Remote("http://localhost:4723", options=opts)
    elif platform.lower() == "ios":
        opts = XCUITestOptions()
        opts.platform_name = "iOS"
        opts.device_name = "iPhone 16 Pro Max"
        opts.platform_version = "18.4"
        opts.automation_name = "XCUITest"
        return webdriver.Remote("http://localhost:4723", options=opts)
    else:
        raise ValueError(f"Unsupported platform: {platform}")