from selenium.webdriver.common.by import By


class Login_locators:

    USERNAME = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
    PASSWORD = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
    LOGIN_BUTTON =(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")

class Click_admin_nav:
    ADMIN_NAV = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span")

class Click_user_management:

    USERS_MANGEMENT = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span/i")
    USERS = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a")
    JOB = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span")
    JOB_TITLE = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a")
    ORGANISATION = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span")
    GENERAL_INFORMATION = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]/a")
    QUALIFICATION = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span")
    SKILLS = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]/a")

class Click_pim:

    PIM_NAV = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]")
    CLICK_CONFIGURATION = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]")

class Click_leave:

    LEAVE = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]")
    ENTITLEMENT = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span")
    REPORTS = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span")
    CONFIGURE = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[5]/span")

class Click_time_nav:

    TIME_NAV = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span")
    TIMESHEET = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span")
    ATTENDANCE = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span")
    # CUSTOMERS = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]/a")

class Click_recruitment_side_nav:

    RECRUITMENT = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span")

class Click_myinfo_nav:

    MYINFO = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span")

class Click_performance:

    PERFORMANCE = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span")

class Click_dashboard:

    DASBOARD = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span")

class Click_directory:

    DIRECTORY = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span")

class User_dropdown:

    DROPDOWN = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i")
    LOGOUT = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a")










