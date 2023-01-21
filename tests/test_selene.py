from selene.support.shared import browser
from selene import be, by
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "juliacich100")
@allure.feature("Issues in repo")
@allure.story("No steps approach")
@allure.link("https://github.com", name="Testing")
def test_github_issue_name():
    browser.open('https://github.com')

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys('juliacich100/allure_reports_lecture')
    browser.element('.header-search-input').submit()
    browser.element(by.link_text('juliacich100/allure_reports_lecture')).click()

    browser.element('#issues-tab').click()
    browser.element(by.partial_text('first issue')).should(be.visible)
