import streamlit as st
import pandas as pd


def run_elementary_app() :
    st.subheader('데이터 분석')
    st.text('전체 데이터 프레임 확인하기')
    df = pd.read_csv('data/read_book.csv')
    st.dataframe(df)
    



