from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import argparse

# Pre-Reqs
parser = argparse.ArgumentParser(description="This script will create groups in Serv-U")
parser.add_argument("--group", "-g", type=str, help="Group ID")
args=parser.parse_args()

groupname = args.group
homedirectory = "/mnt/project_data/" + groupname
driver = webdriver.Firefox()
driver.maximize_window()

#Log in Stage
driver.get("http://127.0.0.1:43958/?Command=Logout")
#driver.get("https://eidf-mft.epcc.ed.ac.uk/?Command=Logout")

username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-box-text")))
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pword-box-text")))

username_field.send_keys("admin")
password_field.send_keys("admin")

#username_field.send_keys("Admin")
#password_field.send_keys("bitwarden password")


login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-LoginButton")))
login_button.click()

# prod id = 7523
# prod test id = 15033
# local id = 10960
#Admin Domain Stage
admin_domain_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "navmenu-10960-href")))
admin_domain_button.click()

admin_domain_groups_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "navmenu-10960-groups-href")))
admin_domain_groups_link.click()

#Groups Stage
groups_page_ldap = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "PageTabs-item-2-box")))
groups_page_ldap.click()

select_group = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "LDAPGroupsList-row-7")))
select_group.click()

add_child_ldap_group = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-AddChildLDAPGroupButton")))
add_child_ldap_group.click()

#Main Group Info Stage
group_name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Invo__GroupName-box-text")))
group_name_input.send_keys(groupname)

home_directory_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "HomeDir-box-text")))
home_directory_input.send_keys(homedirectory)

#Directory Access Stage
open_directory_access = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "DialogTabs-item-1-box")))
open_directory_access.click()

add_hd_dir_access = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-AddDirButton")))
add_hd_dir_access.click()

#Inputting Directory Access Rule
#Adds path
add_hd_dir_access_rule = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Dir-box-text")))
add_hd_dir_access_rule.send_keys(homedirectory)

add_hd_dir_access_perms = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-FullAccessButton")))
add_hd_dir_access_perms.click()

save_dir_access_rules = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-SaveDirAccessButton")))
save_dir_access_rules.click()

# Starting Limiting Group Permissions
limit_settings_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "DialogTabs-item-7-box")))
limit_settings_tab.click()

# Limit Field drop down menu 
limit_type_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"LimitType-box-text")))
driver.execute_script("arguments[0].removeAttribute('readonly')", limit_type_dropdown) #removing html attribute
limit_type_dropdown.clear()
limit_type_dropdown.send_keys("Advanced")

# Owner ID Section
ownerid_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "LimitsList-cell-0-9-box")))
ownerid_item.click()
owner_edit_limit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"btn-EditLimitButton")))
owner_edit_limit_button.click()

# might not be necessary
owner_limit_confirmation = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-ConfirmDialogYesButton")))
owner_limit_confirmation.click()


owner_select_input =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"LimitEdit-box")))
owner_select_input.click()
owner_value = "nobody"
owner_edit_limit_value = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"LimitEdit-box-text")))
owner_edit_limit_value.send_keys(owner_value)
owner_save_limit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"btn-SaveLimitButton")))
owner_save_limit.click()

#Group ID Section

groupid_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "LimitsList-cell-0-11-box")))
groupid_item.click()

groupid_edit_limit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"btn-EditLimitButton")))
groupid_edit_limit_button.click()

# might not be necessary
groupid_limit_confirmation = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-ConfirmDialogYesButton")))
groupid_limit_confirmation.click()

group_select_input =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"LimitEdit-box")))
group_select_input.click()

group_edit_limit_value = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"LimitEdit-box-text")))
group_edit_limit_value.send_keys(groupname)

group_save_limit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"btn-SaveLimitButton")))
group_save_limit.click()


# Saving Group Properties edits
group_name_save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-SaveGroupButton")))
group_name_save_button.click()
