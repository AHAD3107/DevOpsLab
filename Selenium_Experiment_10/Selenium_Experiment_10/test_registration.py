from pathlib import Path
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


FORM_PATH = Path(__file__).with_name("registration.html").resolve()
FORM_URL = FORM_PATH.as_uri()
SCREENSHOT_DIR = Path(__file__).with_name("screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)


class RegistrationFormTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Selenium Manager manages the matching ChromeDriver automatically.
        options = Options()
        cls.driver = webdriver.Edge(options=options)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get(FORM_URL)

    def fill_valid_form(self):
        self.driver.find_element(By.ID, "studentName").send_keys("Rahul Sharma")
        self.driver.find_element(By.ID, "rollNumber").send_keys("CSE2026001")
        self.driver.find_element(By.ID, "email").send_keys("rahul.sharma@example.com")
        self.driver.find_element(By.ID, "mobile").send_keys("9876543210")
        Select(self.driver.find_element(By.ID, "department")).select_by_visible_text(
            "Computer Science"
        )

    def test_1_valid_submission(self):
        self.fill_valid_form()
        self.driver.save_screenshot(str(SCREENSHOT_DIR / "01_completed_form.png"))
        self.driver.find_element(By.ID, "submitButton").click()
        result = self.wait.until(
            EC.visibility_of_element_located((By.ID, "result"))
        )
        self.assertIn("Registration submitted successfully", result.text)
        self.driver.save_screenshot(str(SCREENSHOT_DIR / "02_success_result.png"))
        print("PASS: Submit valid student details")

    def test_2_empty_name_validation(self):
        self.fill_valid_form()
        name = self.driver.find_element(By.ID, "studentName")
        name.clear()
        self.driver.find_element(By.ID, "submitButton").click()
        is_valid = self.driver.execute_script(
            "return arguments[0].checkValidity()", name
        )
        self.assertFalse(is_valid, "An empty required name should be invalid")
        self.assertTrue(
            self.driver.find_element(By.ID, "result").get_attribute("hidden") is not None
        )
        print("PASS: Empty name is blocked by required-field validation")

    def test_3_invalid_email_validation(self):
        self.fill_valid_form()
        email = self.driver.find_element(By.ID, "email")
        email.clear()
        email.send_keys("not-an-email")
        self.driver.find_element(By.ID, "submitButton").click()
        is_valid = self.driver.execute_script(
            "return arguments[0].checkValidity()", email
        )
        self.assertFalse(is_valid, "An invalid email should be rejected")
        self.assertTrue(
            self.driver.find_element(By.ID, "result").get_attribute("hidden") is not None
        )
        print("PASS: Invalid email is blocked by email validation")

    def test_4_page_title(self):
        self.assertEqual(self.driver.title, "Student Registration Form")
        print("PASS: Page title matches expected value")

    def test_5_submit_valid_data_again(self):
        self.fill_valid_form()
        self.driver.find_element(By.ID, "submitButton").click()
        result = self.wait.until(
            EC.visibility_of_element_located((By.ID, "result"))
        )
        self.assertIn("Rahul Sharma", result.text)
        print("PASS: Second valid submission succeeds")


if __name__ == "__main__":
    unittest.main(verbosity=2)
