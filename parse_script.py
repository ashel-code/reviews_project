import time
import os.path
from selenium import webdriver
from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

URL = "https://yandex.ru/maps/213/moscow/?ll=37.589146%2C55.731010&mode=poi&poi%5Bpoint%5D=37." \
      "589146%2C55.731010&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D153977379747&tab=reviews&z=17.32"
FILE_PATH = "page-source.html"


class Setup:
    @staticmethod
    def create_soup(file_path):
        with open(file_path, 'r') as file:
            source = file.read()
        file.close()
        new_soup = BeautifulSoup(source, 'lxml')
        return new_soup

    @staticmethod
    def get_source_html(url):
        web_driver = webdriver.Safari()
        web_driver.get(url=url)
        time.sleep(5)
        with open('page-source.html', 'w') as file:
            file.write(web_driver.page_source)
        file.close()
        web_driver.quit()


class Prints:
    @staticmethod
    def print_reviews(all_reviews):  # печать всех отзывов
        for i, review in enumerate(all_reviews):
            print(i + 1, review.text)

    @staticmethod
    def print_dates(dates):  # печать всех дат написания отзывов
        for i, date in enumerate(dates):
            print(i + 1, date.text)

    @staticmethod
    def print_all(all_reviews, all_dates, all_ratings, all_names):
        for i in range(len(reviews)):
            print(i + 1, " - ", all_names[i].text, " - ", all_dates[i].text,
                  " - ", all_ratings[i], " - ", all_reviews[i].text)


def get_reviews(new_soup):     # парсинг всех отзывов
    all_reviews = new_soup.find_all('span', 'business-review-view__body-text')
    return all_reviews


def get_average_rating(new_soup):     # парсинг средней оценки
    average_rating = new_soup.find_all('span', 'business-summary-rating-badge-view__rating-text')
    return average_rating


def get_dates(new_soup):     # парсинг дат написания отзывов
    dates = new_soup.find_all('span', 'business-review-view__date')
    return dates


def get_title(new_soup):
    title = new_soup.find_all('h1', class_="card-title-view__title")
    return title[0].text


def get_names(new_soup):
    all_names = new_soup.find_all('div', class_="business-review-view__author")
    fixed_names = []
    for name in all_names:
        fixed_names.append(name.find_next('a'))
    return fixed_names


def get_ratings(new_soup):
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


if os.path.exists(FILE_PATH) is False:
    Setup.get_source_html(URL)
soup = Setup.create_soup(FILE_PATH)


reviews = get_reviews(soup)
total_mark = get_average_rating(soup)
review_dates = get_dates(soup)
rating = get_ratings(soup)
names = get_names(soup)

print("Название -", get_title(soup))
print("Оценка -", total_mark[0].text + "." + total_mark[2].text)
print("-------------------------------------------------------------------------")
Prints.print_all(reviews, review_dates, rating, names)
