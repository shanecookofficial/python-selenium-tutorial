from selenium import webdriver # Import the Selenium WebDriver module to automate browser actions.
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time # This import is so we can delay the termination of the browser so you can view the driver session start in action.

driver = webdriver.Chrome() # Create a new Chrome browser session using the Chrome WebDriver.

time.sleep(5) # These sleep lines are purely for demonstration purposes only so you can easily follow along through each part of the script.

driver.get("https://todomvc.com/examples/react/dist/")

time.sleep(5)

# Start creating a todo item
todo = "Walk the cat."
todo_input = driver.find_element(By.ID, "todo-input")
todo_input.send_keys(todo)
time.sleep(5)

# Edit the todo item
todo_input.clear()
time.sleep(2)
new_todo = "Walk the dog."
todo_input.send_keys(new_todo)
time.sleep(2)

# Finish creating the todo item
todo_input.send_keys(Keys.ENTER)
time.sleep(5)

driver.quit() # A best practice is to always dispose of your driver sessions after your code is finished to prevent potential memory leak.