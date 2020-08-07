import xlsxwriter

workbook = xlsxwriter.Workbook("user.xlsx")
worksheet = workbook.add_worksheet()

print("login[0] or sign up[1]")
lsu = input(">> ")
if lsu ==  0:
    print("login")
    print("email")
    eml = input(">> ")
    print("passworc")
    pwl = input(">> ")
    print("re enter password")
    rpwl = input(">> ")
    if pwl == rpwl:
        print("wellcome")
        user = (
            [eml, pwl]
        ) 
    elif lsu == 1:
        print("sign up")
        print("email")
        emsu = input(">> ")
        print("password")
        pwsu = input(">> ")
        print("re enter password")
        rpwsu = input(">> ")

row = 0
col = 0

for eml, pwl in (user):
    worksheet.write(row, col, eml)
    worksheet.write(row, col + 1, pwl)
    row += 1

worksheet.write(row, 0, 'total')
worksheet.write(row, 1, 'sum(B1 : B4)')

workbook.close()


        