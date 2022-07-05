import func
import xlsxwriter


row = 0
workbook = xlsxwriter.Workbook('Суммы.xlsx')
worksheet = workbook.add_worksheet()
data = [('Название', 'Ссылка', 'Цена')]
row = func.addtobook(data, worksheet, row)
row = func.addtobook([('Minecraft', 'minecraft.org', '2500')], worksheet, row)
row = func.addtobook([('Laptop', 'youtube.com', '134000')], worksheet, row)

workbook.close()
