# 📰 Web Scraper

This project is a simple **web scraping tool** that extracts the latest headlines from a BBC News topic page using **Selenium** and **BeautifulSoup**, and saves them into a CSV file.

---

## 📌 Features

- Scrapes dynamic JavaScript-loaded content using Selenium
- Extracts `<h2>` headlines from BBC News
- Saves data to a clean CSV file
- Headless browser operation (runs in the background)

---

## 🛠️ Requirements

- Python 3.7+
- Google Chrome (version 138.x)
- ChromeDriver (version 138.0.7204.159)

---

## 📦 Install Dependencies

Open terminal and run:

```bash
pip install selenium beautifulsoup4
```

---

### 📂 Folder Structure

bbc-news-web-scraper/<br>
│
├── chromedriver.exe                      # ChromeDriver executable (v138)<br>
├── data.csv                              # Output file with scraped headlines<br>
├── LICENSE.chromedriver                  # Optional license file<br>
├── THIRD_PARTY_NOTICES.chromedriver      # Optional notices file<br>
├── Web Scraper_Main Program File.py      # Main Python script<br>
|── README.md                             # README file<br>
├── LICENSE                               # LICENSE file

---

## 🚀 How to Run
- Make sure chromedriver.exe is in the same folder as the Python script.

- Run the script using:
  - python "Web Scraper_Main Program File.py"

-It will create/update a file called data.csv with the latest scraped headlines.

---

## 📤 Output: data.csv
- No.	    Headline
- 1	      Sunak unveils new NHS policies
- 2	      Ukraine conflict latest updates
- ...	    ...

---

## ⚙️ Customization

- To see the browser in action, comment out this line in the script:
  - options.add_argument("--headless")

- You can change the URL by updating:
  - URL = "https://www.bbc.com/news/topics/crem2zr2vmqt"

---

## 📄 License
- This project is for educational use. chromedriver.exe is licensed under the ChromeDriver License.

---

### 🙋‍♂️ Author
**CHANDRUPATLA SAI VARUN**
Developed as part of **Techno Hacks Internship** Program

---
