import allure
from selene.support.shared import browser
from selene import be, by


@allure.step('Open the main page')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Look for the {repo}')
def search_for_repo(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys(repo)
    browser.element('.header-search-input').submit()


@allure.step('Follow the repo link')
def go_to_repo(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Open Issues tab')
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Issue containing {text} should be visible')
def find_issue_containing(text):
    browser.element(by.partial_text(text)).should(be.visible)