import PySimpleGUI as sg
sg.theme('Dark')
def z(a, d):
    try:
        for i in range(0, len(a)):
            d += int(a[i])
        return(str(round(d/len(a), 0)).replace('.0', ''))
    except:
        pass
l = [[sg.Input(key='i', pad=0)], [sg.Text(key='o', pad=0)]]
w = sg.Window('Средний балл', l, font='Arial 16', finalize=True, size=(350, 65), icon="icon.ico")
w['i'].bind('<Return>', 'e')
w['i'].bind('<Shift_R>', 's')
while True:
    try:
        event, values = w.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'i' + 'e':
            w['o'].update('Средний балл: ' + z(values['i'], 0))
        elif event == 'i' + 's':
            w['i'].update('')
    except:
        pass
w.close()