from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# function to go to the weather website
def open_weather_website() -> None:
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.meteoblue.com/en/weather/week/helsinki_finland_658225')
    time.sleep(5)  # Wait for the page to load completely
    
    return driver


# function to get weather details from HTML element
def get_weather_description(driver) -> str | None:
    try:
        description_element = driver.find_element(By.XPATH, "//*[@id='tab_wrapper']/div[2]/div/div[5]/p")
        return description_element.text
    except Exception as e:
        print(f"Error extracting weather description: {e}")
        return None
