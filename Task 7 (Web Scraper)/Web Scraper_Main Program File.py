from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv
import os

# === Configuration ===
URL = "https://www.bbc.com/news/topics/crem2zr2vmqt"
CHROME_DRIVER_PATH = os.path.join(os.getcwd(), "chromedriver.exe")  # Same folder

# === Set up Selenium options ===
options = Options()
options.add_argument("--headless")  # Optional: comment this out to see the browser
options.add_argument("--disable-gpu")
options.add_argument("--log-level=3")  # Suppress logs

# === Start WebDriver ===
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# === Open the page ===
driver.get(URL)
time.sleep(5)  # Wait for JavaScript content to load (adjust if needed)

# === Get page source & parse with BeautifulSoup ===
soup = BeautifulSoup(driver.page_source, "html.parser")

# === Find all <h2> tags ===
headlines = soup.find_all("h2")

# === Write to CSV ===
with open("data.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["No.", "Headline"])  # CSV Header
    for i, tag in enumerate(headlines, 1):
        text = tag.get_text(strip=True)
        if text:
            writer.writerow([i, text])

# === Cleanup ===
driver.quit()
print("✅ Headlines saved successfully to 'data.csv'")
