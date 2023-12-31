attr = [["姓名"],
        ["学号"],
        ["性别"],
        ["专业"],
        ["入学年月"],
        ["已获得", "毕业时最低应获学分/已获得学分"],
        ["学院"],
        ["毕业年月"]]
score_titles = ["学习时间", "课程名称", "备注", "学分",
                "成绩", "课程性质"]
search_score_title = "课程名称"

rank2score = {
    "优": "90",
    "良": "80",
    "中": "70",
    "及格": "60",
    "免修": "80",
    "通过": "60",
    "缺考": "0"
}


header = ["学号", "姓名", "性别", "学院", "专业", "已获得", "入学年月", "毕业年月", "平均分"]


dir_name = "./file/"


def calculate_condition(lesson):
    '''
    接收一个课程字典，判断是否计算这个成绩
    '''
    if lesson["课程性质"] != "":
        return True
    return False
