from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Making function with 6 parameters
def post_to_x(title, excerpt, image, link, username, password):
    try:
        # Setting up chrome with options
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        # You can change service = service if needed

        # Now opening X login page
        driver.get("https://x.com/login")
        wait = WebDriverWait(driver, 15)

        # Entering username field
        print("Entering username...")
        username_field = wait.until(EC.presence_of_element_located(By.XPATH, "//input[@name='text']"))
        username_field.send_keys(username)
        time.sleep(1)
        username_field.send_keys(Keys.RETURN)

        # Entering Password
        print("Entering Password...")
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        password_field.send_keys(password)
        time.sleep(1)
        password_field.send_keys(Keys.RETURN)

        # Wait for compose button for posting
        print("Waiting for compose button...")
        tweet_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/compose/post']")))
        tweet_button.click()

        # Entering Tweet text
        print("Typing tweet...")
        tweet_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetTextarea_0']")))
        tweet_box.send_keys(text)
        time.sleep(1)

        # Uploading image if provided
        if image:
            print("Uploading Image...")
            # Convert to absolute path
            absolute_image_path = os.path.abspath(image)
            if not os.path.exists(absolute_image_path):
                raise FileNotFoundError(f"Image file not found at {absolute_image_path}")
            image_input = driver.find_element(By.XPATH, "//input[@type='file']")
            image_input.send_keys(absolute_image_path)
            time.sleep(3) # Waiting time for upload

        # Now posting the tweet
        print("Posting Tweet...")
        post_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='tweetbutton']")))
        post_button.click()

        # Waiting for confirmation of posting from X backend
        time.sleep(3)
        print(f"Successfully posted to X for {username}")
        return True
    except Exception as e:
        print(f"Error Posting to X: {str(e)}")
        return False
    finally:
        driver.quit()

# Now its time to use the function
# Here is how you can use this function
if __name__ == "__main__":
    title = "Title as per your need"
    excerpt = "A short description for the post"
    image = "Path to your image, e.g., "c:/hello/"
    link = "Paste your link if you have one"
    username = "Username"
    password = "password"

    if post_to_x(title, excerpt, image, link, username, password):
        print("Tweet Posted Successfully")
        print("Tweet went live!")
    else:
        print("Tweet Failed.")

# If your post is not posted at first time don't think program is incorrect, you can 
# try once again and then you will find your post is posted successfully
# Sometimes X recognize it as Bot response that is why.