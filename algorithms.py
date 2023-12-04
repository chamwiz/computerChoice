import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

userBudget = 0
purpose = ""
CPU=""
GPU=""
SSD=""
RAM=""


# GUI

def ram_toggle_textfield():
    if checkbox_var4.get() == 1:
        fixRAMText.config(state="normal")  
        fixRAMConfirmBtn.config(state="normal")  
        fixRAMModifyBtn.config(state="disabled")  
    else:
        fixRAMText.config(state="disabled")  
        fixRAMConfirmBtn.config(state="disabled")  
        fixRAMModifyBtn.config(state="disabled")

def fixRAM_confirm_click():  
    text_content = fixRAMText.get("1.0", "end-1c")
    RAM = text_content
    print("RAM Selected Purpose:", RAM)
    fixRAMText.config(state="disabled")
    fixRAMConfirmBtn.config(state="disabled")
    fixRAMModifyBtn.config(state="normal")

def ram_enable_editing():
    fixRAMText.config(state="normal")
    fixRAMConfirmBtn.config(state="normal")
    fixRAMModifyBtn.config(state="disabled")

def ssd_toggle_textfield():
    if checkbox_var3.get() == 1:
        fixSSDText.config(state="normal")  
        fixSSDConfirmBtn.config(state="normal")  
        fixSSDModifyBtn.config(state="disabled")  
    else:
        fixSSDText.config(state="disabled")  
        fixSSDConfirmBtn.config(state="disabled")  
        fixSSDModifyBtn.config(state="disabled")

def fixSSD_confirm_click():  
    text_content = fixSSDText.get("1.0", "end-1c")
    SSD = text_content
    print("SSD Selected Purpose:", SSD)
    fixSSDText.config(state="disabled")
    fixSSDConfirmBtn.config(state="disabled")
    fixSSDModifyBtn.config(state="normal")

def ssd_enable_editing():
    fixSSDText.config(state="normal")
    fixSSDConfirmBtn.config(state="normal")
    fixSSDModifyBtn.config(state="disabled")

def gpu_toggle_textfield():
    if checkbox_var2.get() == 1:
        fixGPUText.config(state="normal")  
        fixGPUConfirmBtn.config(state="normal")  
        fixGPUModifyBtn.config(state="disabled")  
    else:
        fixGPUText.config(state="disabled")  
        fixGPUConfirmBtn.config(state="disabled")  
        fixGPUModifyBtn.config(state="disabled")

def fixGPU_confirm_click():  
    text_content = fixGPUText.get("1.0", "end-1c")
    GPU = text_content
    print("GPU Selected Purpose:", GPU)
    fixGPUText.config(state="disabled")
    fixGPUConfirmBtn.config(state="disabled")
    fixGPUModifyBtn.config(state="normal")

def gpu_enable_editing():
    fixGPUText.config(state="normal")
    fixGPUConfirmBtn.config(state="normal")
    fixGPUModifyBtn.config(state="disabled")

def cpu_toggle_textfield():
    if checkbox_var1.get() == 1:
        fixCPUText.config(state="normal")  
        fixCPUConfirmBtn.config(state="normal")  
        fixCPUModifyBtn.config(state="disabled")  
    else:
        fixCPUText.config(state="disabled")  
        fixCPUConfirmBtn.config(state="disabled")  
        fixCPUModifyBtn.config(state="disabled")

def fixCPU_confirm_click():  
    text_content = fixCPUText.get("1.0", "end-1c")
    CPU = text_content
    print("CPU Selected Purpose:", CPU)
    fixCPUText.config(state="disabled")
    fixCPUConfirmBtn.config(state="disabled")
    fixCPUModifyBtn.config(state="normal")

def cpu_enable_editing():
    fixCPUText.config(state="normal")
    fixCPUConfirmBtn.config(state="normal")
    fixCPUmodifyBtn.config(state="disabled")

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
    text_content = budgetText.get("1.0", "end-1c")
    userBudget = int(text_content)
    print("Selected:", text_content)
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
#CPU값 입력 
fixLabel = tk.Label(frame2, text="3. Enter a fixed part", font=("Arial", 15), fg="#2B2B2B")
fixLabel.grid(row=3, column=0, padx=(33, 0), pady=(38, 0))

fixCPUText = tk.Text(frame2, height=2, width=25, bd=1, relief="solid")
fixCPUText.grid(row=4, column=0, padx=(45, 0), pady=(20, 10))
default_text = "CPU"
fixCPUText.insert("1.0", default_text)

fixCPUConfirmBtn = tk.Button(frame2, text="Confirm", command=fixCPU_confirm_click,
                              height=1, width=10, bg="#0099BC", fg="#F7FFFF", state="disabled")  
fixCPUConfirmBtn.grid(row=4, column=1, padx=(10, 0), pady=(10, 0))

fixCPUModifyBtn = tk.Button(frame2, text="Modify", command=cpu_enable_editing, height=1,
                             width=10, bg="#0099BC",fg="#F7FFFF", state="disabled")
