import streamlit as st


def run_home_app () :
    st.subheader('환영합니다.')
    st.text('이 앱은 초,중,고별 읽는 책의 형태에 관한 내용입니다.')
    
    st.text('AWS에 배포까지 된 앱입니다.')
    
    img_url = 'https://cdn.kosinnews.com/news/photo/202110/22491_24115_2556.jpg'
    
    st.image(img_url)





