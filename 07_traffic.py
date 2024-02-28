import streamlit as st
import pandas as pd
import numpy as np
import datetime

now = datetime.datetime.now().strftime("%y/%m/%d") # 현재 날짜를 now에 입력
st.title("전국 교통사고 현황")          
st.markdown("---")                                 # 구분선 생성

raw = pd.read_csv("./data/시군구별 교통사고 통계.csv")
df = raw.copy()
city_name= df["시도"].to_list()

# Selectbox 위젯 생성
sel_city = st.selectbox(label = "시도선택", # 위젯 상단의 레이블 설정
                           options = set(city_name), index=11)

dong = df.loc[(df['시도'] == sel_city), '시군구']
# Selectbox 위젯 생성
#sel_dong = st.selectbox(label = "시군구선택", # 위젯 상단의 레이블 설정
#                           options = set(dong))


chart_data = pd.DataFrame(df.loc[(df['시도'] == sel_city), '시군구':])
ydata = pd.DataFrame(df.loc[(df['시도'] == sel_city), '사고건수':])

st.write(chart_data)

st.line_chart(chart_data, x='시군구', y=ydata)