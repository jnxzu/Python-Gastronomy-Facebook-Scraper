import time

from selenium import webdriver

logo_path = "C:\\Users\\xsero\\Desktop\\Projekty\\Python - Gastronomy Facebook Scraper\\logo.jpg"
bg_path = "C:\\Users\\xsero\\Desktop\\Projekty\\Python - Gastronomy Facebook Scraper\\bg.png"


def login():
    driver = webdriver.Firefox()
    driver.set_window_position(-2000, 0)
    driver.get("https://panel.finebite.co/")
    driver.minimize_window()
    driver.find_element_by_xpath(
        "//input[@name='email']").send_keys("")  # redacted
    driver.find_element_by_xpath(
        "//input[@name='password']").send_keys("")  # redacted
    driver.find_element_by_xpath("//input[@value='Zaloguj']").click()
    return driver


def insert(place, driver):
    driver.get("https://panel.finebite.co/places/new")
    driver.find_element_by_xpath(
        "//input[@name='name']").send_keys(place.nazwa)
    driver.find_element_by_xpath(
        "//textarea[@name='description[plNominative]']").send_keys(place.opis)
    driver.find_element_by_xpath(
        "//input[@type='file' and not(@multiple)]").send_keys(logo_path)
    driver.find_element_by_xpath(
        "//input[@type='file' and @multiple]").send_keys(bg_path)
    miasta = driver.find_element_by_xpath("//select[@name='city']")
    for miasto in miasta.find_elements_by_tag_name('option'):
        if miasto.text == place.miasto:
            miasto.click()
    driver.find_element_by_xpath(
        "//input[@name='street']").send_keys(place.adres)
    driver.find_element_by_xpath(
        "//button[contains(text(), 'Wskaż automatycznie na podstawie adresu')]").click()
    driver.find_element_by_xpath("//span[contains(text(), '$$')]").click()
    driver.find_element_by_xpath(
        "//input[@name='info[website]']").send_keys(place.web)
    driver.find_element_by_xpath(
        "//input[@name='info[facebook]']").send_keys(place.fb)
    driver.find_element_by_xpath(
        "//input[@name='info[instagramId]']").send_keys(place.ig)
    driver.find_element_by_xpath(
        "//input[@name='info[email]']").send_keys(place.email)
    driver.find_element_by_xpath(
        "//input[@name='info[phone]']").send_keys(place.tel)
    time.sleep(2)
    driver.find_element_by_xpath("//input[@value='Zapisz zmiany']").click()


def end(driver):
    driver.close()
