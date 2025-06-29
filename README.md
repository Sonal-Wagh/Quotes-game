#  Quote Guessing Game Web App (Streamlit)

This is a fun little web app where you read a quote and try to guess who said it. You get 4 tries, and helpful hints are given after each wrong guess.

The app also scrapes quotes from [quotes.toscrape.com](http://quotes.toscrape.com), saves them in an Excel file, and uses that data for the guessing game.

---

This project is completed in 3 simple steps:

### 1. **Scraping Quotes**
- Used Python and `BeautifulSoup` to scrape quotes from a website called `quotes.toscrape.com`.
- The scraper collected:
  - Quote text
  - Author name
  - Link to author's bio
- The code looped through **all pages** of the site (up to 10).
- The data was saved into a list of dictionaries.

### 2. **Saving to Excel**
- Used `pandas` to convert the scraped quotes into a table (DataFrame).
- Then  saved it into an Excel file called `quotes.xlsx` using `to_excel()`.

### 3. **Building the Guessing Game**
- A random quote is shown to the user.
- The user has to guess who said it in 4 tries.
- After each wrong guess, we show a hint:
  - Hint 1: Author’s birthdate and birthplace
  - Hint 2: First letter of the first name
  - Hint 3: First letter of the last name
- After 4 wrong attempts, the correct answer is revealed.
- uUed `Streamlit` to turn this into a web app.

---

##  Live Demo

Click below to try the app live:

 [Deployed App on Streamlit Cloud](https://quotes-guessing-game.streamlit.app/)

---


