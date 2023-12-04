from selenium import webdriver
import json
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import tkinter as tk
from selenium.webdriver.chrome.options import Options
import re
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
#-- coding: utf-8 --

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

def getInfoOne(driver, type):
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
    product = driver.find_element(By.CSS_SELECTOR, ".prod_item")
    
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
    
    # categories

    # 종료 조건
    if current_category == len(categories):
        if current_option >= min_option:  # 최소 옵션 달성 여부
            result.append(current_combination.copy())
        return

    # 부품 단위로 반복문
    for item in categories[current_category]:
        current_combination[current_category] = item
        if current_price + item['price'] > budget:
            return  # 예산 초과 시 Pruning (Backtracking)
        find_combination(categories, budget, min_option, current_category + 1, current_combination,
                         current_option + item['option'], current_price + item['price'], result)
        current_combination[current_category] = None


# 크롤링
CPU = getInfo(driver, 'cpu')
GPU = getInfo(driver, 'gpu')
SSD = getInfo(driver, 'ssd')
RAM = getInfo(driver, 'ram')

# 필요정보를 int형 변환
CPU = intArr(CPU, 'cpu')
GPU = intArr(GPU, 'gpu')
SSD = intArr(SSD, 'ssd')
RAM = intArr(RAM, 'ram')

# 정렬을 통해 pruning. 다음 카테고리 뿐만 아니라 이후 품목들도 안 살펴봐도 됨(어차피 더 비싸기 때문)
CPU = sorted(CPU, key=lambda x: x['price'])
GPU = sorted(GPU, key=lambda x: x['price'])
SSD = sorted(SSD, key=lambda x: x['price'])
RAM = sorted(RAM, key=lambda x: x['price'])

# 변수 선언
total_categories = [CPU, GPU, SSD, RAM]  # 카테고리 순서
input_combination = [None] * 4  # 초기값. 사용자가 선택한 부품을 채워서 받아야함.
input_combination = [None, None, None, {'name': 'RAM1', 'option': 1, 'price': 15}]  # debugging용 테스트 input

budget = 700000  # UI로 입력받아야함.
min_option = 10  # UI로 입력받아야함.

current_price = 0
current_option = 0
current_categories = []
index_list = []
data = []
# 선택한 부품 처리 + 함수 매개변수로 넘길 리스트 만들기
for i in range(4):
    if input_combination[i] != None:  # 이미 선택된 품목 처리
        current_price += input_combination[i]['price']
        current_option += input_combination[i]['option']
        index_list.append(i)
    else:  # 알고리즘을 돌릴 카테고리 리스트 생성
        current_categories.append(total_categories[i])

result = []

find_combination(current_categories, budget, min_option, 0, [None] * len(current_categories), current_option,
                 current_price, result)

for combination in result:
    for i in index_list:
        combination.insert(i,input_combination[i])
    data.append(combination)
    
final_combinations = []

for combination in data:
    item_names = [item['name'] for item in combination]
    total_price = sum(item['price'] for item in combination)
    item_names.append(total_price)
    final_combinations.append(item_names)


# GUI

def add_text_to_scroll(text):
    scroll_text.insert(tk.END, text + "\n")
    scroll_text.yview(tk.END)


def toggle_textfield(var, checkbox_var, text_widget, confirm_btn, modify_btn):
    if checkbox_var.get() == 1:
        text_widget.config(state="normal")
        confirm_btn.config(state="normal")
        modify_btn.config(state="disabled")
    else:
        print(var)
        if var == "CPU":
            CPU = ""
        elif var == "GPU":
            GPU = ""
        elif var == "SSD":
            SSD = ""
        elif var == "RAM":
            RAM = ""
        print(var)
        text_widget.config(state="disabled")
        confirm_btn.config(state="disabled")
        modify_btn.config(state="disabled")


def confirm_click(text_widget, confirm_btn, modify_btn, purpose):
    text_content = text_widget.get("1.0", "end-1c")

    if purpose == "CPU":
        CPU = text_content
    elif purpose == "GPU":
        GPU = text_content
    elif purpose == "SSD":
        SSD = text_content
    elif purpose == "RAM":
        RAM = text_content

    print(f"{purpose} Selected Purpose:", text_content)
    text_widget.config(state="disabled")
    confirm_btn.config(state="disabled")
    modify_btn.config(state="normal")


