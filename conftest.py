import pytest
from utils.driver_utils import setup_driver

drivers = {}

def pytest_addoption(parser):
    parser.addoption(
        "--platforms",
        action="store",
        default="android,ios",
        help="Comma-separated list of platforms to test, e.g. android,ios"
    )

def pytest_sessionstart(session):
    platforms = [p.strip() for p in session.config.getoption("--platforms").split(",")]
    for p in platforms:
        print(f"[SETUP] Launching driver for platform: {p}")
        drivers[p] = setup_driver(p)

def pytest_sessionfinish(session, exitstatus):
    print('')
    for name, driver in drivers.items():
        print(f"[TEARDOWN] Quitting driver for platform: {name}")
        driver.quit()

def pytest_generate_tests(metafunc):
    if "platform" in metafunc.fixturenames:
        platforms = metafunc.config.getoption("--platforms").split(",")
        metafunc.parametrize("platform", [p.strip() for p in platforms])

@pytest.fixture(scope="function")
def driver(platform):
    return drivers[platform]
