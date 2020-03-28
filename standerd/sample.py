 1　import pathlib  # 標準ライブラリ
 2　import openpyxl # 外部ライブラリ
 3　import csv      # 標準ライブラリ
 4
 5
 6　lwb = openpyxl.Workbook() # 売上一覧のワークブックをlwbとして作成
 7　lsh = lwb.active 　　　　# デフォルトで作成されるワークシートを選択
 8　list_row = 1
 9　path = pathlib.Path("..￥data￥sales")　　　 # 相対パス指定
10　for pass_obj in path.iterdir()：
11　    if pass_obj.match("*.xlsx")：
12　        wb = openpyxl.load_workbook(pass_obj)
13    　    for sh in wb：
14　            for dt_row in range(9,19)：
15　                if sh.cell(dt_row, 2).value ！= None：
16　                    lsh.cell(list_row, 1).value = sh.cell(2, 7).value
17　                    lsh.cell(list_row, 2).value = sh.cell(3, 7).value
18　                    lsh.cell(list_row, 3).value = sh.cell(4, 3).value
19　                    lsh.cell(list_row, 4).value = sh.cell(7, 8).value
20　                    lsh.cell(list_row, 5).value = sh.cell(dt_row, 1).value
21　                    lsh.cell(list_row, 6).value = sh.cell(dt_row, 2).value
22　                    lsh.cell(list_row, 7).value = sh.cell(dt_row, 3).value
23　                    lsh.cell(list_row, 8).value = sh.cell(dt_row, 4).value
24　                    lsh.cell(list_row, 9).value = sh.cell(dt_row, 5).value
25　                    lsh.cell(list_row, 10).value = sh.cell(dt_row, 4).value * ￥
26　                    sh.cell(dt_row, 5).value
27　                    lsh.cell(list_row, 11).value = sh.cell(dt_row, 7).value
28　                    list_row += 1
29
30　with open("..￥data￥sales￥salesList.csv","w",encoding="utf_8_sig") as fp：
31　    writer = csv.writer(fp,lineterminator="￥n")
32　    for row in lsh.rows：
33　        writer.writerow([col.value for col inrow]) 　#リスト内包表記