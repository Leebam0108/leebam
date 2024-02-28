import streamlit as st

st.title('추억이 쌓이는 미니앨범')
st.markdown('**:blue[추억의] 사진**을 만들어 보아요 :sunglasses:')

album = [
    {
        "제목" : "2017년 우리 셋만.....",
        "설명" : "스케일에 감탄 한 호텔  ",
        "image_url" : "./images/img1.jpg"
    },
    {
        "제목" : "2023년 마지막 해",
        "설명" : "2024년 행복의 기도를....",
        "image_url" : "./images/img5.jpg"
    },
    {
        "제목" : "연말명동",
        "설명" : "연말에만 볼수 있는 곳 ",
        "image_url" : "./images/img3.jpg"
    },
    {
        "제목" : "절친과 함께",
        "설명" : "행복했던 여행",
        "image_url" : "./images/img4.jpg"
    },
    {
        "제목" : "힐링 나무",
        "설명" : "비자나무 보며 힐링",
        "image_url" : "./images/img2.jpg"
    },
    {
        "제목" : "우리 셋째",
        "설명" : "4살 축하해",
        "image_url" : "./images/img6.jpg"
    }
]

cols = st.columns(3)
album_idx=0
for i in range(len(album)):
    with cols[i % 3]:
        album_idx = album[i]
        with st.expander(label=album_idx["제목"], expanded=True):
            st.image(album_idx["image_url"])
            st.text(album_idx["설명"])
