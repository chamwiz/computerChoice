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
            core = ""
            specs = product.find_elements(By.CSS_SELECTOR, ".spec_item")
            for i in specs:
                if "코어" in i.text:
                    core = i.text

            cpu = {
                "name" : product.find_element(By.CSS_SELECTOR, ".prod_name > strong").text,
                "price" : product.find_element(By.CSS_SELECTOR, ".low_price > dd").text,
                "core" : core
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
            gpu = ""
            specs = product.find_elements(By.CSS_SELECTOR, ".spec_item")
            for i in specs:
                if "스트림 프로세서" in i.text:
                    gpu = i.text
            gpu = {
                "name" : product.find_element(By.CSS_SELECTOR, ".prod_name > strong").text,
                "price" : product.find_element(By.CSS_SELECTOR, ".low_price > dd").text,
                "processor" :gpu
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
        elif type == "hdd":
            hdd = ""
            specs = product.find_elements(By.CSS_SELECTOR, ".spec_item")
            for i in specs:
                if "메모리" in i.text:
                    hdd = i.text
            hdd = {
                "name" : product.find_element(By.CSS_SELECTOR, ".prod_name > strong").text,
                "price" : product.find_element(By.CSS_SELECTOR, ".low_price > dd").text,
                "capacity" :hdd
            }
            arr.append(hdd)
        elif type == "mainboard":
            mainboard = {
                "name" : product.find_element(By.CSS_SELECTOR, ".prod_name > strong").text,
                "price" : product.find_element(By.CSS_SELECTOR, ".low_price > dd").text
            }
            arr.append(mainboard)
    return arr

chrome_options = Options()
driver = webdriver.Chrome()
cpuArr = getInfo(driver, "ssd")
print()
# # Tkinter 윈도우 생성
# window = tk.Tk()
# window.title("Tkinter 예제")

# # 입력 상자 생성
# entry = tk.Entry(window)
# entry.grid(row=0, column=1)

# # Tkinter 이벤트 루프 시작
# window.mainloop()