import tkinter as tk
from search import Main
from tkinter import ttk
from tkinter import scrolledtext

# 예산 저장
userBudget = 0
# 목적 저장
purpose = ""
# 고정 옵션
CPU = ""
GPU = ""
SSD = ""
RAM = ""
# 결과저장 result 에...
result = []


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

# 결과 계산
result = Main()
result = result.working()

# 결과 화면
frame3 = tk.Frame(window)
frame3.grid(row=0, column=0, sticky="nsew")

resultLabel = tk.Label(frame3, text="Reuslt", font=("Arial", 18), fg="#2B2B2B")
resultLabel.grid(row=0, column=0, padx=(0, 0), pady=(70, 0), columnspan=5)

scroll_text = scrolledtext.ScrolledText(frame3, wrap=tk.WORD, width=60, height=40)
scroll_text.grid(row=1, column=0, padx=32, pady=20, columnspan=3)

print(result)

for data in result:
    message = ', '.join(map(str, data))
    add_text_to_scroll(message)

# 버튼 설정
btnToFrame2 = tk.Button(frame1, text="Start", padx=10, pady=10, command=lambda: openFrame(frame2), width=15,
                        bg="#0099BC", fg="#F7FFFF")
btnToFrame3 = tk.Button(frame2, text="Confirm", padx=10, pady=10, command=lambda: openFrame(frame3), width=10,
                        bg="#0099BC", fg="#F7FFFF")

btnToFrame2.grid(row=4, column=0, pady=25)
btnToFrame3.grid(row=8, column=0, padx=(50, 0), pady=40, columnspan=5)
openFrame(frame1)

window.mainloop()