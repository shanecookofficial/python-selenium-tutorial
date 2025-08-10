<html>
    <main>
        <h1>Lesson 04: Interacting with Website Elements</h1>
        <h2>What is a Website Element?</h2>
        <p>
            A website element is any individual part of a web page such as a heading, a block of text, an image, or a button. 
            These elements are the building blocks that, together, create the entire website.
        </p>
        <p>
            As one definition puts it: 
            "An element is a part of a webpage. In XML and HTML, an element may contain a data item or a chunk of text or an image, or perhaps nothing. 
            A typical element includes an opening tag with some attributes, enclosed text content, and a closing tag."
            <sub><a href="#source-1">1</a></sub>
        </p>
        <h2>How do we Locate a Website Element?</h2>
        <p>
            To interact with an element on a page, we first need to tell Selenium exactly where to find it. 
            Selenium offers several different ways of identifying elements in the page’s HTML.
        </p>
        <h3>By.ID</h3>
        <p>
            "In general, if HTML IDs are available, unique, and consistently predictable, they are the preferred method for locating an element on a page. They tend to work very quickly, and forego much processing that comes with complicated DOM traversals."<sub><a href="#source-2">2</a></sub><br><br>
            Ex.
<pre><code>
from selenium import webdriver
from selenium.webdriver.common.by import By<br>
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/locators_tests/locators.html")
element = driver.find_element(By.ID, "lname")
</code></pre>
        </p>
        <h3>By.CSS_SELECTOR</h3>
        <p>
            "If unique IDs are unavailable, a well-written CSS selector is the preferred method of locating an element."<sub><a href="#source-2">2</a></sub><br><br>
            Ex.
<pre><code>
from selenium import webdriver
from selenium.webdriver.common.by import By<br>
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/locators_tests/locators.html")
element = driver.find_element(By.CSS_SELECTOR, "#fname")
</code></pre>
        </p>
        <h3>By.XPATH</h3>
        <p>
            "XPath works as well as CSS selectors, but the syntax is complicated and frequently difficult to debug. Though XPath selectors are very flexible, they are typically not performance tested by browser vendors and tend to be quite slow."<sub><a href="#source-2">2</a></sub><br><br>
            Ex.
<pre><code>
from selenium import webdriver
from selenium.webdriver.common.by import By<br>
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/locators_tests/locators.html")
element = driver.find_element(By.XPATH, "//input[@value='f']")
</code></pre>
        </p>
        <h3>Other Supported Strategies</h3>
        <p>
            Selenium offers the following additional strategies for locating elements:
        </p>
            <ul>
                <li>
                    By.NAME
                </li>
                <li>
                    By.LINK_TEXT
                </li>
                <li>
                    By.PARTIAL_LINK_TEXT
                </li>
                <li>
                    By.TAG_NAME
                </li>
                <li>
                    By.CLASS_NAME
                </li>
            </ul>
        <p>
        "Selection strategies based on linkText and partialLinkText have drawbacks in that they only work on link elements. Additionally, they call down to <a href="https://www.w3.org/TR/webdriver/#link-text">querySelectorAll</a> selectors internally in WebDriver.<br><br>
        Tag name can be a dangerous way to locate elements. There are frequently multiple elements of the same tag present on the page. This is mostly useful when calling the findElements(By) method which returns a collection of elements.
        <br><br>
        The recommendation is to keep your locators as compact and readable as possible. Asking WebDriver to traverse the DOM structure is an expensive operation, and the more you can narrow the scope of your search, the better."<sub><a href="#source-2">2</a></sub>
        </p>
        <h2>How can I interact with a Website Element?</h2>
        <h3>.click()</h3>
        <p>
            "The <a href="https://w3c.github.io/webdriver/#dfn-element-click">element click command</a> is executed on the <a href="https://w3c.github.io/webdriver/#dfn-center-point">center of the element</a>. If the center of the element is <a href="https://w3c.github.io/webdriver/#dfn-obscuring">obscured</a> for some reason, Selenium will return an <a href="https://w3c.github.io/webdriver/#dfn-element-click-intercepted">element click intercepted</a> error."<sub><a href="#source-3">3</a></sub><br><br>
            Ex.
<pre><code>
from selenium import webdriver
from selenium.webdriver.common.by import By<br>
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

