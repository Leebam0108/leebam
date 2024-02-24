import streamlit as st

st.title("개인정보 입력")
st.text("본인의 정보를 입력하고 확인합니다")
st.markdown("streamlit의 기본 위젯을 확인합니다 :balloon:")

user_name = st.text_input(label="성명 : ", value="")
radio_gender = st.radio(label="성별 : ", options=["남자", "여자"])
check_1 = st.checkbox(label="동의합니다", value=False)
memo = st.text_area(label="남기고 싶은말", value="")

if st.button("확인", type="primary"):
    con = st.container()
    con.caption("결과")
    con.write(f"성명 : {str(user_name)}")
    con.write(str(radio_gender))
    con.write(f"동의여부 : {check_1}")
    con.write(f"memo : {str(memo)}")