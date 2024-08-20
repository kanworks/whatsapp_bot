from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    # Set up the WebDriver
    driver = webdriver.Chrome()  # Make sure ChromeDriver is in your PATH

    try:
        # Navigate to a website
        driver.get("https://www.google.com")

        # Find and interact with elements
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium Python tutorial")
        search_box.send_keys(Keys.RETURN)

        # Wait for search results
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )

        # Print the title of the first search result
        first_result = driver.find_element(By.CSS_SELECTOR, "h3")
        print("First result:", first_result.text)

        # Demonstrate other Selenium features
        # Find multiple elements
        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        print(f"Number of results found: {len(results)}")

        # Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for scroll to complete

        # Go back to the previous page
        driver.back()
        time.sleep(2)  # Wait for page to load

        # Refresh the page
        driver.refresh()
        time.sleep(2)  # Wait for page to reload

        # Handle an alert (Note: Google doesn't typically show alerts, so this is just for demonstration)
        try:
            driver.execute_script("alert('This is a test alert');")
            alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
            print("Alert text:", alert.text)
            alert.accept()
        except:
            print("No alert found")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
