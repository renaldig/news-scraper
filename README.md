# Automated Daily News Digest

## Description
In this age of information overload, it's challenging to keep up with all the news that's important to us. This application aims to solve this problem by creating an automated daily news digest. The application will scrape news from a website, summarize them, and then send a daily digest email to the user.

## Features
1. News Scraping: The application will scrape news articles from a website.
2. News Summarization: The application will then summarize these news articles using NLP techniques.
3. Daily Digest Email: The application will send a daily digest email to the user with the summarized news articles.

## Technologies and Libraries
1. Python
2. BeautifulSoup
3. Gensim
4. SMTP library

## How to use
1. Clone the repository.
2. Install the required libraries by running `pip install -r requirements.txt`.
3. Customize the variables in `main.py` file.
4. Run the `main.py` file.
5. The application will scrape the news articles, summarize them, and then send a daily digest email to the specified email address.

## Note
The `scraper.py` and `main.py` files need to be customized based on the structure of the news website you want to scrape.
