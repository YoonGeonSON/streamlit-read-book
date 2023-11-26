import streamlit as st

import plotly.express as px
import pandas as pd
import altair as alt


def run_student_app() :
    st.title('학생 데이터 분석')

    st.info('차트보기')
    
    df = pd.read_csv('data/read_book.csv')

    df = df.drop("HLDY_AT" , axis=1)

    df = df.drop('FLAG_NM', axis=1)

    df = df.rename(columns={'BOOK_TY_NM':'책_형태'})

    df = df.rename(columns={'FLAG_VALUE':'연령'})

    df = df.tail(83)

    if st.checkbox('데이터 프레임 보기') :
        st.dataframe( df )

    else :
        st.text('') 


