from selenium import webdriver # Import the Selenium WebDriver module to automate browser actions.
import time # This import is so we can delay the termination of the browser so you can view the driver session start in action.

driver = webdriver.Chrome() # Create a new Chrome browser session using the Chrome WebDriver.

time.sleep(5) # This line is purely for demonstration purposes only so you can view your browser opening up.

driver.quit() # A best practice is to always dispose of your driver sessions after your code is finished to prevent potential memory leak.