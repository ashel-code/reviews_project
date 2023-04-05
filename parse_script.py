import time
import os.path
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import comments
from analysis import run_analysis



class Setup:
    @staticmethod
    def create_soup(file_path):     # create Beautiful Soup object
        with open(file_path, 'r', encoding="utf-8") as file:
            source = file.read()
        file.close()
        new_soup = BeautifulSoup(source, 'lxml')
        return new_soup

    @staticmethod
    def get_source_html(url):       # get source code of the page
        web_driver = webdriver.Safari()
        web_driver.get(url=url)
        time.sleep(10)

        # Get scroll height
        last_height = web_driver.execute_script("return document.body.scrollHeight")
        new_height = 0
        while True:
            # Scroll down to bottom

            for i in range(3):
                web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)
                new_height = web_driver.execute_script("return document.body.scrollHeight")
                if new_height != last_height:
                    break
                print(last_height, new_height)
                web_driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)

            if new_height == last_height:
                break
            last_height = new_height
        html = web_driver.page_source
        with open('page-source.html', 'w', encoding="utf-8") as file:
            file.write(html)
        file.close()
        web_driver.quit()


class Prints:
    @staticmethod
    def print_reviews(all_reviews):  # print all reviews
        for i, review in enumerate(all_reviews):
            print(i + 1, review.text)

    @staticmethod
    def print_dates(dates):  # print all dates
        for i, date in enumerate(dates):
            print(i + 1, date.text)

    @staticmethod
    def print_all(all_reviews, all_dates, all_ratings, all_names):  # print everything
        for i in range(len(all_ratings)):
            print('~' + str(i + 1), " - ", all_names[i].text, " - ", all_dates[i].text,
                  " - ", all_ratings[i], " - ", all_reviews[i].text)


def get_reviews(new_soup):     # parse reviews
    all_reviews = new_soup.find_all('span', 'business-review-view__body-text')
    return all_reviews


def get_average_rating(new_soup):     # parse average rating
    average_rating = new_soup.find_all('span', 'business-summary-rating-badge-view__rating-text')
    return average_rating


def get_dates(new_soup):     # parse review`s dates
    dates = new_soup.find_all('span', 'business-review-view__date')
    return dates


def get_title(new_soup):    # parse title of the restaurant
    title = new_soup.find_all('h1', class_="card-title-view__title")
    return title[0].text


def get_names(new_soup):    # parse user names
    all_names = new_soup.find_all('div', class_="business-review-view__author")
    fixed_names = []
    for name in all_names:
        fixed_names.append(name.find_next('a'))
    return fixed_names


def get_ratings(new_soup):    # parse review`s ratings
    items = new_soup.find_all('div', class_="business-rating-badge-view__stars")[1:]
    rates = []
    for item in items:
        temp = item.find_all_next('span', class_='inline-image _loaded business-rating-badge-view__star _full _size_m')
        rates.append(len(temp))
    fixed_rates = []
    for i in range(1, len(rates)):
        fixed_rates.append(abs(rates[i] - rates[i - 1]))
    fixed_rates.append(rates[-1])
    return fixed_rates


def parse(URL, FILE_PATH):
    if os.path.exists(FILE_PATH) is False:
        Setup.get_source_html(URL)
    soup = Setup.create_soup(FILE_PATH)

    reviews = get_reviews(soup)
    total_mark = get_average_rating(soup)
    review_dates = get_dates(soup)
    rating = get_ratings(soup)
    names = get_names(soup)

    print("Title -", get_title(soup))
    print("Rating -", total_mark[0].text + "." + total_mark[2].text)
    print("-------------------------------------------------------------------------")
    # Prints.print_all(reviews, review_dates, rating, names)

    comments_list = comments.parseLists(rating, names, reviews, review_dates)

    comments.parseLists(rating, names, reviews, review_dates)
#   for i in range(len(all_ratings)):
#             print('~' + str(i + 1), " - ", all_names[i].text, " - ", all_dates[i].text,
#                   " - ", all_ratings[i], " - ", all_reviews[i].text)

    run_analysis(comments_list)

    
