from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def post_to_x(title, excerpt, image, link, username, password):
    """
    Post to X using Selenium automation with username and password.
    
    Args:
        title (str): Blog post title
        excerpt (str): Blog post excerpt
        image (str): Path to image file (e.g., 'featured_image.jpg'), or None
        link (str): URL to the blog post
        username (str): X username
        password (str): X password
    
    Returns:
        bool: True if successful, False if failed
    """
    text = f"{title}\n{excerpt}\n{link}"
    
    try:
        # Set up Chrome with options
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)  # Add service=Service("/path/to/chromedriver") if needed
        
        # Open X login page
        driver.get("https://x.com/login")
        wait = WebDriverWait(driver, 15)
        
        # Enter username
        print("Entering username...")
        username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']")))
        username_field.send_keys(username)
        time.sleep(1)
        username_field.send_keys(Keys.RETURN)
        
        # Enter password
        print("Entering password...")
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        password_field.send_keys(password)
        time.sleep(1)
        password_field.send_keys(Keys.RETURN)
        
        # Wait for compose button
        print("Waiting for compose button...")
        tweet_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/compose/post']")))
        tweet_button.click()
        
        # Enter tweet text
        print("Typing tweet...")
        tweet_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetTextarea_0']")))
        tweet_box.send_keys(text)
        time.sleep(1)
        
        # Upload image if provided
        if image:
            print("Uploading image...")
            # Convert to absolute path
            absolute_image_path = os.path.abspath(image)
            if not os.path.exists(absolute_image_path):
                raise FileNotFoundError(f"Image file not found at {absolute_image_path}")
            image_input = driver.find_element(By.XPATH, "//input[@type='file']")
            image_input.send_keys(absolute_image_path)
            time.sleep(3)  # Wait for upload
        
        # Post the tweet
        print("Posting tweet...")
        post_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='tweetButton']")))
        post_button.click()
        
        # Wait to confirm posting
        time.sleep(3)
        print(f"Successfully posted to X for {username}!")
        return True
    
    except Exception as e:
        print(f"Error posting to X: {str(e)}")
        return False
    
    finally:
        driver.quit()

# Example usage
if __name__ == "__main__":
    title = "My Awesome Blog Post"
    excerpt = "A short summary of my thoughts today."
    image = "featured_image.jpg"  # Ensure this file exists in your script's directory
    link = "https://yourblog.com/my-post"
    username = "username"
    password = "password"
    
    if post_to_x(title, excerpt, image, link, username, password):
        print("Tweet went live!")
    else:
        print("Tweet failed.")