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

class Search:
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

                core_str=stringArr[i].get('core')
                if 'P' in core_str and 'E' in core_str:
                    # 'Px+Ey코어' 형태의 경우
                    p_index = core_str.index('P')
                    e_index = core_str.index('E')
                    x = int(core_str[p_index + 1:e_index - 1])
                    y = int(core_str[e_index + 1:].replace('코어', ''))
                    core = 2 * x + y
                elif '코어' in core_str:
                    # 'x코어' 형태의 경우
                    core = int(core_str.replace('코어', ''))

                cpu={
                "name" : stringArr[i].get('name'),
                # core
                "option": core/2,
                "price" : int(re.sub(r'[^0-9]','', stringArr[i].get('price')))
                }
                arr.append(cpu)

        elif type == "gpu":
            for i in range(len(stringArr)):
                processor_str=stringArr[i].get('processor')
                processor = processor_str[processor_str.find(':')+1:processor_str.find('개')]

                gpu={
                "name" : stringArr[i].get('name'),
                "option" : int(processor)/250,
                "price" : int(re.sub(r'[^0-9]','', stringArr[i].get('price')))
                }
                arr.append(gpu)

        elif type == "ram":
            for i in range(len(stringArr)):
                # RAM의 MHz값과 GB값 각각 가중치를 이용해 임의적인 option 기준 생성
                option = int(stringArr[i].get('MHz'))/800 + int(stringArr[i].get('GB'))

                ram={
                "name" : stringArr[i].get('name'),
                "option" : option/5,
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
                "option" : temp/512,
                "price" : int(re.sub(r'[^0-9]','', stringArr[i].get('price')))
                }
                arr.append(ssd)

        return arr


    chrome_options = Options()
    driver = webdriver.Chrome()

    # 카테고리 단위로 재귀 호출
    def find_combination(categories, budget, min_option, current_category, current_combination, current_option,
                         current_price, result):
        # 종료 조건
        if current_category == len(categories):
            if current_option >= min_option:  # 최소 옵션 달성 여부 (조건 1)
                result.append(current_combination.copy())
            return

        # 부품 단위로 반복문
        for item in categories[current_category]:
            current_combination[current_category] = item
            if current_price + item['price'] > budget:
                return  # 예산 초과 시 Pruning (Backtracking) (조건 2)
            Search.find_combination(categories, budget, min_option, current_category + 1, current_combination,
                             current_option + item['option'], current_price + item['price'], result)
            current_combination[current_category] = None

class Main:
    def __init__(self):
        pass

    def working(self):
        # 크롤링
        CPU = Search.getInfo(Search.driver, 'cpu')
        GPU = Search.getInfo(Search.driver, 'gpu')
        SSD = Search.getInfo(Search.driver, 'ssd')
        RAM = Search.getInfo(Search.driver, 'ram')

        # 필요정보를 int형 변환
        CPU = Search.intArr(CPU, 'cpu')
        GPU = Search.intArr(GPU, 'gpu')
        SSD = Search.intArr(SSD, 'ssd')
        RAM = Search.intArr(RAM, 'ram')

        # 정렬을 통해 pruning. 다음 카테고리 뿐만 아니라 이후 품목들도 안 살펴봐도 됨(어차피 더 비싸기 때문)
        CPU = sorted(CPU, key=lambda x: x['price'])
        GPU = sorted(GPU, key=lambda x: x['price'])
        SSD = sorted(SSD, key=lambda x: x['price'])
        RAM = sorted(RAM, key=lambda x: x['price'])

        # 변수 선언
        total_categories = [CPU, GPU, SSD, RAM]  # 카테고리 순서
        input_combination = [None] * 4  # 초기값. 사용자가 선택한 부품을 채워서 받아야함.
        input_combination = [None, None, None, None]

        budget = 700000  # UI로 입력받아야함.
        min_option = 30  # UI로 입력받아야함.

        current_price = 0
        current_option = 0
        current_categories = []
        index_list = []

        # 선택한 부품 처리 + 함수 매개변수로 넘길 리스트 만들기
        for i in range(4):
            if input_combination[i] != None:  # 이미 선택된 품목 처리
                current_price += input_combination[i]['price']
                current_option += input_combination[i]['option']
                index_list.append(i)
            else:  # 알고리즘을 돌릴 카테고리 리스트 생성
                current_categories.append(total_categories[i])

        result = []

        Search.find_combination(current_categories, budget, min_option, 0, [None] * len(current_categories), current_option,
                         current_price, result)

        print("result")

        data = []

        for combination in result:
            for i in index_list:
                combination.insert(i, input_combination[i])
            data.append(combination)

        final_combinations = []

        for combination in data:
            item_names = [item['name'] for item in combination]
            total_price = sum(item['price'] for item in combination)
            item_names.append(total_price)
            final_combinations.append(item_names)

        # # 출력 디버깅
        # print("Final Combinations:")
        # for final_combination in final_combinations:
        #     print(final_combination)

        return final_combinations

if __name__ == '__main__':
    main = Main()
    main.working()