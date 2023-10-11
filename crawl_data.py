import random
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Create an instance of the WebDriver
options = webdriver.ChromeOptions()
# Add experimental for devtools
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# Open driver full display
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Set the number of pages and images per page
num_pages = 100
images_per_page = 60

# Iterate over the pages
for page in range(1, num_pages + 1):
    # Construct the URL for each page
    url = f"https://www.istockphoto.com/vi/search/2/image?page={page}&phrase=dog%20and%20cat%20together"

    # Navigate to the page
    driver.get(url)

    sleep(random.randint(5, 10))

    # Iterate over the image elements and retrieve the source URLs of the images
    for i in range(1, images_per_page + 1):
        image_elements = driver.find_element(By.XPATH, f"/html/body/div[2]/section/div/main/div/div/div[2]/div[2]/div[3]/div[1]/article/a")
        image_elements.click()

        sleep(random.randint(2, 3))

#         img_url = element.get_attribute('src')

#         # Download the image
# urllib.request.urlretrieve(img_url, f"D:\Project1\PreprocessingData\train\Dog&Catimage\dog&cat_{page}_{i+1}.jpg")

# # Close the WebDriver
# driver.quit()
