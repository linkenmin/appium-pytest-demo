from platforms.android_platform import AndroidPlatform
from platforms.ios_platform import IosPlatform
import pytest


def test_001_set_screen_lock(driver, platform):
    if platform == 'android':
        actions = AndroidPlatform(driver)
        assert actions.set_screen_lock(pswd='1234')
    else:
        pytest.skip(f"Platform {platform} not supported")

def test_002_unlock_screen_with_password_wrong(driver, platform):
    if platform == 'android':
        actions = AndroidPlatform(driver)
        assert actions.unlock_screen_with_password(pswd='1111')
        assert actions.is_locked()
    else:
        pytest.skip(f"Platform {platform} not supported")

def test_003_unlock_screen_with_password(driver, platform):
    if platform == 'android':
        actions = AndroidPlatform(driver)
        assert actions.unlock_screen_with_password(pswd='1234')
        assert not actions.is_locked()
    else:
        pytest.skip(f"Platform {platform} not supported")

def test_004_unset_screen_lock(driver, platform):
    if platform == 'android':
        actions = AndroidPlatform(driver)
        assert actions.unset_screen_lock(pswd='1234')
    else:
        pytest.skip(f"Platform {platform} not supported")

def test_005_unlock_screen_with_none(driver, platform):
    if platform == 'android':
        actions = AndroidPlatform(driver)
        assert actions.unlock_screen_with_none()
        assert not actions.is_locked()
    elif platform == 'ios':
        actions = IosPlatform(driver)
        assert actions.unlock_screen_with_none()
        assert not actions.is_locked()
    else:
        pytest.skip(f"Platform {platform} not supported")

def test_006_device_info(driver, platform):
    if platform == 'android':
        actions = AndroidPlatform(driver)
        info = actions.get_device_info()
    elif platform == 'ios':
        actions = IosPlatform(driver)
        info = actions.get_device_info()
    else:
        pytest.skip(f"Platform {platform} not supported")

    assert info.get('Device Name'), "Device Name should not be empty"
    assert info.get('OS Version'), "OS Version should not be empty"
    assert info.get('Model Name'), "Model Name should not be empty"