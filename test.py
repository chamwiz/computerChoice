from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import tkinter as tk
from selenium.webdriver.chrome.options import Options
import re


a = {
    "CPU" : "",
    "RAM" : "",
    "GPU" : "",
    "SSD/HDD" : "",
    "MAINBOARD" : ""
}

def getInfo(driver, type):
    arr = []
    if type == "cpu":
        driver.get("https://shop.danawa.com/main/?controller=goods&methods=search&keyword=cpu")
    elif type == "ram":
        driver.get("https://shop.danawa.com/main/?controller=goods&methods=search&keyword=%EC%BB%B4%ED%93%A8%ED%84%B0%20%EB%9E%A8")
    elif type == "gpu":
        driver.get("https://shop.danawa.com/main/?controller=goods&methods=search&keyword=%EA%B7%B8%EB%9E%98%ED%94%BD%EC%B9%B4%EB%93%9C")
    elif type == "ssd":
        driver.get("https://shop.danawa.com/main/?controller=goods&methods=search&keyword=ssd")
    elif type == "hdd":
        driver.get("https://shop.danawa.com/main/?controller=goods&methods=search&keyword=hdd")
    elif type == "mainboard":
        driver.get("https://shop.danawa.com/main/?controller=goods&methods=search&keyword=%EB%A9%94%EC%9D%B8%EB%B3%B4%EB%93%9C")

    driver.implicitly_wait(5)
    # 샵 다나와 클릭
    driver.find_element(By.CSS_SELECTOR, "#searchGoods").click()
    time.sleep(2)
    # 물건
    products = driver.find_elements(By.CSS_SELECTOR, ".prod_item")
    for product in products:
        if type == "cpu":
            print()
            cpu = {
                "name" : product.find_element(By.CSS_SELECTOR, ".prod_name > strong").text,
                "price" : product.find_element(By.CSS_SELECTOR, ".low_price > dd").text,
                "score" : 0
            }
            arr.append(cpu)
        elif type == "ram":
            ddr = ""
            specs = product.find_elements(By.CSS_SELECTOR, ".spec_item")
            for i in specs:
                if "DDR" in i.text:
                    ddr = i.text
            ram = {
               "name" : product.find_element(By.CSS_SELECTOR, ".prod_name > strong").text,
                "price" : product.find_element(By.CSS_SELECTOR, ".low_price > dd").text,
                "ddr" : ddr
            }
            arr.append(ram)
        elif type == "gpu":
            gpu = {
                "name" : product.find_element(By.CSS_SELECTOR, ".prod_name > strong").text,
                "price" : product.find_element(By.CSS_SELECTOR, ".low_price > dd").text,
                "score" :0
            }
            arr.append(gpu)
        elif type == "ssd":
            ssd = ""
            specs = product.find_element(By.CSS_SELECTOR, ".prod_name > strong")
            if "TB" in specs.text or "GB" in specs.text:
                ssd = specs.text
            # 정규 표현식을 사용하여 괄호 안의 문자열 추출
            match = re.search(r'\((.*?)\)', ssd)
            if match:
                extracted_string = match.group(1)
                ssd = extracted_string
            ssd = {
                "name" : product.find_element(By.CSS_SELECTOR, ".prod_name > strong").text,
                "price" : product.find_element(By.CSS_SELECTOR, ".low_price > dd").text,
                "capacity" :ssd
            }
            arr.append(ssd)
    return arr

def getScore(driver, arr, type):
    if type == "cpu":
        for i in arr:
            name = i["name"]
            # 정규표현식을 사용하여 연속된 숫자 뒤에 문자까지 추출
            matches = re.findall(r'\d+[^\s]*', name)
            # 리스트의 마지막 항목 가져오기
            if matches:
                last_match = matches[-1]
            else:
                last_match = ""
            driver.get("https://cpu-benchmark.org/search?k=" + last_match)
            driver.implicitly_wait(2)
            try:
                score = driver.find_element(By.CSS_SELECTOR, 'body > div.container.mt-3.p-3.frame > div:nth-child(2) > div > div > table > tbody > tr > td:nth-child(5)').click().text
                i["score"] = score
            except:
                pass
    elif type == "gpu":
        pass

chrome_options = Options()
driver = webdriver.Chrome()
cpuArr = getInfo(driver, "cpu")
getScore(driver, cpuArr, "cpu")
print()


