import os
import time
from simplebrowser import SimpleBrowser
import logging
import pytest

logger = logging.getLogger(__name__)

# TODO baseurl has to be changed
@pytest.fixture
def browser(module_browser, base_url):
    module_browser.get(base_url+'/templates/expense-reports')
    time.sleep(3)
    return module_browser

def test_h1_text(browser):
    e = browser.find(xpath='//h1')
    assert e.text == "Free Expense Report Templates", "h1 text is not matching"

def test_element_present(browser):
    h1 = browser.find_many(xpath='//h1')
    assert len(h1)!=0, "There should be atleast one h1 in page"
    h2 = browser.find_many(xpath='//h2')
    assert len(h2)!=0, "There should be atleast one h2 in page"

def test_h1_count(browser):
    e = browser.find_many(xpath='//h1')
    assert len(e)==1, "Expected h1 count is one"

def test_element_fontsize(browser):
    h1 = browser.find(xpath='//h1').value_of_css_property('font-size')
    assert h1=='50px', "expected font size of h1 is 50px"
    h2 = browser.find(xpath='//h2').value_of_css_property('font-size')
    assert h2=='30px', "expected font size of h2 is 30px"



