import PySimpleGUI as sg
import threading
import json
from itertools import *
import sys
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # print('no path')
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
file = os.path.join('data', 'words.json')
files=resource_path(file)
list1 = []
with open(files) as json_file:
    data = json.load(json_file)
def long_function_thread(ip):
    global data
# print(type(data))
    final = []
    global list1
    list1=[]
    for k in ip.split():
        # for word in k:
            # lis1 = []
        per = permutations(k)
        # for j in per:
        lis1 = [''.join(j) for j in per if ''.join(j) in data]
        lis1=list(dict.fromkeys(lis1))
        # print(lis1)
        # lis1 = [i for i in per if i in data]
        if len(lis1) == 0:
            final.append([k])
        else:
            final.append(lis1)
    # final.sort()
    print('=========================================')
    for i in product(*final):
        print((' '.join(i)))
    print('=========================================')
    print('-Completed-')

def long_function(datam):
    print('=========================================')
    print('-Starting-')
    threading.Thread(target=long_function_thread, args=(datam,), daemon=True).start()

sg.theme('Topanga')

layout = [[sg.Output(size=(60,10))],[sg.Text('Scramble-Unscramble',font=("Helvetica", 25))],
          [sg.Text('Enter your sentence:',font=('Arial',10)),sg.Input(key='data')],
          [sg.Submit('Enter',key='Submit'), sg.Cancel('Exit',key='Exit')]]

# layout = [[sg.Output(size=(60,10))],
#           [sg.Button('Go'), sg.Button('Nothing'), sg.Button('Exit')]  ]

window = sg.Window('Solver', layout)

while True:  # Event Loop
    try:
        event, values = window.read()
        datam = (values['data'])
        datam = datam.lower()
        if event == 'Submit':
            if len(datam) != 0:
                long_function(datam)
        elif event == 'Exit':
            break
        # if event == sg.WIN_CLOSED or event == 'Exit':
        #     break
        # if event == 'Go':
        #     print('About to go to call my long function')
        #     long_function()
        #     print('Long function has returned from starting')
        # elif event == '-THREAD DONE-':
        #     print('Your long operation completed')
    except:
        window.close()
        break
window.close()
