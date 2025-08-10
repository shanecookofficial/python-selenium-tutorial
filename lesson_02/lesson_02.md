<html>
    <main>
        <h1>Lesson 02 - Drivers</h1>
        <p>
            Before we begin writing code to automate the browser, we need to learn what a <strong><em>driver</em></strong> is.
        </p>
        <h2>What is a Driver?</h2>
        <p>
            In Selenium and other web automation tools, a <strong><em>driver</em></strong> 
            "drives a browser natively, as a user would, either locally or on a remote machine"
            <sub><a href="source-1">1</a></sub>.
            <br><br>
            Think of a driver like a person behind the wheel of a car, where the car represents the web browser. 
            Without a driver, most cars won’t go anywhere on their own. Likewise, a web browser needs a driver to carry out instructions.
            <br><br>
            As the "driver", you’ll write code that tells the browser what to do, just as shifting gears, pressing the accelerator, and steering guide a car to its destination.
        </p>
        <h2>What is a Driver Session?</h2>
        <p>
            Just like you need to start a car before driving it, a <strong>Driver Session</strong> begins when you launch a browser instance to be controlled by a WebDriver. 
            It’s the “ignition” that powers your automation, allowing the driver to send commands and the browser to respond.
        </p>
        <div>
            <p>
                To start a driver session, consider the following Python code:<br><br>
                <code>
                    from selenium import webdriver<br><br>
                    driver = webdriver.Chrome()
                </code><br><br>
                In the code:
            </p>
            <ul>
                <li>
                    <code>webdriver</code> is a module (specifically, selenium.webdriver) from the Selenium library.
                </li>
                <li>
                    <code>selenium</code> → the top-level Selenium package.
                </li>
                <li>
                    <code>webdriver.Chrome()</code> → a class constructor inside that module which creates a Chrome browser automation session.
                </li>
            </ul>
            <p>
                So when you write <code>driver = webdriver.Chrome()</code>, you’re telling Selenium:<br><br>
                “Use the Chrome driver class from the webdriver module to start a new Chrome browser that I can control through an object called 'driver'.”
            </p>
            <p>
                Lastly, it’s best practice to terminate your driver session once your code finishes running or if an error occurs.
                "If we do not use <code>quit()</code> at the end of the program, the WebDriver session will not be closed properly, and the files will not be cleared from memory. This may result in memory leak errors."<sub><a href="source-2">2</a></sub>
            </p>
            <p>
                Please execute the code found in <code>lesson_02.py</code> to see Drivers and Driver Sessions in action.
            </p>
        </div>
        <div id="Sources">
            <h2>Sources</h2>
            <p id="source-1">
                1. Selenium. (n.d.). <em>WebDriver | Selenium</em>. <a href="https://www.selenium.dev/documentation/webdriver/#:~:text=drives%20a%20browser%20natively%2C%20as%20a%20user%20would%2C%20either%20locally%20or%20on%20a%20remote%20machine">https://www.selenium.dev/documentation/webdriver/</a>
            </p>
            <p id="source-2">
                2. Zyxware. (2023, February 6). <em>What is close() and quit() commands in Selenium Webdriver? | Zyxware</em> <a href="https://www.zyxware.com/articles/5552/what-is-close-and-quit-commands-in-selenium-webdriver#:~:text=If%20we%20do%20not%20use%20quit()%20at%20the%20end%20of%20the%20program%2C%20the%20WebDriver%20session%20will%20not%20be%20closed%20properly%2C%20and%20the%20files%20will%20not%20be%20cleared%20off%20memory.%20This%20may%20result%20in%20memory%20leak%20errors.">https://www.zyxware.com/articles/5552/what-is-close-and-quit-commands-in-selenium-webdriver</a>
            </p>
        </div>
    </main>
</html>