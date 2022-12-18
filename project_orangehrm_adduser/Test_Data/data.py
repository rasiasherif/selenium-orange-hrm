class HRM_Data:
    username = "Admin"
    password = "admin123"
    firstname = "mehwish"
    middlename = "n"
    lastname = "mehwish"
    DL = "DL0055"

# Python Class for Selenium Selectors
class HRM_Selectors:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    pim_xpath = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'

class HRM_AddEmp_Selectors:
    input_box_firstName = "firstName"
    input_box_middleName = "middleName"
    input_box_lastName = "lastName"
    input_box_nickName_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    input_box_DL_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'

    pim_add_emp_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    pim_save_emp_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    pim_select_emp_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div'
    pim_edit_emp_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div'
    pim_edit_save_emp_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    pim_delete_emp_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/div/div[9]/div/button[1]'
    pim_delete_confirm_emp_xpath = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'