def enable_editing_components(text_widget, confirm_btn, modify_btn):
    text_widget.config(state="normal")
    confirm_btn.config(state="normal")
    modify_btn.config(state="disabled")


def on_combobox_select(event):
    selected_value = combo_var.get()
    print("Selected:", selected_value)


def disable_combobox():
    combobox.config(state="readonly")
    confirm_button.config(state="disabled")
    modify_button.config(state="normal")


def confirm_selection():
    combobox.config(state="disabled")
    confirm_button.config(state="disabled")
    modify_button.config(state="normal")


def enable_combobox():
    combobox.config(state="normal")
    confirm_button.config(state="normal")
    modify_button.config(state="disabled")


def budget_confirm_click():
    global userBudget
    userBudget = int(budgetText.get("1.0", "end-1c"))
    budgetText.config(state="disabled")
    budgetconfirmBtn.config(state="disabled")
    modifyBtn.config(state="normal")


def enable_editing():
    budgetText.config(state="normal")
    budgetconfirmBtn.config(state="normal")
    modifyBtn.config(state="disabled")


def openFrame(frame):
    frame.tkraise()


window = tk.Tk()
window.title("Algorithms")
window.geometry("500x750")

# 시작 화면
frame1 = tk.Frame(window)
frame1.grid(row=0, column=0, sticky="nsew")

titLabel = tk.Label(frame1, text="Custom PC Build Helper", font=("Arial", 20, "bold"), fg="#2B2B2B")
titLabel.grid(row=0, column=0, padx=80, pady=(160, 10))

subLabel = tk.Label(frame1, text="1. Enter your budget", font=("Arial", 12), fg="#3D3D3D")
subLabel.grid(row=1, column=0, padx=100, pady=(60, 0))

subLabel2 = tk.Label(frame1, text="2. Enter a purpose", font=("Arial", 12), fg="#3D3D3D")
subLabel2.grid(row=2, column=0, padx=100, pady=(20, 10))

subLabel3 = tk.Label(frame1, text="3. Enter a fixed part", font=("Arial", 12), fg="#3D3D3D")
subLabel3.grid(row=3, column=0, padx=100, pady=10)

# 사용자 입력 화면
# 사용자 입력 화면 - 예산 입력 (userBudget 변수에 int형으로 저장됨)
frame2 = tk.Frame(window)
frame2.grid(row=0, column=0, sticky="nsew")

budgetLabel = tk.Label(frame2, text="1. Enter your budget", font=("Arial", 15), fg="#2B2B2B")
budgetLabel.grid(row=0, column=0, padx=(50, 0), pady=(60, 0))

budgetText = tk.Text(frame2, height=2, width=25, bd=1, relief="solid")
budgetText.grid(row=1, column=0, padx=(70, 0), pady=(20, 10))

budgetconfirmBtn = tk.Button(frame2, text="Confirm", command=budget_confirm_click, height=1, width=10,
                             bg="#0099BC", fg="#F7FFFF", state="normal")
budgetconfirmBtn.grid(row=1, column=1, padx=(10, 0), pady=(10, 0))

modifyBtn = tk.Button(frame2, text="Modify", command=enable_editing, height=1, width=10, bg="#0099BC", fg="#F7FFFF",
                      state="disabled")
modifyBtn.grid(row=1, column=2, padx=(10, 0), pady=(10, 0))

# 사용자 입력 화면 - 용도 입력 (purpose 변수에 string형으로 저장됨)
purposeLabel = tk.Label(frame2, text="2. Enter a purpose", font=("Arial", 15), fg="#2B2B2B")
purposeLabel.grid(row=2, column=0, padx=(33, 0), pady=(0, 0))

combo_var = tk.StringVar()
combobox = ttk.Combobox(frame2, textvariable=combo_var, values=["Documentation work", "professionals", "gaming",
                                                                "Versatile"])
combobox.config(width=15, state="readonly")
combobox.bind("<<ComboboxSelected>>", on_combobox_select)
combobox.grid(row=2, column=0, padx=(119, 0), pady=(90, 0))

