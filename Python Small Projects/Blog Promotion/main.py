import requests
import Instagram_Promotion
import Twitter_Promotion

# Fetch latest post from WordPress
url = "https://dexteritycoder.com/wp-json/wp/v2/posts?per_page=1"
response = requests.get(url)
post = response.json()[0]

# Extract details
title = post["title"]["rendered"]
excerpt = post["excerpt"]["rendered"].replace("<p>", "").replace("</p>", "")
link = post["link"]
image_url = post["featured_media"]  # You'll need to fetch the image URL separately

# Fetch image URL (example, depends on your setup)
media_response = requests.get(f"https://dexteritycoder.com/wp-json/wp/v2/media/{image_url}")
image = media_response.json()["source_url"]

# Download image
image_data = requests.get(image).content
with open("featured_image.jpg", "wb") as f:
    f.write(image_data)

# Now you’d write functions to post to each platform...
print(f"Title: {title}\nExcerpt: {excerpt}\nLink: {link}\nImage saved!")
# print(type(image_data))

Image = "F:/Python Small Projects/featured_image.jpg"
# post_to_instagram(title, excerpt, image, link, username, password)
Instagram_Promotion.post_to_instagram(title, excerpt, Image, link, "dexteritycoder", "smg313hu")

# post_to_x(title, excerpt, image, link, username, password)
Twitter_Promotion.post_to_x(title, excerpt, Image, link, "dexteritycoder", "smg313hu")