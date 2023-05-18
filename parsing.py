import time
import os.path
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from structure import comments
from db_actions import DatabaseActions


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
        options = Options()
        options.headless = False
        web_driver = webdriver.Chrome(executable_path='chromedriver', options=options)
        web_driver.get(url=url)
        time.sleep(14)
        reviews_amount_element = web_driver.find_element(By.CSS_SELECTOR, 'h2')
        reviews_amount = int(reviews_amount_element.text.split()[0])
        temp_amount = 0
        while temp_amount != reviews_amount:
            a = web_driver.find_element(By.CLASS_NAME, 'card-reviews-view__actions-button')
            web_driver.execute_script("arguments[0].scrollIntoView();", a)
            WebDriverWait(web_driver, 120000).until(
                ec.presence_of_element_located((By.CLASS_NAME, 'business-review-view__body-text'))
            )
            temp_amount = len(web_driver.find_elements(By.CLASS_NAME, 'business-review-view__body-text'))
            time.sleep(0.5)
            print(temp_amount)

        html = web_driver.page_source
        with open('page-source.html', 'w', encoding="utf-8") as file:
            file.write(html)
        file.close()
        web_driver.quit()


def print_all(all_reviews, all_dates, all_ratings, all_names):  # print everything
    for i in range(len(all_ratings)):
        print('~' + str(i + 1), " - ", all_names[i], " - ", all_dates[i],
              " - ", all_ratings[i], " - ", all_reviews[i])


def get_reviews(new_soup):     # parse reviews
    all_reviews = new_soup.find_all('span', 'business-review-view__body-text')
    result = []
    for i in all_reviews:
        elem = i.text.replace('"', ' ')
        elem.replace("'", ' ')
        result.append(elem)
    return result


def get_average_rating(new_soup):     # parse average rating
    average_rating = new_soup.find_all('span', 'business-summary-rating-badge-view__rating-text')
    return average_rating


def convert_dates(dates):
    month = {
        'января': 1,
        'февраля': 2,
        'марта': 3,
        'апреля': 4,
        'мая': 5,
        'июня': 6,
        'июля': 7,
        'августа': 8,
        'сентября': 9,
        'октября': 10,
        'ноября': 11,
        'декабря': 12,
    }
    new_dates = []
    for d in dates:
        date = d.split()
        new_date = date[0] + '-' + str(month.get(date[1])) + '-' + date[2]
        new_dates.append(new_date)
    return new_dates


def get_dates(new_soup):     # parse review`s dates
    unprepared_dates = new_soup.find_all('span', 'business-review-view__date')
    dates = []
    for d in unprepared_dates:
        numbers = 0
        date = d.text
        for symbol in date:
            if symbol.isdigit():
                numbers += 1
        if numbers < 3:
            date += ' 2023'
        date = date.split()
        date = date[2] + " " + date[1] + " " + date[0]
        dates.append(date)
    prepared_dates = convert_dates(dates)
    return prepared_dates


def get_title(new_soup):    # parse title of the restaurant
    title = new_soup.find_all('h1', class_="card-title-view__title")
    return title[0].text


def get_names(new_soup):    # parse user names
    all_names = new_soup.find_all('div', class_="business-review-view__author")
    fixed_names = []
    for name in all_names:
        fixed_names.append(name.find_next('span').text)
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


def parse(url, file_path):
    print("STATUS: parsing in progress...")
    if os.path.exists(file_path) is False:
        Setup.get_source_html(url)
    soup = Setup.create_soup(file_path)

    reviews = get_reviews(soup)
    total_mark = get_average_rating(soup)
    review_dates = get_dates(soup)
    rating = get_ratings(soup)
    names = get_names(soup)
    restaurant = get_title(soup)

    print("Title -", get_title(soup))
    print("Rating -", total_mark[0].text + "." + total_mark[2].text)
    print("-------------------------------------------------------------------------")
    print_all(reviews, review_dates, rating, names)
    # comments.parse_lists(rating, names, reviews, review_dates)
    for i in range(len(reviews)):
        DatabaseActions.add_element(rating[i], review_dates[i], names[i], reviews[i], restaurant)
    print("DATABASE UPDATED")
    os.remove(file_path)
    print("FILE REMOVED")

