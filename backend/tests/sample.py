import pandas as pd

# 샘플 데이터 생성
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['John Doe', 'Jane Smith', 'Chris Johnson', 'Alice Brown', 'Michael Davis', 'Linda Taylor', 'James Miller', 'Susan Wilson', 'Robert Moore', 'Karen Lee'],
    'age': [28, 35, 42, 30, 45, 31, 38, 29, 50, 33],
    'gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'email': [
        'john.doe@example.com', 'jane.smith@example.com', 'chris.j@example.com',
        'alice.brown@example.com', 'michael.d@example.com', 'linda.taylor@example.com',
        'james.miller@example.com', 'susan.w@example.com', 'robert.m@example.com', 'karen.lee@example.com'
    ],
    'join_date': ['2023-01-15', '2021-07-22', '2019-03-05', '2022-05-18', '2020-11-30', '2018-09-17', '2017-04-23', '2023-02-07', '2016-12-12', '2021-06-21'],
    'salary': [55000, 62000, 72000, 49000, 80000, 53000, 71000, 58000, 83000, 60000],
    'department': ['Engineering', 'Marketing', 'Sales', 'Support', 'Management', 'Engineering', 'Marketing', 'Engineering', 'Management', 'Sales']
}

# 데이터프레임으로 변환
df = pd.DataFrame(data)

# CSV 파일로 저장
df.to_csv('sample_data.csv', index=False)

# Excel 파일로 저장
df.to_excel('sample_data.xlsx', index=False)