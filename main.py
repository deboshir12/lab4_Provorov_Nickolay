from inspect import EndOfBlock
import tkinter as tk
from tkinter import PhotoImage
import random
import pygame


def close():
    window.destroy()
    
    
def calc():
    
    s = arg_B.get()
    if len(s)<6 or len(s)>6:
        lbl_result.config(text = 'Invalid values')
        #EndOfBlock()
    else:
        try:
            text_tk = int(s)
            
            m_int= []
            
            for i in s:
                m_int.append(int(i))
            
            sum_code = str(int(s[:3:])+ int(s[3::]))
            if len(sum_code)<4:
                sum_code = '0'*(4-len(sum_code))+ sum_code
                
            a,b,c,d = chr(random.randint(65,90)),chr(random.randint(65,90)),\
                chr(random.randint(65,90)),chr(random.randint(65,90))
            str_res = str(m_int[3]) + str(m_int[4]) + str(m_int[5]) + a + b +\
                ' - ' + str(m_int[0]) + str(m_int[1]) + str(m_int[2]) + c + d \
                    + ' ' + sum_code
            print(text_tk,len(s),m_int,sum_code)
            lbl_result.config(text = str_res)
        except:
            lbl_result.config(text = 'Invalid values')

window = tk.Tk()
window.title('Title')
window.geometry('450x320')

frame = tk.Frame(window)
frame.place(relx = 0.5, rely = 0.5, anchor='center')

lbl_B = tk.Label(frame, text= 'GENERATE CODE', font=('Arial', 15))
lbl_B.grid(column = 1,row = 0, padx = 10, pady = 15)
arg_B = tk.Entry(frame, width = 15)
arg_B.grid(column=1, row = 1, padx = 10, pady = 15)
arg_B.insert(0,'')

lbl_roots = tk.Label(frame, text = 'RESULT: ', font=('Arial', 15))
lbl_roots.grid(column=0, row = 2)
lbl_value = tk.Label(frame, text = 'Enter 6 numbers.', font = ('Arial',15))
lbl_value.grid(column = 0, row = 1)
lbl_result = tk.Label(frame, text = '', font = ('Arial',15))
lbl_result.grid(column = 1, row = 2)

btn_calc = tk.Button(frame, text='Generate', font= ('Arial',15), command = calc)
btn_calc.grid(column=0, row = 3)
btn_exit = tk.Button(frame, text='Exit', font= ('Arial',15), command = close)
btn_exit.grid(column=2, row = 3)


frameCnt = 3
frames = [PhotoImage(file='111.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    shot = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=shot)
    frame.after(100, update, ind)
label = tk.Label(frame)
label.grid(column=0, row = 0)
frame.after(0, update, 0)

pygame.init()
song = pygame.mixer.Sound('55.wav')
clock = pygame.time.Clock()
song.play()
    

window.mainloop()
