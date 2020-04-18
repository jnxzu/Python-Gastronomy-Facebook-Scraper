import urllib.request as url

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from Place import Place


def open_driver():
    driver = webdriver.Firefox()
    driver.set_window_position(-2000, 0)
    driver.get("https://www.facebook.com/")
    driver.minimize_window()
    return driver


def scrape(page, driver):
    driver.get(page)
    driver.get(driver.find_element_by_xpath(
        "//div[@data-key='tab_about']/a").get_attribute("href"))

    nazwa = driver.find_element_by_xpath("//a[@class='_64-f']/span").text

    try:
        opis = driver.find_element_by_xpath(
            "//div[@class='_1xnd']//div[text()='Informacje']/following::div[1]").get_attribute("textContent")
        if opis.endswith("Zobacz więcej"):
            opis = opis[:-13]
    except Exception:
        opis = ""
    try:
        url.urlretrieve(driver.find_element_by_xpath("//a[@aria-label='Zdjęcie profilowe']/div/img").get_attribute("src"),
                        "logo.jpg")
    except:
        print("Brak logo.")

    try:
        url.urlretrieve(driver.find_element_by_xpath(
            "//a[@rel='theater']/div/div").get_attribute("src"), "bg.png")

    except:
        print("Brak tła.")

    try:
        miasto = driver.find_element_by_xpath(
            "//div[@class='_4bl9']/div[2]/span").text.split(",")[0]
        adres = driver.find_element_by_xpath(
            "//div[@class='_4bl9']/div[1]/span").text
    except:
        miasto = ""
        adres = ""
        print("Brak adresu.")

    fb = page

    try:
        ig = driver.find_element_by_xpath(
            "//div[@class='_1xnd']//a[contains(@href,'instagram')]/div").text
        if "/" in ig:
            ig = ig.rsplit("/", 1)[1]
    except NoSuchElementException:
        ig = ""

    try:
        email = driver.find_element_by_xpath(
            "//div[@class='_1xnd']//a[not(@target)]/div").text
    except NoSuchElementException:
        email = ""

    try:
        tel = driver.find_element_by_xpath(
            "//div[@class='_3n4o']//div[@class='_50f4']").text.split(" ", 1)[1]
    except NoSuchElementException:
        tel = ""

    try:
        web = driver.find_element_by_xpath(
            "//div[@class='_1xnd']//a[not(contains(@href,'instagram')) and (@target)]/div").text
    except NoSuchElementException:
        web = ""

    return Place(nazwa, opis, miasto, adres, fb, ig, email, tel, web)


def end(driver):
    driver.close()
