from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from LoginLocators.locators import Login_locators, Click_admin_nav, Click_user_management, Click_pim, Click_leave, \
    Click_time_nav, Click_recruitment_side_nav, Click_myinfo_nav, Click_performance, Click_dashboard, Click_directory, \
    User_dropdown


class login_pages:

    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, user_name):
        username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.USERNAME))
        username.send_keys(user_name)

    def enter_password(self, password):
        username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.PASSWORD))
        username.send_keys(password)

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Login_locators.LOGIN_BUTTON))
        login_button.click()

        time.sleep(4)


class admin_nav:

    def __init__(self, driver):
        self.driver = driver

    def click_admin_nav(self):
        admin_nav_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Click_admin_nav.ADMIN_NAV))
        admin_nav_button.click()



class User_management:

    def __init__(self, driver):
        self.driver = driver

    def click_user_management(self):
        admin_user_management = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_user_management.USERS_MANGEMENT))
        admin_user_management.click()

    def click_users(self):
        admin_users = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_user_management.USERS))
        admin_users.click()

    def click_job(self):
        admin_job = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_user_management.JOB))
        admin_job.click()

    def click_job_title(self):
        admin_job_title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_user_management.JOB_TITLE))
        admin_job_title.click()

    def click_organisation(self):
        admin_organisation = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_user_management.ORGANISATION))
        admin_organisation.click()

    def click_general_information(self):
        admin_general_information = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_user_management.GENERAL_INFORMATION))
        admin_general_information.click()

    def click_qualification(self):
        admin_qualification = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_user_management.QUALIFICATION))
        admin_qualification.click()

    def click_skills(self):
        admin_skills = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_user_management.SKILLS))
        admin_skills.click()

class Click_pim_nav:

    def __init__(self, driver):
            self.driver = driver

    def click_pim(self):
        admin_pim = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_pim.PIM_NAV))
        admin_pim.click()

    def click_configuration(self):
        admin_configuration = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_pim.CLICK_CONFIGURATION))
        admin_configuration.click()

class leave_side_nav:

    def __init__(self, driver):
            self.driver = driver

    def click_leave(self):
        click_admin_leave = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_leave.LEAVE))
        click_admin_leave.click()

    def click_entitlement(self):
        click_entitlement = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_leave.ENTITLEMENT))
        click_entitlement.click()

    def click_reports(self):
        click_admin_report = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_leave.REPORTS))
        click_admin_report.click()

    def click_configure(self):
        click_admin_configure = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_leave.CONFIGURE))
        click_admin_configure.click()

class Time_side_nav:

    def __init__(self, driver):
            self.driver = driver

    def click_time_nav(self):
        click_admin_time = WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located(Click_time_nav.TIME_NAV))
        click_admin_time.click()

    def click_timesheet(self):
        click_admin_timesheet = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_time_nav.TIMESHEET))
        click_admin_timesheet.click()

    def click_attendance(self):
        click_admin_attendance = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_time_nav.ATTENDANCE))
        click_admin_attendance.click()

    # def click_customers(self):
    #     click_admin_customers = WebDriverWait(self.driver, 20).until(
    #         EC.presence_of_element_located(Click_time_nav.CUSTOMERS))
    #     click_admin_customers.click()

class Recruitment_side_nav:

    def __init__(self, driver):
            self.driver = driver

    def click_recruitment(self):
        click_admin_recruitment = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_recruitment_side_nav.RECRUITMENT))
        click_admin_recruitment.click()

class Myinfo_side_nav:

    def __init__(self, driver):
            self.driver = driver

    def click_myinfo(self):
        click_admin_myinfo = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_myinfo_nav.MYINFO))
        click_admin_myinfo.click()

class Performance_side_nav:

    def __init__(self, driver):
            self.driver = driver

    def click_performance(self):
        click_admin_performance = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_performance.PERFORMANCE))
        click_admin_performance.click()

class Dashboard_side_nav:

    def __init__(self, driver):
            self.driver = driver

    def click_dashboard(self):
        click_admin_dashboard = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_dashboard.DASBOARD))
        click_admin_dashboard.click()

class Directory_side_nav:

    def __init__(self, driver):
            self.driver = driver

    def click_directory(self):
        click_admin_directory = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_directory.DIRECTORY))
        click_admin_directory.click()

class User_drop_down:

    def __init__(self, driver):
            self.driver = driver

    def click_dropdown(self):
        click_user_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(User_dropdown.DROPDOWN))
        click_user_dropdown.click()

    def log_out(self):
        click_user_logout = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(User_dropdown.LOGOUT))
        click_user_logout.click()




























