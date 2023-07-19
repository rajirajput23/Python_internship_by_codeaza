import time
from selenium import webdriver

# Set up Selenium WebDriver
driver = webdriver.Chrome('C:/Users/ZOHAIB/Documents/selenium p/chromedriver.exe')  # Make sure you have ChromeDriver installed and provide the path

# Open the group page
group_url = 'https://www.facebook.com/groups/423577148047130/'  #  the actual group URL
driver.get(group_url)

# Wait for the page to load
time.sleep(5)

# Scroll to load more members (modify the number of scrolls as per your requirement)
scrolls = 5
for _ in range(scrolls):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)

# Find all member profile links
member_links = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div[3]/div/div')

# Extract member data
data = []
for link in member_links:
    member_data = {
        'Full Name': 'N.A.',
        'Nick Name': 'N.A.',
        'DOB': 'N.A.',
        'Education': 'N.A.',
        'Marital status': 'N.A.',
        'Location/Region': 'N.A.',
        'Profile Image URL': 'N.A.',
        'Cover Image URL': 'N.A.',
        'Profile URL': link.get_attribute('href')
    }

    # Open member profile
    driver.get(link.get_attribute('href'))

    # Wait for the profile to load
    time.sleep(2)

    # Extract profile data
    member_data['Full Name'] = driver.find_element_by_xpath('//span[contains(text(), "Full Name")]/following-sibling::span').text
    member_data['Nick Name'] = driver.find_element_by_xpath('//span[contains(text(), "Nick Name")]/following-sibling::span').text
    member_data['DOB'] = driver.find_element_by_xpath('//span[contains(text(), "DOB")]/following-sibling::span').text
    member_data['Education'] = driver.find_element_by_xpath('//span[contains(text(), "Education")]/following-sibling::span').text
    member_data['Marital status'] = driver.find_element_by_xpath('//span[contains(text(), "Marital status")]/following-sibling::span').text
    member_data['Location/Region'] = driver.find_element_by_xpath('//span[contains(text(), "Location/Region")]/following-sibling::span').text
    member_data['Profile Image URL'] = driver.find_element_by_xpath('//img[@class="profile-image"]').get_attribute('src')
    member_data['Cover Image URL'] = driver.find_element_by_xpath('//img[@class="cover-image"]').get_attribute('src')

    # Add member data to the list
    data.append(member_data)

    # Go back to the group page
    driver.get(group_url)
    time.sleep(2)

# Print the extracted data
for member in data:
    print(member)

# Close the browser
driver.quit()
