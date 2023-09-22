import pandas as pd
import re  # 정규 표현식 모듈을 추가합니다.

# 엑셀 파일 "A"와 "B" 불러오기 (engine="openpyxl"로 설정)
df_a = pd.read_excel(r"C:\\Users\\HnS\\Desktop\\z230921.homeservice-main\\file1.xlsx", engine="openpyxl")
df_b = pd.read_excel(r"C:\\Users\\HnS\\Desktop\\z230921.homeservice-main\\file2.xlsx", engine="openpyxl")

# 위치 정보를 처리하는 함수 정의
def extract_info(location):
    # 행과 열 정보를 추출합니다.
    row_info, col_info = location
    # 행 정보를 문자열로 변환합니다.
    row_info = str(row_info)
    # 열 정보를 문자열로 변환합니다.
    col_info = str(col_info)
    # 행 정보에서 숫자 부분을 추출합니다.
    row_match = re.search(r'\d+', row_info)
    row = int(row_match.group()) if row_match else None
    # 열 정보에서 영어 부분을 추출합니다.
    col_match = re.search(r'[A-Za-z]+', col_info)
    col = col_match.group() if col_match else None
    return row, col

# 차이를 저장할 데이터프레임 초기화
diff_df = pd.DataFrame(columns=['행', '열', '파일 A의 값', '파일 B의 값'])

# 두 데이터프레임을 비교하여 일치하지 않는 부분 찾기
for location in df_a.columns:
    for idx, row in df_a.iterrows():
        val_a = row[location]
        val_b = df_b.iloc[idx][location]
        if val_a != val_b:
            row, col = extract_info((idx, location))
            diff_df = diff_df.append({'행': row, '열': col, '파일 A의 값': val_a, '파일 B의 값': val_b}, ignore_index=True)

# 차이가 있는 데이터프레임을 출력
print(diff_df)