confirm_button = tk.Button(frame2, text="Confirm", command=confirm_selection, height=1, width=10, bg="#0099BC",
                           fg="#F7FFFF")
confirm_button.grid(row=2, column=1, padx=(10, 0), pady=(90, 0))

modify_button = tk.Button(frame2, text="Modify", command=enable_combobox, state="disabled", height=1, width=10,
                          bg="#0099BC", fg="#F7FFFF")
modify_button.grid(row=2, column=2, padx=(10, 0), pady=(90, 0))

# 사용자 입력 화면 - 고정 항목 입력 (CPU, GPU, SSD, RAM 에 string형으로 저장, 없으면 초기값)
# CPU값 입력
fixLabel = tk.Label(frame2, text="3. Enter a fixed part", font=("Arial", 15), fg="#2B2B2B")
fixLabel.grid(row=3, column=0, padx=(33, 0), pady=(38, 0))

fixCPUText = tk.Text(frame2, height=2, width=25, bd=1, relief="solid")
fixCPUText.grid(row=4, column=0, padx=(45, 0), pady=(20, 10))
default_text = "CPU"
fixCPUText.insert("1.0", default_text)

fixCPUConfirmBtn = tk.Button(frame2, text="Confirm",
                             command=lambda: confirm_click(fixCPUText, fixCPUConfirmBtn, fixCPUModifyBtn, "CPU"),
                             height=1, width=10, bg="#0099BC", fg="#F7FFFF", state="disabled")

fixCPUConfirmBtn.grid(row=4, column=1, padx=(10, 0), pady=(10, 0))

fixCPUModifyBtn = tk.Button(frame2, text="Modify",
                            command=lambda: enable_editing_components(fixCPUText, fixCPUConfirmBtn, fixCPUModifyBtn),
                            height=1, width=10, bg="#0099BC", fg="#F7FFFF", state="disabled")
fixCPUModifyBtn.grid(row=4, column=2, padx=(10, 0), pady=(10, 0))

checkbox_var1 = tk.IntVar()
checkbox1 = tk.Checkbutton(frame2, text="", variable=checkbox_var1,
                           command=lambda: toggle_textfield("CPU", checkbox_var1, fixCPUText, fixCPUConfirmBtn,
                                                            fixCPUModifyBtn))
checkbox1.grid(row=4, column=3, padx=(10, 0), pady=(10, 0))

# GPU값 입력
fixGPUText = tk.Text(frame2, height=2, width=25, bd=1, relief="solid")
fixGPUText.grid(row=5, column=0, padx=(45, 0), pady=(20, 10))
default_text = "GPU"
fixGPUText.insert("1.0", default_text)

fixGPUConfirmBtn = tk.Button(frame2, text="Confirm",
                             command=lambda: confirm_click(fixGPUText, fixGPUConfirmBtn, fixGPUModifyBtn, "GPU"),
                             height=1, width=10, bg="#0099BC", fg="#F7FFFF", state="disabled")

fixGPUConfirmBtn.grid(row=5, column=1, padx=(10, 0), pady=(10, 0))

fixGPUModifyBtn = tk.Button(frame2, text="Modify",
                            command=lambda: enable_editing_components(fixGPUText, fixGPUConfirmBtn, fixGPUModifyBtn),
                            height=1, width=10, bg="#0099BC", fg="#F7FFFF", state="disabled")
fixGPUModifyBtn.grid(row=5, column=2, padx=(10, 0), pady=(10, 0))

checkbox_var2 = tk.IntVar()
checkbox2 = tk.Checkbutton(frame2, text="", variable=checkbox_var2,
                           command=lambda: toggle_textfield("GPU", checkbox_var2, fixGPUText, fixGPUConfirmBtn,
                                                            fixGPUModifyBtn))
checkbox2.grid(row=5, column=3, padx=(10, 0), pady=(10, 0))

# SSD값 입력
fixSSDText = tk.Text(frame2, height=2, width=25, bd=1, relief="solid")
fixSSDText.grid(row=6, column=0, padx=(45, 0), pady=(20, 10))
default_text = "SSD"
fixSSDText.insert("1.0", default_text)

