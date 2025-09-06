import pandas as pd
from tkinter import *
from tkinter import filedialog






a = [el for el in range(400,999)]
b =  [el for el in range(1000,2000)]
KAMAZ = a + b
Kontrak1 = [401,402,403,404,405,406,407,408,409,501,502,503,504,505,506,601,602,603,604,605]
Kontrak1_summa = len(Kontrak1)
Kontrakt4 = [435, 436,  438, 439, 440, 441, 442, 443, 446, 447
    , 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462
    , 463, 464, 465, 466, 467, 468, 469, 470, 471, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482,484, 485, 486
, 487, 488, 489,  491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551
, 552, 553, 554, 557, 558, 559,  561, 563, 564, 565,  567, 569, 571, 572, 573, 574, 575, 576, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596
,  598, 599, 600, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645,647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 658, 659, 660, 661, 662, 663, 664, 665,  667, 668, 669, 670,  672, 673, 674
, 675, 676, 677, 678, 679, 681, 682, 683, 684, 685, 686, 687, 688, 689]
Kontrak4_summa = len(Kontrakt4)
print(Kontrak4_summa)
# df1 =  df.iloc[:,0]
# df2 = df.iloc[:,3]
#
# current_job = dict(zip(df1,df2))
#
# for key in current_job:
#     if key in KAMAZ:
#         print(key, current_job[key])

df = []
# def askfile():
#     global df
    
#     df = pd.read_excel('asd.xls', sheet_name=0)

#     label.config(text="Файл выбран")
def open_file():
    filepath = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    # if not filepath:
    #     return
    
    # with open(filepath, "r") as file:
    #     content = file.read()
    #     text_area.delete(1.0, tk.END)
    #     text_area.insert(tk.END, content)
    print(filepath.split("/")[-1][:-4])   
    label.config(text=filepath.split("/")[-1][:-4], font=("Arial", 20))

    global df
    
    df = pd.read_excel(filepath, sheet_name=0)

    df1 =  df.iloc[:,0]
    df2 = df.iloc[:,3]

    current_job = dict(zip(df1,df2))

    for key in current_job:
        if key in KAMAZ:
            print(key, current_job[key])

window = Tk()
w = window.winfo_screenwidth()
h = window.winfo_screenheight()

window.geometry(f"900x600+{w//2-450}+{h//2-300}")
window.title('Камаз - Сводка, всего: ' + str(Kontrak4_summa) +"  " +  str(Kontrak1_summa))

frame_top = LabelFrame(text="Заголовок")
frame_top.pack()
label_1 = Label(frame_top, width=7, height=4, bg='yellow', text="1")
label_1.pack(side=LEFT)
label_2 = Label(frame_top, width=7, height=4, bg='orange', text="2")
label_2.pack(side=LEFT)

frame_bottom = LabelFrame(text="Низ")
frame_bottom.pack()
label_3 = Label(frame_bottom, width=7, height=4, bg='lightgreen', text="3")
label_3.pack(side=LEFT)
label_4 = Label(frame_bottom, width=7, height=4, bg='lightblue', text="4")
label_4.pack(side=LEFT)
frame_bottom = LabelFrame(text="Низ")
frame_bottom.pack()
label_3 = Label(frame_bottom, width=7, height=4, bg='lightgreen', text="3")
label_3.pack(side=LEFT)
label_4 = Label(frame_bottom, width=7, height=4, bg='lightblue', text="4")
label_4.pack(side=LEFT)

Button = Button(frame_top, text="Выберите файл", command=open_file)
Button.pack()
label = Label(frame_top, text="Выберите файл")
label.pack()



window.mainloop()
