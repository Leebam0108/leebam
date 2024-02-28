import streamlit as st
from pykrx import stock

#tickers = stock.get_market_ticker_list("20240126", market="KOSPI")

#for ticker in stock.get_market_ticker_list():
#        
#        print(tickers_name)tickers_name = stock.get_market_ticker_name(ticker)

#삼성전자(005930) 주식 정보 조회
#get_stock_info("005930", "20240126", "20240226")
def get_stock_info(stock_cd, st_date, ed_date):
    df= stock.get_market_ohlcv_by_date(st_date, ed_date, stock_cd)


st.title('주식 정보 조회 앱')
stock_cd = st.text_input('주식 코드를 입력하세요   예) 삼성전자 코드 : 005930')
st_date = st.date_input ('조회 시작 날짜를 입력하세요.', value=None)  
ed_date = st.date_input ('조회 종료 날짜를 입력하세요.', value=None)

if st.button('주식 정보 조회'):
    st_date_type = st_date.strftime('%y%m%d')
    ed_date_type = ed_date.strftime('%y%m%d')
    sto_data = get_stock_info(stock_cd, st_date_type, ed_date_type)