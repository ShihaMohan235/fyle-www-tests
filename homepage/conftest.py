from simplebrowser import SimpleBrowser
import logging
import pytest
import os
import time

logger = logging.getLogger(__name__)

@pytest.fixture(scope='module')
def base_url():
   return 'https://ww2.fylehq.com'

@pytest.fixture(scope='module')
def module_browser(base_url):
    browser = os.getenv('BROWSER', 'chrome')
    device = None
    logger.debug('creating browser %s, device %s', browser, device)
    module_browser = SimpleBrowser(browser=browser, device=device)
    module_browser.get(base_url)
    module_browser.input(xpath="//span[contains(@class, 'banner-close')]", click=True)
    return module_browser
