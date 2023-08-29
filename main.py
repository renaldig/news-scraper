import requests
import time
from bs4 import BeautifulSoup
from scraper import scrape_news
from summarizer import get_summary
from emailer import send_email
import os

# Customize these variables according to your details
SENDER_EMAIL = '<ENTER_YAHOO_EMAIL_HERE>'
SENDER_PASSWORD = '<ENTER_SENDER_APP_PASSWORD>'
RECEIVER_EMAIL = '<ENTER_EMAIL_HERE>'
SUBJECT = 'Daily News Digest'

def main():
    print("Now started")
    while True:
        news_list = scrape_news()
        for news in news_list:
            link = news['link']
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Customize this part based on the structure of the news website
            text = ' '.join([p.text for p in soup.find_all('p')])

            try:
                summary = get_summary(text)
                news['summary'] = summary if summary else text[:200] + '...'
            except ValueError:
                news['summary'] = text[:200] + '...'

        message = ''
        for news in news_list:
            message += f"Title: {news['title']}\n"
            message += f"Summary: {news['summary']}\n"
            message += f"Link: {news['link']}\n\n"

        if message:
            send_email(SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL, SUBJECT, message)
            print('Email sent successfully!')
        else:
            print("Message is empty")

        time.sleep(86400)  # wait for 24 hours

if __name__ == '__main__':
    main()
