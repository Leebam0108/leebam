from pykrx import stock
import streamlit as st

#tickers = stock.get_market_ticker_list("20240126", market="KOSPI")


#for ticker in stock.get_market_ticker_list():
#        tickers_name = stock.get_market_ticker_name(ticker)
#        print(tickers_name)

def get_stock_info(stock_cd, st_date, ed_date):
    df= stock.get_market_ohlcv_by_date(st_date, ed_date, stock_cd)
    print(df)

#삼성전자(005930) 주식 정보 조회
#get_stock_info("005930", "20240126", "20240226")

st.title('주식 정보 조회 앱')
stock_cd = st.text_input('주식 코드를 입력하세요')
st_date = st.date.input ('조회 시작 날짜를 입력하세요.', value=None)  
ed_date = st.date.input ('조회 종료 날짜를 입력하세요.', value=None)

if st.button('주식 정보 조회'):
    st_date_type = st_date.strftime('%y%m%d')
    ed_date_type = ed_date.strftime('%y%m%d')
    stock_data= get_stock_info(stock_cd, st_date_type, ed_date_type)

    st.write(stock_data)
