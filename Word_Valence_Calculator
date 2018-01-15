from openpyxl import load_workbook
file = '/Volumes/MY DATA/Users/Sarah/Documents/LIDo rotation 1/Review extrapolation code/Anew_extended.xlsx'

wb = load_workbook(file, read_only=True)

ws = wb['Ratings_Warriner_et_al']

# Read the cell values into a list of lists
negative = []
concern = []
threat = []
neutral = []

for i in range(1,13916):
    V = ws.cell(row=i, column=3)
    A = ws.cell(row=i, column=6)
    D = ws.cell(row=i, column=9)
    name = ws.cell(row=i, column=2)
    if V.value < 5 and A.value > 5 and D.value < 5:
        negative.append(name.value)
    if V.value < 4 and A.value in range(3,5) and D.value < 4:
        concern.append(name.value)
    if V.value < 4 and A.value > 4 and D.value in range(3,5):
        threat.append(name.value)
    if V.value in range(4,6) and A.value < 5 and D.value > 5:
        neutral.append(name.value)




import xlsxwriter

workbook = xlsxwriter.Workbook('Grouping of words.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0
for name in (negative):
    worksheet.write(row, col, name)
for name1 in (concern):
    worksheet.write(row, col+1, name1)
for name2 in (threat):
    worksheet.write(row, col+2, name2)
for name3 in (neutral):
    worksheet.write(row, col+3, name3)
workbook.close()

