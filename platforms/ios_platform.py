from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class IosPlatform:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_settings(self):
        self.driver.terminate_app("com.apple.Preferences")
        self.driver.activate_app("com.apple.Preferences")
        info = self.driver.execute_script("mobile: activeAppInfo")
        current_bundle = info.get("bundleId")
        if current_bundle != "com.apple.Preferences":
            self.driver.terminate_app(current_bundle)
            self.driver.activate_app("com.apple.Preferences")

    def is_locked(self):
        return self.driver.is_locked()

    def unlock_screen_with_none(self):
        try:
            self.driver.lock()
            sleep(2)
            self.driver.unlock()
            sleep(2)

            return True

        except Exception as e:
            print(f"[Failed] Unexpected error: {e}")
            return False
    
    def _get_device_info_value(self, target):
        try:
            cell = self.wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.IOS_PREDICATE, f'label == "{target}"')
                )
            )
            static_texts = cell.find_elements(AppiumBy.CLASS_NAME, "XCUIElementTypeStaticText")
            if len(static_texts) >= 2:
                return static_texts[1].get_attribute("value")
            else:
                return None
        except Exception as e:
            print(f"Failed to get value for {target}: {e}")
            return None
    
    def get_device_info(self):
        # Open Settings
        self.open_settings()

        # Click General
        self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "General")
            )
        ).click()

        # Click About
        self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "About")
            )
        ).click()

        # Get Info
        self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.IOS_PREDICATE, 'label == "About"')
            )
        )
        info = {}
        info['Device Name'] = self._get_device_info_value("Name")
        info['OS Version'] = self._get_device_info_value("iOS Version")
        info['Model Name'] = self._get_device_info_value("Model Name")

        print(f"[iOS Device Info] {info}")
        return info