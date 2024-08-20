import pandas as pd
import sqlite3

# CSV 파일 읽기
csv_file = './data/daily_top10_articles.csv'
df = pd.read_csv(csv_file)

# 날짜 형식 변환 (CSV 파일의 날짜 형식에 맞게 조정 필요)
df['ranking_date'] = pd.to_datetime(df['ranking_date'], format='%Y%m%d').dt.date

# 데이터베이스 연결
conn = sqlite3.connect('./../crawling.sqlite3')

# 데이터베이스에 테이블 생성 (테이블이 이미 존재한다면 이 부분은 생략해도 됩니다)
cursor = conn.cursor()
sql = '''
CREATE TABLE IF NOT EXISTS article(
    articleCd INTEGER PRIMARY KEY AUTOINCREMENT,
    news_organization_name TEXT,
    ranking_date DATE,
    ranking INTEGER,
    article_title TEXT,
    reporter_name TEXT,
    article_section TEXT,
    monthly_article_count INTEGER
)
'''
cursor.execute(sql)

# DataFrame을 데이터베이스에 추가
df.to_sql('article', conn, if_exists='append', index=False)

# 커밋 및 연결 종료
conn.commit()
conn.close()

print('데이터베이스 파일에 데이터 추가를 성공하였습니다.')
