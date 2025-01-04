import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Action_pages.action_page import login_pages, User_management, admin_nav, Click_pim_nav, leave_side_nav, \
    Time_side_nav, Recruitment_side_nav, Myinfo_side_nav, Performance_side_nav, Directory_side_nav, User_drop_down
from Config import config
from Config.config import Config
from LoginLocators.locators import Click_pim


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode

    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()



@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = login_pages(driver)
    login_page.login_url(Config.BASEURL)
    return login_page

def tests_login_page(login):
    login.enter_username(Config.USERNAME)
    login.enter_password(Config.PASSWORD)
    login.click_login_button()

def test_admin_nav(login):
    click_admin_nav = admin_nav(login.driver)
    click_admin_nav.click_admin_nav()

def test_user_management(login):
    click_user_management = User_management(login.driver)
    click_user_management.click_user_management()

def test_admin_users(login):
    click_on_users = User_management(login.driver)
    click_on_users.click_users()

def test_admin_jobs(login):
    click_on_jobs = User_management(login.driver)
    click_on_jobs.click_job()

def test_admin_job_title(login):
    click_job_title = User_management(login.driver)
    click_job_title.click_job_title()

def test_admin_organisation(login):
    click_admin_organisation = User_management(login.driver)
    click_admin_organisation.click_organisation()

def test_admin_general_information(login):
    click_admin_general_information = User_management(login.driver)
    click_admin_general_information.click_general_information()

def test_admin_qualification(login):
    click_admin_qualification = User_management(login.driver)
    click_admin_qualification.click_qualification()

def test_admin_skills(login):
    click_admin_skills = User_management(login.driver)
    click_admin_skills.click_skills()

def test_pim(login):
    click_on_pim = Click_pim_nav(login.driver)
    click_on_pim.click_pim()

def test_configuration(login):
    click_admin_configuration = Click_pim_nav(login.driver)
    click_admin_configuration.click_configuration()

def test_leave(login):
    click_admin_leave = leave_side_nav(login.driver)
    click_admin_leave.click_leave()

def test_entitlement(login):
    click_admin_entitlement = leave_side_nav(login.driver)
    click_admin_entitlement.click_entitlement()

def test_reports(login):
    click_reports = leave_side_nav(login.driver)
    click_reports.click_leave()

def test_configure(login):
    click_admin_configure = leave_side_nav(login.driver)
    click_admin_configure.click_configure()

def test_time_nav(login):
    click_admin_time = Time_side_nav(login.driver)
    click_admin_time.click_time_nav()

def test_timesheet(login):
    click_admin_timesheet = Time_side_nav(login.driver)
    click_admin_timesheet.click_timesheet()

def test_attendance(login):
    click_admin_attendance = Time_side_nav(login.driver)
    click_admin_attendance.click_attendance()

# def test_customers(login):
#     click_admin_customers = Time_side_nav(login.driver)
#     click_admin_customers.click_customers()

def test_recruitment(login):
    click_admin_recruitment = Recruitment_side_nav(login.driver)
    click_admin_recruitment.click_recruitment()

def test_myinfo(login):
    click_admin_myinfo = Myinfo_side_nav(login.driver)
    click_admin_myinfo.click_myinfo()

def test_performance(login):
    click_admin_performance = Performance_side_nav(login.driver)
    click_admin_performance.click_performance()

def test_directory(login):
    click_admin_directory = Directory_side_nav(login.driver)
    click_admin_directory.click_directory()

def test_dropdown(login):
    click_user_dropdown = User_drop_down(login.driver)
    click_user_dropdown.click_dropdown()

def test_logout(login):
    click_logout = User_drop_down(login.driver)
    click_logout.log_out()