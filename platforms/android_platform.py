from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class AndroidPlatform:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_settings(self):
        self.driver.terminate_app("com.android.settings")
        self.driver.activate_app("com.android.settings")
        if self.driver.current_package != "com.android.settings":
            self.driver.terminate_app(self.driver.current_package)
            self.driver.activate_app("com.android.settings")

    def is_locked(self):
        return self.driver.is_locked()

    def set_screen_lock(self, pswd):
        try:
            # Open Settings
            self.open_settings()

            # Scroll to Security & privacy
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true))'
                    '.scrollIntoView(new UiSelector().text("Security & privacy"))')
                )
            ).click()

            # Device unlock
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Device unlock").instance(1)')
                )
            ).click()

            # None displayed
            self.wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("None")')
                )
            )

            # Screen lock
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Screen lock")')
                )
            ).click()

            # Password
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Password")')
                )
            ).click()

            # Input password and click NEXT
            self.wait.until(
                EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
            ).send_keys(pswd)
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NEXT")').click()

            # Input password and CONFIRM
            self.wait.until(
                EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
            ).send_keys(pswd)
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("CONFIRM")').click()
            
            # Done
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Done")')
                )
            ).click()

            # Password is displayed
            return self.wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Password")')
                )
            )

        except Exception as e:
            print(f"[Failed] Unexpected error: {e}")
            return False

    def unset_screen_lock(self, pswd):
        try:
            # Open Settings
            self.open_settings()

            # Scroll to Security & privacy
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true))'
                    '.scrollIntoView(new UiSelector().text("Security & privacy"))')
                )
            ).click()

            # Device unlock
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Device unlock")')
                )
            ).click()

            # Password displayed
            self.wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Password")')
                )
            )

            # Screen lock
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Screen lock")')
                )
            ).click()

            # Input password and click ENTER
            self.wait.until(
                EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
            ).send_keys(pswd)
            self.driver.press_keycode(66) # ENTER
            
            # Click None
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("None")')
                )
            ).click()

            # Click Delete
            self.wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Delete")')
                )
            ).click()

            # None is displayed
            return self.wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("None")')
                )
            )
            
        except Exception as e:
            print(f"[Failed] Unexpected error: {e}")
            return False
        
    def unlock_screen_with_password(self, pswd):
        try:
            self.driver.lock()
            sleep(2)
            self.driver.unlock()
            sleep(2)

            # Input password and click ENTER
            self.wait.until(
                EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
            ).send_keys(pswd)
            self.driver.press_keycode(66) # ENTER
            sleep(2)
            return True
        
        except Exception as e:
            print(f"[Failed] Unexpected error: {e}")
            return False
        
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
            element = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{target}").fromParent(new UiSelector().className("android.widget.TextView").instance(1))'
            )
            return element.text
        except Exception as e:
            print(f"Failed to get value for {target}: {e}")
            return None

    def get_device_info(self):
        # Open Settings
        self.open_settings()

        # Click About
        self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().textContains("About"))')
            )
        ).click()

        # Get Info
        self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Basic info")')
            )
        )
        info = {}
        info['Device Name'] = self._get_device_info_value("Device name")
        info['OS Version'] = self._get_device_info_value("Android version")
        info['Model Name'] = self._get_device_info_value("Model")

        print(f"[Android Device Info] {info}")
        return info
