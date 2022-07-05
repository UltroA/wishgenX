import func
import xlsxwriter

row = 0
workbook = xlsxwriter.Workbook('Wishlist.xlsx')
worksheet = workbook.add_worksheet()
row = func.addtobook([('Название', 'Ссылка', 'Цена')], worksheet, row)
while(input() != 'x'):
    row = func.addtobook([(input('Название: '), input('Ссылка: '), input('Цена: '))], worksheet, row)
workbook.close()
