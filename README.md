# appium-pytest-demo

This project demonstrates native mobile automation testing using **Appium**, **Pytest**, and **Python** for both **Android** and **iOS** platforms. It runs on emulators/simulators and is designed to perform basic device-level interactions (e.g., app launching, screen locking, etc.) in a **modular and cross-platform** way.

> ✅ Tested on:  
> - **Android Emulator:** Android 16 (API level 34)  
> - **iOS Simulator:** iOS 18.4  
> > ⚠️ iOS simulators do not support screen locking; such test cases will be skipped. For full coverage, connect a real iOS device.

---

## Design Philosophy

1. **Modular Platform Abstraction**  
   Android and iOS interactions are encapsulated in platform-specific modules under `drivers/`, allowing the **same test case** to run on both platforms by switching a single config.

2. **Unified Test Framework with Pytest**  
   The project uses Pytest as the main runner to keep test structure clean, readable, and easy to maintain. Platform switching is done via command-line parameters.

3. **Extendable & Scalable Architecture**  
   The framework is built to support future expansion (e.g., more device actions, real device cloud providers, CI integration), ensuring flexibility for diverse mobile automation needs.

---

## Prerequisites

Before running the tests, ensure your system meets the following requirements:

### General
- Python 3.8+
- Node.js & npm
- Java JDK 8 or later (required for Android emulator & Appium)
- Homebrew (on macOS, optional but recommended)

### Android Emulator Setup
- [Android Studio](https://developer.android.com/studio) installed with:
  - Android SDK Tools
  - Android Virtual Device (AVD) Manager
- Make sure `$ANDROID_HOME` is set and `adb` is in your `PATH`
- One or more Android Virtual Devices (AVD) created and bootable

### iOS Simulator Setup (macOS only)
- [Xcode](https://developer.apple.com/xcode/) with Command Line Tools
- Accept the Xcode license (run once):
  ```bash
  sudo xcodebuild -license accept
  ```
- At least one iOS Simulator (e.g., iPhone 14) available

### Appium & Drivers
Install minimal Appium components globally:

```bash
npm install -g appium appium-uiautomator2-driver appium-xcuitest-driver
```

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/linkenmin/appium-pytest-demo.git
   cd appium-pytest-demo
   ```

2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Python dependencies**

   ```bash
   pip install --upgrade pip
   pip install --no-cache-dir -r requirements.txt
   ```

---

## Run the Tests

- **Run on both Android and iOS emulators**

  ```bash
  pytest
  ```

- **Run on Android emulator**

  ```bash
  pytest --platform=android
  ```

- **Run on iOS simulator**

  ```bash
  pytest --platform=ios
  ```

- **Skip unsupported iOS tests gracefully**  
  Some tests (like screen lock) will auto-skip on iOS simulator with a warning.

> ⚠️ Test Order Note:
> Some tests (e.g., screen lock scenarios) require a specific execution order (e.g., set and unset screen lock password).
> To ensure reliability, test cases are prefixed with numbers (e.g., test_001_xxx, test_002_yyy) to enforce deterministic ordering.

---

## Project Structure

```
├── platforms/                     # Platform-specific Appium setup and actions
│   ├── android_platform.py
│   └── ios_platform.py
├── tests/                         # Test cases for both android and ios platforms
│   └── test_cases.py
├── utils/                         # Utility to load and parse platform config
│   └── driver_utils.py            
├── conftest.py                    # Pytest fixtures for driver initialization
├── pytest.ini                     # Custom test configuration
└── requirements.txt               # Python dependencies (appium, selenium, pytest)
```