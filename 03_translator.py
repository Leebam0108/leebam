import streamlit as st
import googletrans

,
    {
        "제목" : "비자나무",
        "설명" : "비자나무 보며 힐링",
        "image_url" : "https://github.com/Leebam0108/leebam/blob/main/images/img2.jpg"
    },
    {
        "제목" : "절친과 함께",
        "설명" : "그냥 떠난 여행",
        "image_url" : "https://github.com/Leebam0108/leebam/blob/main/images/img3.jpg"
    },
    {
        "제목" : "연말명동",
        "설명" : "연말에만 볼수 있는 곳 ",
        "image_url" : "https://github.com/Leebam0108/leebam/blob/main/images/img4.jpg"
    },
    {
        "제목" : "2023년 마지막 해",
        "설명" : "2024년 행복의 기도를....",
        "image_url" : "https://github.com/Leebam0108/leebam/blob/main/images/img5.jpg"
    },
    {
        "제목" : "우리 셋째",
        "설명" : "4살 축하해",
        "image_url" : "https://github.com/Leebam0108/leebam/blob/main/images/img6.jpg"
    }

def chk_lang(a):
    if lang_type == '영어':
        lang = 'en'
    elif lang_type == '일어':
        lang = 'ja'  
    elif lang_type == '중국어':
        lang = 'zh-CN'
    elif lang_type == '프랑스어':
        lang = 'fr'
    else:
        lang = 'en'

    return lang


st.title('밤이 번역기')
st.text("구글 번역기를 이용하여 나만의 번력기를 만들기")
st.markdown(":rosette::rosette::rosette::rosette::rosette:")
            
trans_str = st.text_input(label="번역할 글 : ", value="")
lang_type = chk_lang(st.selectbox(':blue[번역할 언어를 선택하세요]', ('영어', '일어', '중국어', '프랑스어'), placeholder='영어'))


trans = googletrans.Translator()

if not trans_str:
    if st.button("번역하기"):
        src = trans.detect(trans_str).lang
        trans_str=src

        result=trans.translate(trans_str, dest=lang_type, src='auto')

st.success(result.text)

