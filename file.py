import os
import csv

file_path = "num.csv"

year = input("年度：")

os.mkdir(year)
for i in range(1,5):
    os.mkdir(year+'\\第'+str(i)+'四半期')
os.mkdir(year+'\\その他')


with open(file_path, encoding="cp932") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1].find("四半期") != -1:
            i = row[1].find("四半期") -1
            num = row[1][i]
        elif row[1].find("Ｑ") != -1:
            i = row[1].find("Ｑ") -1
            num = row[1][i]
        else:
            num = "0"

        print(num)
        
        if num == "0":
            folder_name = year + "\\その他\\"
        elif num == "１" or num == "1":
            folder_name = year + "\\第1四半期\\"
        elif num == "２" or num == "2":
            folder_name = year + "\\第2四半期\\"
        elif num == "３" or num == "3":
            folder_name = year + "\\第3四半期\\"
        elif num == "４" or num == "4":  
            folder_name = year + "\\第4四半期\\"
        
        folder_name += row[0] + '_' + row[1]
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
