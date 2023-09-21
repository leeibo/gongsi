import time

import requests
import json
from openpyxl import Workbook
from openpyxl.styles import Alignment
from .trans_rmb import money_en_to_cn

data = [{'name': '接口压兰', 'specification': '100', 'kind': 'K型', 'level': 'None', 'weight': '4.10', 'quantity': '1',
         'price': '1', 'rowid': 'row_19', 'unitprice': '4.10', 'amount': '4.10'},
        {'name': '承套', 'specification': '80', 'kind': 'K型', 'level': 'None', 'weight': '13.50', 'quantity': '3',
         'price': '3', 'rowid': 'row_23', 'unitprice': '40.50', 'amount': '121.50'},
        {'name': '法兰盘', 'specification': '40', 'kind': 'None', 'level': 'PN10', 'weight': '1.80', 'quantity': '213',
         'price': '2', 'rowid': 'row_27', 'unitprice': '3.60', 'amount': '766.80'}]


def f_name(s):
    if s is None:
        return ""
    elif s == "None":
        return ""
    else:
        return s


def export_to_excel(table):
    # 创建一个新的工作簿

    wb = Workbook()
    ws = wb.active

    # 写入表头
    header_labels = ["序号", "名称", "规格", "型号", "压力级别", '单位', "数量", "单重", "单价(公斤)", "单价(件)",
                     '合计',
                     "备注"]
    ws.merge_cells(f'A1:L1')
    ws.cell(row=1, column=1, value="安钢永通铸管报价单").alignment = Alignment(horizontal='center')
    for col, label in enumerate(header_labels, start=1):
        ws.cell(row=2, column=col, value=label).alignment = Alignment(horizontal='center')

    # 写入表格数据
    # ws.cell(row=1, column=1, value=f"序号").alignment = Alignment(horizontal='center')
    mrow = len(table)
    mcol = len(header_labels)
    crow = 3
    ans = 0.0
    for row in range(mrow):
        ws.cell(row=crow, column=1, value=f"{row + 1}").alignment = Alignment(horizontal='center')
        ws.cell(row=crow, column=2, value=f"{f_name(table[row]['name'])}").alignment = Alignment(horizontal='center')
        ws.cell(row=crow, column=3, value=f"{f_name(table[row]['specification'])}").alignment = Alignment(
            horizontal='center')
        ws.cell(row=crow, column=4,
                value=f"{f_name(table[row]['kind'])}").alignment = Alignment(
            horizontal='center')
        ws.cell(row=crow, column=5,
                value=f"{f_name(table[row]['level'])}").alignment = Alignment(
            horizontal='center')
        ws.cell(row=crow, column=6, value=f"件").alignment = Alignment(horizontal='center')
        ws.cell(row=crow, column=7, value=f"{f_name(table[row]['quantity'])}").alignment = Alignment(
            horizontal='center')
        ws.cell(row=crow, column=8, value=f"{f_name(table[row]['weight'])}").alignment = Alignment(horizontal='center')
        ws.cell(row=crow, column=9, value=f"{f_name(table[row]['price'])}").alignment = Alignment(horizontal='center')
        ws.cell(row=crow, column=10, value=f"{f_name(table[row]['unitprice'])}").alignment = Alignment(
            horizontal='center')
        ws.cell(row=crow, column=11, value=f"{f_name(table[row]['amount'])}").alignment = Alignment(horizontal='center')
        ws.cell(row=crow, column=12, value=f"").alignment = Alignment(horizontal='center')
        ans += float(table[row]['amount'])
        crow += 1

    # ws.cell(row=crow, column=1, value=f"{crow-1}").alignment = Alignment(horizontal='center')
    # ws.cell(row=crow, column=2, value=f"合计").alignment = Alignment(horizontal='center')

    ws.merge_cells(f'C{crow}:J{crow}')
    ws.cell(row=crow, column=1, value=f"{crow - 2}").alignment = Alignment(horizontal='center')
    ws.cell(row=crow, column=2, value=f"合计").alignment = Alignment(horizontal='center')
    ws.cell(row=crow, column=3, value=f"{money_en_to_cn(ans)}").alignment = Alignment(horizontal='center')
    ws.cell(row=crow, column=mcol - 1, value=f"{ans}").alignment = Alignment(horizontal='center')

    crow += 1

    ws.merge_cells(f'A{crow}:A{crow + 1}')
    ws.cell(row=crow, column=1, value=f"说明").alignment = Alignment(horizontal='center')

    ws.merge_cells(f'B{crow}:L{crow}')
    ws.cell(row=crow, column=2, value="西安永通球墨铸铁管营销有限公司").alignment = Alignment(
        horizontal='right')
    crow += 1

    ws.merge_cells(f'B{crow}:L{crow}')
    ws.cell(row=crow, column=2, value="联系人：李胜利 电话：13484908787 传真：0298569781").alignment = Alignment(
        horizontal='right')
    crow += 1

    for col_idx, col_width in enumerate([10, 15, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, ]):
        ws.column_dimensions[chr(65 + col_idx)].width = col_width

    # 保存工作簿为 Excel 文件
    loca = time.strftime('%Y-%m-%d-%H-%M-%S')
    excel_filename = f'{loca}.xlsx'
    wb.save(excel_filename)
    return excel_filename
    # print(f"表格数据已成功导出到 {excel_filename}")


export_to_excel(data)
