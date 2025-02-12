import time

from user.tests.test_base_template import BaseTemplate
from user.tests.aarp_pyp_renew_page_with_parameter import PypRenewPage
from user.Config.config import Global_Env_Data
import csv


class TestAarpPypRenewPageWithParameter(BaseTemplate):
    def test_renew(self):
        self.contents = []
        path_to_file = (
            Global_Env_Data.LOCAL_PATH + Global_Env_Data.TEMPLATE_PYP_WITH_PARAMETER
        )
        with open(path_to_file, mode="r") as file:
            cp_url = csv.reader(file)
            for row in cp_url:
                url = row[0]
                self.contents.append(url)

            for url in self.contents:
                print("Testing the below URL")
                print(url)
                self.renew_page = PypRenewPage(self.driver, url)

                self._page_url = self.renew_page.page_url()

                self._default_premium = self.renew_page.default_premium()
                self._default_rkc1 = self.renew_page.default_campaignid(
                    "premium1", "rkc"
                )
                self._default_rkc2 = self.renew_page.default_campaignid(
                    "premium2", "rkc"
                )

                # Perform the test steps
                self.perform_test_steps_premium1(
                    self._page_url, self._default_premium, self._default_rkc1
                )

                self.driver.back()

                # Clear cookies and refresh the page
                self.driver.delete_all_cookies()
                print("Cookies cleared")
                self.driver.refresh()

                # Perform the test steps
                self.perform_test_steps_premium2(
                    self._page_url, self._default_premium, self._default_rkc2
                )

                # Clear cookies and refresh the page
                self.driver.delete_all_cookies()
                print("Cookies cleared")
                self.driver.refresh()

                print("URL testing completed.")
                print("\n")

            print("********* END OF REPORT *********")
            print("\n")

            self.driver.quit()

    def perform_test_steps_premium1(self, page_url, default_premium, default_rkc1):
        self.full_page_screenshot_lp = lambda x: self.driver.execute_script(
            "return document.body.parentNode.scroll" + x
        )
        self.driver.set_window_size(
            self.full_page_screenshot_lp("Width"),
            self.full_page_screenshot_lp("Height"),
        )  # May need manual adjustment
        self.driver.find_element("tag name", "body").screenshot(
            "user/static/reports/html/screenshot/onload_screenshot.png"
        )

        self._host_name = self.renew_page.host_name(page_url)

        self._path = self.renew_page.path_name(page_url)

        self._qs_json_lp_page = self.renew_page.qs_as_json_object(page_url)

        print("Premium 1: \n")
        if default_premium == "premium2":
            # select premium 1
            print("select premium 1")
            self.renew_page.select_premium("premium1")

        self.renew_page.click_renew_button()

        self._application_page_url = self.renew_page.page_url()
        time.sleep(2)

        self.full_page_screenshot_app = lambda x: self.driver.execute_script(
            "return document.body.parentNode.scroll" + x
        )
        self.driver.set_window_size(
            self.full_page_screenshot_app("Width"),
            self.full_page_screenshot_app("Height"),
        )  # May need manual adjustment
        self.driver.find_element("tag name", "body").screenshot(
            "user/static/reports/html/screenshot/application_page.png"
        )

        self._qs_json_application_page = self.renew_page.qs_as_json_object(
            self._application_page_url
        )

        self.renew_page.compare_all_qs_params_in_json_for_pyp(
            self._qs_json_lp_page, self._qs_json_application_page
        )

        self._campaign_id = self.renew_page.qs_value_from_name(
            self._application_page_url, "campaignid"
        )

        self._tc_hpc = self.renew_page.qs_value_from_name(
            self._application_page_url, "tc_hpc"
        )

        self._tc_tm_version = self.renew_page.qs_value_from_name(
            self._application_page_url, "tc_tm_version"
        )

        self.renew_page.compare_qs_values("campaignid", default_rkc1, self._campaign_id)

        self.renew_page.compare_qs_values("tc_hpc", self._host_name, self._tc_hpc)
        self.renew_page.compare_qs_values(
            "tc_tm_version", self._path, self._tc_tm_version
        )

    def perform_test_steps_premium2(self, page_url, default_premium, default_rkc2):
        self.full_page_screenshot_lp = lambda x: self.driver.execute_script(
            "return document.body.parentNode.scroll" + x
        )
        self.driver.set_window_size(
            self.full_page_screenshot_lp("Width"),
            self.full_page_screenshot_lp("Height"),
        )  # May need manual adjustment
        self.driver.find_element("tag name", "body").screenshot(
            "user/static/reports/html/screenshot/onload_screenshot.png"
        )

        self._host_name = self.renew_page.host_name(page_url)

        self._path = self.renew_page.path_name(page_url)

        self._qs_json_lp_page = self.renew_page.qs_as_json_object(page_url)

        print("Premium 2: \n")
        if default_premium == "premium1":
            self.renew_page.select_premium("premium2")

        self.renew_page.click_renew_button()

        self._application_page_url2 = self.renew_page.page_url()
        time.sleep(2)

        self.full_page_screenshot_app = lambda x: self.driver.execute_script(
            "return document.body.parentNode.scroll" + x
        )
        self.driver.set_window_size(
            self.full_page_screenshot_app("Width"),
            self.full_page_screenshot_app("Height"),
        )  # May need manual adjustment
        self.driver.find_element("tag name", "body").screenshot(
            "user/static/reports/html/screenshot/application_page2.png"
        )

        self._qs_json_application_page = self.renew_page.qs_as_json_object(
            self._application_page_url
        )

        self.renew_page.compare_all_qs_params_in_json_for_pyp(
            self._qs_json_lp_page, self._qs_json_application_page
        )

        self._campaign_id = self.renew_page.qs_value_from_name(
            self._application_page_url2, "campaignid"
        )

        self._tc_hpc = self.renew_page.qs_value_from_name(
            self._application_page_url2, "tc_hpc"
        )

        self._tc_tm_version = self.renew_page.qs_value_from_name(
            self._application_page_url2, "tc_tm_version"
        )

        self.renew_page.compare_qs_values("campaignid", default_rkc2, self._campaign_id)

        self.renew_page.compare_qs_values("tc_hpc", self._host_name, self._tc_hpc)
        self.renew_page.compare_qs_values(
            "tc_tm_version", self._path, self._tc_tm_version
        )
