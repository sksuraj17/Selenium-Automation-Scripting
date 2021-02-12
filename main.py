#                             **********************SELENIUM AUTOMATION SCRIPTING**********************
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("C:\\Program Files\\Python39\\Lib\\site-packages\\chromedriver.exe")
driver.get("https://www.thesparksfoundationsingapore.org")

# TEST CASE 1:ABOUT US -> GUIDING PRINCIPLES
try:
    driver.find_element_by_link_text('About Us').click()
    time.sleep(2)
    driver.find_element_by_link_text('Guiding Principles').click()
    time.sleep(4)
    print('Successfully visited the Guiding Principles page of About Us.\n')
except NoSuchElementException:
    print("About us / Guiding Principles page does not exist.\n")
    time.sleep(1)

# TEST CASE 2:HOME LINK
try:
    driver.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Home link is Working.\n")
except NoSuchElementException:
    print("Home link does not exist.\n")

# TEST CASE 3:POLICIES AND CODE -> POLICIES
try:
    driver.find_element_by_link_text('Policies and Code').click()
    time.sleep(2)
    driver.find_element_by_link_text('Policies').click()
    time.sleep(4)
    print('Successfully visited the Policies page of Policies and Code.\n')
except NoSuchElementException:
    print("Policies and Code / Policies page does not exist.\n")
    time.sleep(1)

# TEST CASE 4:PROGRAMS -> WORKSHOPS
try:
    driver.find_element_by_link_text('Programs').click()
    time.sleep(2)
    driver.find_element_by_link_text('Workshops').click()
    time.sleep(4)
    print('Successfully visited the the Workshops page of Programs.\n')
except NoSuchElementException:
    print("Programs / Workshops page does not exist.\n")
    time.sleep(1)

# TEST CASE 5:LINK -> AI IN EDUCATION
try:
    driver.find_element_by_link_text('LINKS').click()
    time.sleep(2)
    driver.find_element_by_link_text('AI in Education').click()
    time.sleep(4)
    print('Successfully visited the AI in Education page of LINKS.\n')
except NoSuchElementException:
    print("LINKS / AI in Education does not exist.\n")
    time.sleep(1)

# TEST CASE 6:JOIN US -> INTERNSHIP POSITIONS
try:
    driver.find_element_by_link_text('Join Us').click()
    time.sleep(2)
    driver.find_element_by_link_text('Internship Positions').click()
    time.sleep(4)
    print('Successfully visited the Internship Positions page of Join Us.\n')
except NoSuchElementException:
    print("Join Us / Internship Positions page does not exist.\n")
    time.sleep(1)


# TEST CASE 7:SCROLL TO TOP BUTTON
try:
    driver.find_element_by_id("toTopHover").click()
    print('Scroll to top button is functioning properly.\n')
    time.sleep(2)
except NoSuchElementException:
    print("Scroll to top button does not function properly.\n")
    time.sleep(1)

# TEST CASE 8: 6th SLIDE OF THE CAROUSEL

try:
    driver.find_element_by_link_text('6').click()
    time.sleep(4)
    print('Successfully visited the the 6th slide of the carousel.\n')
except NoSuchElementException:
    print("6th slide of the carousel does not exist.\n")
    time.sleep(1)

# TEST CASE 9:RESUME WRITING
try:
    driver.find_element_by_link_text('Resume Writing').click()
    print('Successfully visited the Resume Writing page.\n')
    time.sleep(4)
except NoSuchElementException:
    print('Resume Writing page does not exist.\n')
    time.sleep(1)

# TEST CASE 10:CONTACT US
try:
    driver.find_element_by_link_text('Contact Us').click()
    time.sleep(4)
    print('Successfully visited the Contact Us page.\n')
except NoSuchElementException:
    print("Contact us page does not exist.\n")
    time.sleep(1)

# TEST CASE 11: STUDENT SCHOLARSHIP PROGRAM
try:
    driver.find_element_by_link_text('Student Scholarship Program').click()
    print('Successfully visited the Student Scholarship Program page.\n')
    time.sleep(4)
except NoSuchElementException:
    print('Student Scholarship Program page does not exist.\n')