check_input = driver.find_element(By.NAME, "checkbox_input")
check_input.click()
</code></pre>
        </p>
        <h3>.send_keys()</h3>
        <p>
            "The <a href="https://w3c.github.io/webdriver/#dfn-element-send-keys">element send keys command</a> types the provided keys into an <a href="https://w3c.github.io/webdriver/#dfn-editable">editable</a> element. Typically, this means an element is an input element of a form with a text type or an element with a content-editable attribute. If it is not editable, <a href="https://w3c.github.io/webdriver/#dfn-invalid-element-state">an invalid element state</a> error is returned.<br><br>
            <a href="https://www.w3.org/TR/webdriver/#keyboard-actions">Here</a> is the list of possible keystrokes that WebDriver Supports."<sub><a href="#source-3">3</a></sub><br><br>
            Ex.
<pre><code>
from selenium import webdriver
from selenium.webdriver.common.by import By<br>
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

email_input = driver.find_element(By.NAME, "email_input")

email = "admin@localhost.dev"
email_input.send_keys(email)
</code></pre>
</p>
        <h3>.clear()</h3>
        <p>
            "The <a href="https://w3c.github.io/webdriver/#dfn-element-clear">element clear command</a> resets the content of an element. This requires an element to be <a href="https://w3c.github.io/webdriver/#dfn-editable">editable</a>, and <a href="https://w3c.github.io/webdriver/#dfn-resettable-elements">resettable</a>. Typically, this means an element is an input element of a form with a <code>text</code> type or an element with a <code>content-editable</code> attribute. If these conditions are not met, <a href="https://w3c.github.io/webdriver/#dfn-invalid-element-state">an invalid element state</a> error is returned."<sub><a href="#source-3">3</a></sub><br><br>
            Ex.
<pre><code>
from selenium import webdriver
from selenium.webdriver.common.by import By<br>
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

email_input = driver.find_element(By.NAME, "email_input")
email_input.clear()

email = "admin@localhost.dev"
email_input.send_keys(email)
</code></pre>
        </p>
        <h3>Select()</h3>
        <p>
            "Select lists have special behaviors compared to other elements.
            The Select object will now give you a series of commands that allow you to interact with a <code>select</code> element...Note that this class only works for HTML elements select and option. It is possible to design drop-downs with JavaScript overlays using div or li, and this class will not work for those."<sub><a href="#source-4">4</a></sub><br><br>
            Ex.
<pre><code>
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/selectPage.html")

"""Locate the drop-down element"""
select_element = driver.find_element(By.NAME, "selectomatic")

"""Create a Select object"""
dropdown = Select(select_element)

"""Select by visible text"""
dropdown.select_by_visible_text("Four")

"""Select by value"""
dropdown.select_by_value("two")

"""Select by index (0-based)"""
dropdown.select_by_index(3)

"""Get all available options"""
for option in dropdown.options:
    print(option.text)

driver.quit()
</code></pre>
</p>
        <p>
            Please execute the code found in <code>lesson_04.py</code> to see how
            you can perform different actions on web elements.
        </p>
        <div id="Sources">
            <h2>Sources</h2>
            <p id="source-1">
                1. MDN Web Docs. (2025, July 11). <em>Element | Glossary.</em> <a href="https://developer.mozilla.org/en-US/docs/Glossary/Element#:~:text=An%20element%20is%20a%20part%20of%20a%20webpage.%20In%20XML%20and%20HTML%2C%20an%20element%20may%20contain%20a%20data%20item%20or%20a%20chunk%20of%20text%20or%20an%20image%2C%20or%20perhaps%20nothing.%20A%20typical%20element%20includes%20an%20opening%20tag%20with%20some%20attributes%2C%20enclosed%20text%20content%2C%20and%20a%20closing%20tag.">https://developer.mozilla.org/en-US/docs/Glossary/Element</a>
            </p>
            <p id="source-2">
                2. Selenium. (n.d.). <em>Tips on working with locators | Selenium.</em> <a href="https://www.selenium.dev/documentation/test_practices/encouraged/locators/#:~:text=Tips%20on%20working,search%2C%20the%20better.">https://www.selenium.dev/documentation/test_practices/encouraged/locators/</a>
            </p>
            <p id="source-3">
                3. Selenium. (2025, July 29). <em>Interacting with web elements | Selenium.</em> <a href="https://www.selenium.dev/documentation/webdriver/elements/interactions/">https://www.selenium.dev/documentation/webdriver/elements/interactions/</a>
            </p>
            <p id="source-4">
                4. Selenium. (n.d.). <em>Working with select list elements | Selenium.</em> <a href="https://www.selenium.dev/documentation/webdriver/support_features/select_lists/#:~:text=The%20Select%20object,work%20for%20those.">https://www.selenium.dev/documentation/webdriver/support_features/select_lists/</a>
            </p>
        </div>
    </main>
</html>