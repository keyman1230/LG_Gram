import pandas as pd

# 다중 인덱스 열을 가진 데이터프레임 생성
data = {
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [30, 25, 35],
    '직업': ['학생', '회사원', '자영업']
}

df = pd.DataFrame(data)

add = df.columns[0] # 반복자로 쓸 칼럼
new_columns = [(add, i) for i in df.columns]

# 다중 인덱스 열 설정
df.columns = pd.MultiIndex.from_tuples(new_columns)

# print(df)
df.to_excel("./test.xlsx")