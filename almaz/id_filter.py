import openpyxl

Exp_book = openpyxl.open("D:/py/bot/EXP_Бот.xlsx")
sheet_0 = Exp_book.active
column_B = sheet_0['B']


def id_filter(id):
    for i in range(2, len(column_B) + 1):
        if id == sheet_0[i][0].value:
            return True
    return False
