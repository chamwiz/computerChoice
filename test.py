from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import tkinter as tk
print()
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
            driver.get("https://prod.danawa.com/list/?cate=21349942")
    elif type == "ram":
        driver.get("https://prod.danawa.com/list/?cate=21349943")
    elif type == "gpu":
        driver.get("https://prod.danawa.com/list/?cate=21349945")
    elif type == "ssd":
        driver.get("https://prod.danawa.com/list/?cate=21349946")
    elif type == "ssd":
        driver.get("https://prod.danawa.com/list/?cate=21349947")
    elif type == "mainboard":
        driver.get("https://prod.danawa.com/list/?cate=21349944")

    driver.implicitly_wait(5)
    # 물건
    products = driver.find_elements(By.CSS_SELECTOR, ".prod_item")
    for product in products:
        if type == "cpu":
            cpu = {
                "name" : product.find_element(By.CSS_SELECTOR, ".prod_name > a").text,
                "price" : product.find_element(By.CSS_SELECTOR, ".main_price > a > .low_price > dd > span").text
            }
            arr.append(cpu)
        elif type == "ram":
            ram = {
                "name" : product.find_element(By.CSS_SELECTOR, ".prod_name > a").text,
                "price" : product.find_element(By.CSS_SELECTOR, ".main_price > a > .low_price > dd > span").text
            }
            arr.append(ram)
        elif type == "gpu":
            gpu = {
                "name" : product.find_element(By.CSS_SELECTOR, ".prod_name > a").text,
                "price" : product.find_element(By.CSS_SELECTOR, ".main_price > a > .low_price > dd > span").text
            }
            arr.append(gpu)
        elif type == "ssdhdd":
            ssdhdd = {
                "name" : product.find_element(By.CSS_SELECTOR, ".prod_name > a").text,
                "price" : product.find_element(By.CSS_SELECTOR, ".main_price > a > .low_price > dd > span").text
            }
            arr.append(ssdhdd)
        elif type == "mainboard":
            mainboard = {
                "name" : product.find_element(By.CSS_SELECTOR, ".prod_name > a").text,
                "price" : product.find_element(By.CSS_SELECTOR, ".main_price > a > .low_price > dd > span").text
            }
            arr.append(mainboard)


    return arr

driver = webdriver.Chrome()
cpuArr = getInfo(driver, "ram")

# 윈도우 생성
window = tk.Tk()
window.title("컴퓨터 부품 선택 알고리즘")
window.geometry("400x300")

# 라벨 생성
label = tk.Label(window, text="환영합니다!")
label.pack(padx=10, pady=10)

# 버튼 생성
button = tk.Button(window, text="인사하기")
button.pack(padx=10, pady=10)

# 윈도우 실행
window.mainloop()