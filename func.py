def addtobook(data, worksheet, row):
    for _, (item, link, price) in enumerate(data):
        worksheet.write(row, 0, item)
        worksheet.write(row, 1, link)
        worksheet.write(row, 2, price)
    row += 1
    return row