import streamlit as st
import pandas as pd
import numpy as np
import datetime

now = datetime.datetime.now().strftime("%y/%m/%d") # 현재 날짜를 now에 입력
st.title("전세계 날씨, 기온 및 습도 정보")          # 페이지 타이틀 출력
st.subheader("Date:{}".format(now))                # 현재 날짜를 subheader로 출력
st.markdown("---")                                 # 구분선 생성

# 4.두 개의 Column 생성
col1, col2 = st.columns([3, 7])                    # 두개의 Column(열) 생성
                                                   # 각 Column은 3:7의 넓이로 생성
# 5.국가 SelectBox와 기상 정보
with col1:   
    # 데이터셋 호출:국가별 위/경도, 날씨 정보 포함                                      
    raw = pd.read_csv("./data/세계의 날씨.csv")
    df = raw.copy()
    print(df)
    country_name = df["Country"].to_list()   # 국가명 Column을 리스트로 변경, country_name에 저장
    
    # Selectbox 위젯 생성
    country = st.selectbox(label = "국가이름 선택", # 위젯 상단의 레이블 설정
                           options = country_name,  # 선택 상자에 나열되는 국가명 설정
                           index = 121)             # 초기 출력되는 국가명의 인덱스 설정
    
    # Selectbox에 선정한 국가명에 해당하는 행 추출
    selected_row = df[df["Country"] == country]   
    
    lat = float(selected_row.iloc[0, 5])  # 추출한 행에서 위도를 인덱싱하여 lat에 입력
    lon = float(selected_row.iloc[0, 6])  # 추출한 행에서 경도를 인덱싱하여 lon에 입력
    sky = str(selected_row.iloc[0, 7])    # 추출한 행에서 날씨를 인덱싱하여 sky에 입력
    temp = float(selected_row.iloc[0, 8]) # 추출한 행에서 온도를 인덱싱하여 temp에 입력
    humi = float(selected_row.iloc[0, 9]) # 추출한 행에서 습도를 인덱싱하여 humi에 입력

    st.markdown("---")                    # 경계선 출력
    st.markdown("{} 날씨 정보".format(country)) # OOO(국가명) 날씨 정보 출력
    st.write("날씨 : {}".format(sky))           # 날씨 정보 출력
    st.write("기온 : {:0.1f}℃".format(temp))    # 온도 정보 출력
    st.write("습도 : {:0.1f}%".format(humi))    # 습도 정보 출력
    

# 6.세계지도에 선택한 국가 표시
with col2:
    # 선택한 국가명의 lat(위도), lon(경도)로 데이터 프레임 map_data생성
    map_data = pd.DataFrame({"lat":[lat],       
                             "lon":[lon]})
    # map_data로 지도 생성
    st.map(data = map_data, zoom = 1.5, color='#0044ff') # zoom사이즈로 지도 크기 조절