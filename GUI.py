import func
import xlsxwriter
import PySimpleGUI as sg

row = 0
workbook = xlsxwriter.Workbook('Wishlist.xlsx')
worksheet = workbook.add_worksheet()
row = func.addtobook([('Название', 'Ссылка', 'Цена')], worksheet, row)
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Для добавления строки в wishlist нажмите Добавить')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Добавить'), sg.Button('Закрыть')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Закрыть': # if user closes window or clicks cancel
        break
    links = (values[0].split()[0], values[0].split()[1], values[0].split()[2])
    row = func.addtobook([links], worksheet, row)

window.close()
# close
# while(input() != 'x'):
#     row = func.addtobook([(input('Название: '), input('Ссылка: '), input('Цена: '))], worksheet, row)
workbook.close()
