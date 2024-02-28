import streamlit as st

# 타이틀 적용 예시
st.title('타이틀 입력합니다')

# 특수 이모티콘 삽입 예시
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title('스마일 :grinning:  :grinning: :grinning: :grinning:')

# Header 적용
st.header('문서의 소개 내용을 헤더에 입력합니다  :sparkles:')

# Subheader 적용
st.subheader('subheader를 입력합니다.', divider='rainbow')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')


# 코드 표시
sample_code = '''
def function():
    print('hello, world')
'''
st.code(sample_code, language="python")

# 일반 텍스트
st.text('문서의 일반적인 텍스트를 입력합니다.')

# 마크다운 문법 지원
st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')
# 컬러코드: blue, green, orange, red, violet
st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼트체로 설정할 수 있습니다.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] 와 같이 latex 문법의 수식 표현도 가능합니다 :pencil:")

# latex를 이용해서 수학기호를 사용합니다.
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')