fixCPUModifyBtn.grid(row=4, column=2, padx=(10, 0), pady=(10, 0))

checkbox_var1 = tk.IntVar()
checkbox1 = tk.Checkbutton(frame2, text="", variable=checkbox_var1, command=cpu_toggle_textfield)
checkbox1.grid(row=4, column=3, padx=(10, 0), pady=(10, 0))

#GPU값 입력
fixGPUText = tk.Text(frame2, height=2, width=25, bd=1, relief="solid")
fixGPUText.grid(row=5, column=0, padx=(45, 0), pady=(20, 10))
default_text = "GPU"
fixGPUText.insert("1.0", default_text)

fixGPUConfirmBtn = tk.Button(frame2, text="Confirm", command=fixGPU_confirm_click,
                              height=1, width=10, bg="#0099BC", fg="#F7FFFF", state="disabled")  
fixGPUConfirmBtn.grid(row=5, column=1, padx=(10, 0), pady=(10, 0))

fixGPUModifyBtn = tk.Button(frame2, text="Modify", command=gpu_enable_editing, height=1,
                             width=10, bg="#0099BC",fg="#F7FFFF", state="disabled")
fixGPUModifyBtn.grid(row=5, column=2, padx=(10, 0), pady=(10, 0))

checkbox_var2 = tk.IntVar()
checkbox2 = tk.Checkbutton(frame2, text="", variable=checkbox_var2, command=gpu_toggle_textfield)
checkbox2.grid(row=5, column=3, padx=(10, 0), pady=(10, 0))


#SSD값 입력
fixSSDText = tk.Text(frame2, height=2, width=25, bd=1, relief="solid")
fixSSDText.grid(row=6, column=0, padx=(45, 0), pady=(20, 10))
default_text = "SSD"
fixSSDText.insert("1.0", default_text)

fixSSDConfirmBtn = tk.Button(frame2, text="Confirm", command=fixSSD_confirm_click,
                              height=1, width=10, bg="#0099BC", fg="#F7FFFF", state="disabled")  
fixSSDConfirmBtn.grid(row=6, column=1, padx=(10, 0), pady=(10, 0))

fixSSDModifyBtn = tk.Button(frame2, text="Modify", command=ssd_enable_editing, height=1,
                             width=10, bg="#0099BC",fg="#F7FFFF", state="disabled")
fixSSDModifyBtn.grid(row=6, column=2, padx=(10, 0), pady=(10, 0))

checkbox_var3 = tk.IntVar()
checkbox3 = tk.Checkbutton(frame2, text="", variable=checkbox_var3, command=ssd_toggle_textfield)
checkbox3.grid(row=6, column=3, padx=(10, 0), pady=(10, 0))


#RAM값 입력
fixRAMText = tk.Text(frame2, height=2, width=25, bd=1, relief="solid")
fixRAMText.grid(row=7, column=0, padx=(45, 0), pady=(20, 10))
default_text = "RAM"
fixRAMText.insert("1.0", default_text)

fixRAMConfirmBtn = tk.Button(frame2, text="Confirm", command=fixRAM_confirm_click,
                              height=1, width=10, bg="#0099BC", fg="#F7FFFF", state="disabled")  
fixRAMConfirmBtn.grid(row=7, column=1, padx=(10, 0), pady=(10, 0))

fixRAMModifyBtn = tk.Button(frame2, text="Modify", command=ram_enable_editing, height=1,
                             width=10, bg="#0099BC",fg="#F7FFFF", state="disabled")
fixRAMModifyBtn.grid(row=7, column=2, padx=(10, 0), pady=(10, 0))

checkbox_var4 = tk.IntVar()
checkbox4 = tk.Checkbutton(frame2, text="", variable=checkbox_var4, command=ram_toggle_textfield)
checkbox4.grid(row=7, column=3, padx=(10, 0), pady=(10, 0))


# 결과 화면
frame3 = tk.Frame(window)
frame3.grid(row=0, column=0, sticky="nsew")


# 버튼 설정
btnToFrame1 = tk.Button(frame3, text="ReStart", padx=10, pady=10, command=lambda: openFrame(frame1), width=15,
                        bg="#0099BC", fg="#F7FFFF")
btnToFrame2 = tk.Button(frame1, text="Start", padx=10, pady=10, command=lambda: openFrame(frame2), width=15,
                        bg="#0099BC", fg="#F7FFFF")
btnToFrame3 = tk.Button(frame2, text="Confirm", padx=10, pady=10, command=lambda: openFrame(frame3), width=10,
                        bg="#0099BC", fg="#F7FFFF")

btnToFrame1.grid(row=0, column=0, pady=10)
btnToFrame2.grid(row=4, column=0, pady=25)
btnToFrame3.grid(row=8, column=0, padx=(50,0), pady=40, columnspan=5)
openFrame(frame1)
window.mainloop()
