

import random
from datetime import datetime, timedelta


def generate_work_data():
    data = []
    w_id = 2000  # 初始编号，避免与已有的编号冲突

    for year in range(2022, 2024):
        for month in range(1, 13):
            for _ in range(10):
                w_id += 1
                work_name = random.choice(
                    ['党建工作', '招生工作', '教学工作', '财务工作', '科研工作', '学生工作', '后勤工作'])
                sub_work = random.choice(['领导班子与组织建设工作', '党风廉政建设工作'])
                work_type = random.randint(1, 3)
                w_department = str(random.randint(1, 10))
                work_content = f'{random.randint(1, 10)}.{random.choice(["召开院党委会","专题研究部署工作", "入党积极分子确定","庆祝建党系列活动","梳理年度任务分解清单中的各项任务落实情况","召开会议专题研究党风廉政建设","召开院党委会、院党政联席会","各支部书记讲党课","党员红色基地教育实践活动"])}'
                work_mouth = month
                work_year = year
                create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                creater = '1'
                deleted = 0
                status = 1
                finish_status = random.choice([0, 2])
                note = "NULL"

                data.append((w_id, work_name, sub_work, work_type, w_department, work_content,
                             work_mouth, work_year, create_time, creater, "NULL", "NULL", deleted, "NULL",
                             status, finish_status, note))

    return data


def generate_insert_sql(data):
    sql_statements = []
    for row in data:
        sql = format(row) + ','
        sql_statements.append(sql)

    return sql_statements


if __name__ == "__main__":
    work_data = generate_work_data()
    sql_queries = generate_insert_sql(work_data)

    for query in sql_queries:
        print(query)
