from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Music:
    def __init__(self):
        # Update the path to your ChromeDriver location
        service = Service('C:/webdrivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    def play(self, query):
        self.query = query
        self.driver.get(url=f"https://www.youtube.com/results?search_query={query}")

        try:
            # Wait for the first video to load
            video = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//ytd-video-renderer[1]//a[@id="thumbnail"]'))
            )
            video.click()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Optional: Keep the browser open
            input("Press Enter to close the browser...")
            self.driver.quit()

# Main execution

