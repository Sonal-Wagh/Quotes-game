import streamlit as st
import requests
from bs4 import BeautifulSoup
import random

@st.cache_data(show_spinner=False)
def scrape_all_quotes():
    base_url = "http://quotes.toscrape.com"
    all_quotes = []
    url = "/page/1"

    while url:
        res = requests.get(base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")

        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": base_url + quote.find("a")["href"]
            })

        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None

    return all_quotes

# --- UI Start ---
st.set_page_config(page_title="Quote Guessing Game", layout="centered")
st.title("🎯 Quote Guessing Game")
st.caption("Guess who said it. You have 4 tries and hints will help!")

# Load quotes
quotes = scrape_all_quotes()

# Set up session state
if "quote" not in st.session_state:
    st.session_state.quote = random.choice(quotes)
    st.session_state.guesses_left = 4
    st.session_state.finished = False

quote = st.session_state.quote
guesses_left = st.session_state.guesses_left

# Show quote
st.markdown(f"> 💬 **{quote['text']}**")

# Input from user
if not st.session_state.finished:
    guess = st.text_input(f"✍️ Who said this? ({guesses_left} guesses left)", key="guess_input")

    if st.button("Submit Guess"):
        if guess.lower().strip() == quote["author"].lower():
            st.success("🎉 Correct! You guessed it right!")
            st.session_state.finished = True
        else:
            st.session_state.guesses_left -= 1
            guesses_left = st.session_state.guesses_left

            # Show hints
            if guesses_left == 3:
                res = requests.get(quote["bio-link"])
                soup = BeautifulSoup(res.text, "html.parser")
                date = soup.find(class_="author-born-date").get_text()
                place = soup.find(class_="author-born-location").get_text()
                st.info(f"🧠 Hint: Born on {date} {place}")
            elif guesses_left == 2:
                st.info(f"🧠 Hint: First name starts with **{quote['author'][0]}**")
            elif guesses_left == 1:
                last_initial = quote["author"].split(" ")[-1][0]
                st.info(f"🧠 Hint: Last name starts with **{last_initial}**")
            elif guesses_left == 0:
                st.error(f"❌ Out of guesses! The answer was **{quote['author']}**")
                st.session_state.finished = True

# Play again button
if st.session_state.finished:
    if st.button("🔁 Play Again"):
        st.session_state.quote = random.choice(quotes)
        st.session_state.guesses_left = 4
        st.session_state.finished = False
        st.rerun()
