import time

from user.tests.template_class import TemplateClass
from selenium.webdriver.common.by import By


class PypJoinPage(TemplateClass):
    Button_Click_Hero_Join = (
        By.XPATH,
        "/html/body/div[1]/main/div/div[2]/div[1]/div[1]/div/div[2]/div/a",
    )
    Select_Premium1 = (
        By.XPATH,
        "/html/body/div[1]/main/div/div[2]/div[1]/div[1]/div/div[1]/div/div[1]/a",
    )
    Select_Premium2 = (
        By.XPATH,
        "/html/body/div[1]/main/div/div[2]/div[1]/div[1]/div/div[1]/div/div[2]/a",
    )

    """
    Get the url's from the pageurls.csv page and open it.
    """

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)
        self.driver.maximize_window()

    def back_page(self, driver):
        driver.back()

    def page_title(self):
        return self.get_title()

    def page_url(self):
        return self.get_url()

    def host_name(self, url):
        return self.get_hostname(url)

    def path_name(self, url):
        path = self.get_path(url).replace("/", "")
        return path

    def query_string_present(self, url):
        query_string_present = self.check_query_string_present(url)
        assert (
            query_string_present == False
        ), "Query string should not present in the given input URL \n"

    def click_join_button(self):
        is_visible = self.is_visible(self.Button_Click_Hero_Join)
        assert is_visible == True, "The Button is not visible"
        print("Clicked on JOIN button")
        self.button_click(self.Button_Click_Hero_Join)
        print("Navigated to Application page \n")

    def qs_value_from_name(self, url, name):
        qs_value = self.get_qs_value_by_name(url, name)
        return qs_value

    def search_name(self, experience_name):
        sub_string = self.get_sub_string_from_experience(experience_name)
        return sub_string

    def qs_as_json_object(self, url):
        qs_json_object = self.get_qs_json_object(url)
        return qs_json_object

    def compare_qs_values(self, key, expected_value, passed_value):
        self.compare_values(key, expected_value, passed_value)

    def default_premium(self):
        default_premium = self.find_default_premium()
        return default_premium

    def default_campaignid(self, premium, flow):
        default_campaignid = self.find_default_campaignid(premium, flow)
        return default_campaignid

    def select_premium(self, prem_type):
        if prem_type == "premium1":
            self.button_click(self.Select_Premium1)
            print("Selected premium 1")
        elif prem_type == "premium2":
            self.button_click(self.Select_Premium2)
            print("Selected premium 2")

    def compare_all_qs_params_in_json_for_pyp(
        self, landing_page_qs_params, application_page_qs_params
    ):
        self.compare_query_string_parameters_for_pyp(
            landing_page_qs_params, application_page_qs_params
        )
