from tests import decorator_steps
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "juliacich100")
@allure.feature("Issues in repo")
@allure.story("Decorator steps approach")
@allure.link("https://github.com", name="Testing")
def test_github_issue_name_using_decorator_steps():
    decorator_steps.open_main_page()
    decorator_steps.search_for_repo('juliacich100/allure_reports_lecture')
    decorator_steps.go_to_repo('juliacich100/allure_reports_lecture')
    decorator_steps.open_issues_tab()
    decorator_steps.find_issue_containing('first issue')