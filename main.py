from selenium_module import open_weather_website, get_weather_description
from pyautogui_module import allow_consent
from image_generation import generate_image

def main():
    # Open the weather website
    driver = open_weather_website() 
    allow_consent()
     
    # getting weather from website
    weather_description = get_weather_description(driver)
    print("Weather Description:", weather_description)
    
    # passing prompt to ai API 
    generate_image(weather_description)

    driver.quit()  # Close the browser when done



if __name__ == "__main__":
    main()
