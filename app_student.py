import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd



def run_student_app() :
    st.title('학생이 읽는 책 형태의 데이터 분석')

    st.info('차트보기')
    
    df = pd.read_csv('data/read_book.csv')

    df = df.drop("HLDY_AT" , axis=1)

    df = df.drop('FLAG_NM', axis=1)

    df = df.rename(columns={'BOOK_TY_NM':'책_형태'})

    df = df.rename(columns={'FLAG_VALUE':'연령'})

    df = df.loc[df["연령"].isin(['초등1학년', '초등2학년', '초등3학년', '초등4학년', '초등5학년', '초등6학년', '중등1학년', 
                               '중등2학년', '중등3학년', '고등1학년', '고등2학년', '고등3학년',])]

    if st.checkbox('데이터 프레임 보기') :
        st.dataframe( df )

    else :
        st.text('') 

    df3 = df[df.columns[1]].value_counts()
    
    fig = plt.figure()

    plt.pie(df3, labels= df3.index , autopct="%1.f", startangle=90, wedgeprops={"width":0.7})
    plt.legend()
    plt.title("읽는 책 형태")
    st.pyplot(fig)


