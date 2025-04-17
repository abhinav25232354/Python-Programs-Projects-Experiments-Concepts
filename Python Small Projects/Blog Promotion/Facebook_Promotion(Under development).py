from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def post_to_facebook(title, excerpt, image, link, username, password):
    """
    Post to Facebook using Selenium automation with username and password.
    
    Args:
        title (str): Blog post title
        excerpt (str): Blog post excerpt
        image (str): Path to image file (e.g., 'featured_image.jpg'), or None
        link (str): URL to the blog post
        username (str): Facebook username (email/phone)
        password (str): Facebook password
    
    Returns:
        bool: True if successful, False if failed
    """
    text = f"{title}\n{excerpt}\n{link}"
    
    try:
        # Set up Chrome with options
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)  # Add service=Service("/path/to/chromedriver") if needed
        
        # Open Facebook login page
        driver.get("https://www.facebook.com/")
        wait = WebDriverWait(driver, 20)
        
        # Enter username
        print("Entering username...")
        username_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
        username_field.send_keys(username)
        time.sleep(2)
        
        # Enter password
        print("Entering password...")
        password_field = driver.find_element(By.ID, "pass")
        password_field.send_keys(password)
        time.sleep(2)
        password_field.send_keys(Keys.RETURN)
        
        # Handle CAPTCHA or login completion
        print("Checking for login completion...")
        try:
            # Wait for post box directly
            post_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='What’s on your mind,']")))
        except Exception:
            print("CAPTCHA or verification required. Please solve it manually in the browser.")
            # Wait longer for manual CAPTCHA solving (60 seconds)
            time.sleep(60)
            print("Retrying to find post box after CAPTCHA...")
            # Updated selector for post box (more specific)
            post_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='What’s on your mind,']")))
        
        print("Waiting for post box...")
        post_box.click()
        
        # Enter post text
        print("Typing post...")
        text_area = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='status-attachment-mentions-input']")))
        text_area.send_keys(text)
        time.sleep(2)
        
        # Upload image if provided
        if image:
            print("Uploading image...")
            absolute_image_path = os.path.abspath(image)
            if not os.path.exists(absolute_image_path):
                raise FileNotFoundError(f"Image file not found at {absolute_image_path}")
            image_input = driver.find_element(By.XPATH, "//input[@type='file']")
            image_input.send_keys(absolute_image_path)
            time.sleep(4)
        
        # Click the Post button
        print("Posting to Facebook...")
        post_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='react-composer-post-button']")))
        post_button.click()
        
        # Wait to confirm posting
        time.sleep(4)
        print(f"Successfully posted to Facebook for {username}!")
        return True
    
    except Exception as e:
        print(f"Error posting to Facebook: {str(e)}")
        return False
    
    finally:
        # Keep browser open briefly to verify
        time.sleep(5)
        driver.quit()

# Example usage
if __name__ == "__main__":
    title = "My Awesome Blog Post"
    excerpt = "A short summary of my thoughts today."
    image = "featured_image.jpg"  # Ensure this file exists, or set to None
    link = "https://yourblog.com/my-post"
    username = "8115437919"
    password = "25232354"
    
    if post_to_facebook(title, excerpt, image, link, username, password):
        print("Post went live!")
    else:
        print("Post failed.")