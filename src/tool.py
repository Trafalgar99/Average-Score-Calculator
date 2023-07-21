import os
import config
import os
import win32com.client


# 查找属性
def find_str(str, attr):
    '''
    判断attr中的字符串是否在str中出现过，
    如果出现过，返回这个attr中的字符串
    '''
    for k in attr:
        for c in k:
            if c in str:
                return (True, k[0])
    return (False, "")


def find_attr(sheet, attr):
    info = {}
    for row in sheet.iter_rows():
        for cell in row:
            if cell.value == None:
                continue
            strs = cell.value.split('：')
            strs = [''.join(s.split()) for s in strs]
            res, k = find_str(strs, attr)
            if res == True:
                s = cell.value.split('：')[-1]
                info[k] = s
    return info


def get_file_list(dir_name):
    file_list = []
    for root, _, files in os.walk(dir_name):
        for file in files:
            if file.endswith(".xlsx"):
                file_list.append(root + file)
    return file_list


def find_cell(sheet, str):
    '''
    查找哪几个cell的value完全等于str
    返回坐标集
    '''
    res = []
    for row in sheet.iter_rows():
        for cell in row:
            if cell.value == str:
                res.append((cell.row, cell.column))
    return res


def find_score_points():
    points = find_cell(config.search_score_title)
    points = [(x + 1, y - 1) for (x, y) in points]
    return points


def get_lessons_dict(sheet, sites):
    '''
        获取所有课程信息，传入所有的起始点信息
        返回课程字典
    '''
    from itertools import zip_longest
    lessons = []
    for (x, y) in sites:
        nx = x
        for row in sheet.iter_rows(min_row=nx):
            if row[y].value == "" or row[y].value == None:
                break
            ny = y
            lesson_info = []
            for i in range(0, len(config.score_titles) + 1):
                if sheet.cell(nx, ny).value != None:
                    lesson_info.append(sheet.cell(nx, ny).value)
                ny += 1
            lessons.append(
                dict(zip_longest(config.score_titles, lesson_info, fillvalue="")))
            nx += 1
    return lessons


# 计算平均分
def calculate_average(name, lessons_dict, condition):
    '''
    计算平均分，传入成绩字典,和某个课程应该满足的条件
    返回平均值
    '''
    sum = 0
    ratio = 0
    for lesson in lessons_dict:
        if condition(lesson) == True:
            n = 0
            try:  # 判定时候是非数字成绩
                n = float(lesson["成绩"])
            except ValueError:
                # print(name)
                n = float(config.rank2score[lesson["成绩"]])
            sum += n * float(lesson["学分"])
            ratio += float(lesson["学分"])
    print(f'{name}-计算完成')
    return round(sum / ratio, 2)


# 文件格式转换
def one_xls2xlsx(file_name, excel):
    wb = excel.Workbooks.Open(file_name)
    new_file = os.path.splitext(file_name)[0] + ".xlsx"
    wb.SaveAs(new_file, FileFormat=51)
    os.remove(file_name)


def multi_xls2xlsx(dir_name):
    excel = win32com.client.Dispatch("Excel.Application")
    for root, _, files in os.walk(dir_name):
        for file in files:
            if file.endswith(".xls"):
                file_path = os.path.abspath(root + file)
                one_xls2xlsx(file_path, excel)
                print(f"finish {file}")
    excel.Quit()
