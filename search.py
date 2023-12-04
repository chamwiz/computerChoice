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
            MHz = ""
            specs = product.find_elements(By.CSS_SELECTOR, ".spec_item")
            name = product.find_element(By.CSS_SELECTOR, ".prod_name > strong").text

            # 제품명에 'RGB'가 포함된경우도 GB로 인식하기에 GB값 추출하는 용도의 새로운 변수를 생성
            searchName=name.replace('RGB','')

            # GB값 추출
            GB=searchName[searchName.find('(')+1:searchName.find('GB')]

            for i in specs:
                if "MHz" in i.text:
                    MHz = i.text

            # MHz값 추출
            MHz = MHz[0:MHz.find('MHz')]

            ram = {
               "name" : name,
                "price" : product.find_element(By.CSS_SELECTOR, ".low_price > dd").text,
                "MHz" : MHz,
                "GB" : GB
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
    return arr

def intArr(stringArr, type):
    arr=[]

    if type == "cpu":
        for i in range(len(stringArr)):
            cpu={
            "name" : stringArr[i].name,
            #option: benchmark
            "price" : int(re.sub(r'[^0-9]','', stringArr[i].get('price')))
            }
            arr.append(cpu)

    elif type == "gpu":
        for i in range(len(stringArr)):
            gpu={
            "name" : stringArr[i].get('name'),
            #option: benchmark
            "price" : int(re.sub(r'[^0-9]','', stringArr[i].get('price')))
            }
            arr.append(gpu)

    elif type == "ram":
        for i in range(len(stringArr)):
            # RAM의 MHz값과 GB값 각각 가중치를 이용해 임의적인 option 기준 생성
            option = int(stringArr[i].get('MHz'))/800 + int(stringArr[i].get('GB'))

            ram={
            "name" : stringArr[i].get('name'),
            "option" : option,
            "price" : int(re.sub(r'[^0-9]','', stringArr[i].get('price')))
            }
            arr.append(ram)

    elif type == "ssd":
        for i in range(len(stringArr)):
            # TB는 GB로 변환
            search = stringArr[i].get('capacity')
            if stringArr[i].get('capacity').find('GB') == -1:
                temp = int(re.sub(r'[^0-9]','', stringArr[i].get('capacity'))) * 1024
            else:
                temp = int(re.sub(r'[^0-9]','', stringArr[i].get('capacity')))

            ssd={
            "name" : stringArr[i].get('name'),
            "option" : temp,
            "price" : int(re.sub(r'[^0-9]','', stringArr[i].get('price')))
            }
            arr.append(ssd)

    return arr


chrome_options = Options()
driver = webdriver.Chrome()

# 검색하고자 하는 카테고리 (cpu, ram, gpu, ssd // 소문자 사용)
searchType = 'ram'

# 정보 검색
arr = getInfo(driver, searchType)

# 정보 변환 (옵션과 가격 int형 변환 및 단위값 통일)
arr = intArr(arr, searchType)

# 결과 출력
for i in range(len(arr)):
    print(arr[i])

# # Tkinter 윈도우 생성
# window = tk.Tk()
# window.title("Tkinter 예제")

# # 입력 상자 생성
# entry = tk.Entry(window)
# entry.grid(row=0, column=1)

# # Tkinter 이벤트 루프 시작
# window.mainloop()