fixSSDConfirmBtn = tk.Button(frame2, text="Confirm",
                             command=lambda: confirm_click(fixSSDText, fixSSDConfirmBtn, fixSSDModifyBtn, "SSD"),
                             height=1, width=10, bg="#0099BC", fg="#F7FFFF", state="disabled")

fixSSDConfirmBtn.grid(row=6, column=1, padx=(10, 0), pady=(10, 0))

fixSSDModifyBtn = tk.Button(frame2, text="Modify",
                            command=lambda: enable_editing_components(fixSSDText, fixSSDConfirmBtn, fixSSDModifyBtn),
                            height=1, width=10, bg="#0099BC", fg="#F7FFFF", state="disabled")
fixSSDModifyBtn.grid(row=6, column=2, padx=(10, 0), pady=(10, 0))

checkbox_var3 = tk.IntVar()
checkbox3 = tk.Checkbutton(frame2, text="", variable=checkbox_var3,
                           command=lambda: toggle_textfield("SSD", checkbox_var3, fixSSDText, fixSSDConfirmBtn,
                                                            fixSSDModifyBtn))
checkbox3.grid(row=6, column=3, padx=(10, 0), pady=(10, 0))

# RAM값 입력
fixRAMText = tk.Text(frame2, height=2, width=25, bd=1, relief="solid")
fixRAMText.grid(row=7, column=0, padx=(45, 0), pady=(20, 10))
default_text = "RAM"
fixRAMText.insert("1.0", default_text)

fixRAMConfirmBtn = tk.Button(frame2, text="Confirm",
                             command=lambda: confirm_click(fixRAMText, fixRAMConfirmBtn, fixRAMModifyBtn, "RAM"),
                             height=1, width=10, bg="#0099BC", fg="#F7FFFF", state="disabled")
fixRAMConfirmBtn.grid(row=7, column=1, padx=(10, 0), pady=(10, 0))

fixRAMModifyBtn = tk.Button(frame2, text="Modify",
                            command=lambda: enable_editing_components(fixRAMText, fixRAMConfirmBtn, fixRAMModifyBtn),
                            height=1, width=10, bg="#0099BC", fg="#F7FFFF", state="disabled")
fixRAMModifyBtn.grid(row=7, column=2, padx=(10, 0), pady=(10, 0))

checkbox_var4 = tk.IntVar()
checkbox4 = tk.Checkbutton(frame2, text="", variable=checkbox_var4,
                           command=lambda: toggle_textfield("RAM", checkbox_var4, fixRAMText, fixRAMConfirmBtn,
                                                            fixRAMModifyBtn))
checkbox4.grid(row=7, column=3, padx=(10, 0), pady=(10, 0))

# 결과 화면
frame3 = tk.Frame(window)
frame3.grid(row=0, column=0, sticky="nsew")

resultLabel = tk.Label(frame3, text="Result", font=("Arial", 18), fg="#2B2B2B")
resultLabel.grid(row=0, column=0, padx=(0, 0), pady=(70, 0), columnspan=5)

scroll_text = scrolledtext.ScrolledText(frame3, wrap=tk.WORD, width=60, height=40)
scroll_text.grid(row=1, column=0, padx=32, pady=20, columnspan=3)

# 이전 코드에서 추가한 부분
result_strings = []

for combination in final_combinations:
    # 각 조합을 JSON 형식의 문자열로 변환
    json_string = json.dumps(combination, ensure_ascii=False).encode('utf-8').decode('utf-8')
    result_strings.append(json_string)

# 이전 코드에서 추가한 부분
for string in result_strings:
    add_text_to_scroll(string)



# 버튼 설정
btnToFrame2 = tk.Button(frame1, text="Start", padx=10, pady=10, command=lambda: openFrame(frame2), width=15,
                        bg="#0099BC", fg="#F7FFFF")
btnToFrame3 = tk.Button(frame2, text="Confirm", padx=10, pady=10, command=lambda: openFrame(frame3), width=10,
                        bg="#0099BC", fg="#F7FFFF")

btnToFrame2.grid(row=4, column=0, pady=25)
btnToFrame3.grid(row=8, column=0, padx=(50, 0), pady=40, columnspan=5)
openFrame(frame1)

window.mainloop()
