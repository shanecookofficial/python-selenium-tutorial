<html>
    <main>
        <h1>Lesson 03 - Website Navigation</h1>
        <p>
            Now that our "car" (the browser) is running, it’s time to decide where to drive it. 
            In Selenium, that means navigating to a specific website.
        </p>
        <h2>How to Navigate to a Website?</h2>
        <p>
            The first thing you’ll usually want to do after launching your browser is open a web page. 
            In Selenium, this is done with the <code>get()</code> method, which takes the website’s URL in a string as an argument.<br><br>Ex.
        </p>
        <code>
            driver.get("http://selenium.dev")
        </code><br><br>
        <p>
            This command tells your browser to go directly to the given address, just like typing the URL into the address bar and pressing Enter.
        </p>
        <h2>Browser Navigation Controls</h2>
        <p>
            Selenium can also mimic your browser’s navigation buttons:
        </p>
        <h3>Back</h3>
        <code>
            driver.back()
        </code><br><br>
        <p>
            Moves one step back in the browser’s history, like clicking the back button.
        </p>
        <h3>Forward</h3>
        <code>
            driver.forward()
        </code><br><br>
        <p>
            Moves forward in the browser’s history if you’ve gone back, like clicking the forward button.
        </p>
        <h3>Refresh</h3>
        <code>
            driver.refresh()
        </code><br><br>
        <p>
            Reloads the current page, just like pressing your browser’s refresh button.
        </p>
        <p>
            Please execute the code found in <code>lesson_03.py</code> to see how
            you can navigate to different websites
            and perform normal navigation actions on them.
        </p>
    </main>
</html>
