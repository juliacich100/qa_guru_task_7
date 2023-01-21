from selene.support.shared import browser
from selene import be, by
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "juliacich100")
@allure.feature("Issues in repo")
@allure.story("With allure steps approach")
@allure.link("https://github.com", name="Testing")
def test_github_issue_name_with_allure_step():
    with allure.step('Open the main page'):
        browser.open('https://github.com')

    with allure.step('Look for a repo'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').send_keys('juliacich100/allure_reports_lecture')
        browser.element('.header-search-input').submit()

    with allure.step('Follow the repo link'):
        browser.element(by.link_text('juliacich100/allure_reports_lecture')).click()

    with allure.step('Open Issues tab'):
        browser.element('#issues-tab').click()

    with allure.step('Issue named "My first issue" should be visible'):
        browser.element(by.partial_text('first issue')).should(be.visible)