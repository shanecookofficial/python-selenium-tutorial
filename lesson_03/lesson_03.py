from selenium import webdriver # Import the Selenium WebDriver module to automate browser actions.
import time # This import is so we can delay the termination of the browser so you can view the driver session start in action.

driver = webdriver.Chrome() # Create a new Chrome browser session using the Chrome WebDriver.

time.sleep(5) # These sleep lines are purely for demonstration purposes only so you can easily follow along through each part of the script.

driver.get("https://www.selenium.dev/") # Navigate to https://www.selenium.dev/

time.sleep(5)

driver.get("https://www.selenium.dev/about/") # Navigate to a new url

time.sleep(5)

driver.back() # Go back to the first url

time.sleep(5)

driver.forward() # Go back to the about url

time.sleep(5)

driver.refresh() # Refresh the page

time.sleep(5)

driver.quit() # A best practice is to always dispose of your driver sessions after your code is finished to prevent potential memory leak.