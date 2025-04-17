from instagrapi import Client
from instagrapi.exceptions import ClientError

def post_to_instagram(title, excerpt, image, link, username, password):
    """
    Post a photo to Instagram with a caption composed of title, excerpt, and link.
    
    Args:
        title (str): Blog post title
        excerpt (str): Blog post excerpt
        image (str): Path to the image file (e.g., 'featured_image.jpg')
        link (str): URL to the blog post
        username (str): Instagram username
        password (str): Instagram password
    
    Returns:
        bool: True if successful, False if failed
    """
    caption = f"{title}\n{excerpt}\nRead more: {link}"
    cl = Client()
    
    try:
        cl.login(username, password)
        cl.photo_upload(image, caption)
        print("Successfully posted to Instagram!")
        return True
    
    except ClientError as e:
        print(f"Error: {str(e)}")
        return False
    
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False
    
    finally:
        cl.logout()

# Example usage (remove or modify this part when integrating)
# if __name__ == "__main__":
#     title = "My Awesome Blog Post"
#     excerpt = "A short summary of my thoughts today."
#     image = "featured_image.jpg"
#     link = "https://yourblog.com/my-post"
#     username = "dexteritycoder"
#     password = "smg313hu"
    
#     if post_to_instagram(title, excerpt, image, link, username, password):
#         print("Post went live!")
#     else:
#         print("Post failed.")