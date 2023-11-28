import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

def run_adult_app() :
    st.title('성인이 읽는 책 형태의 데이터 분석')

    st.info('차트보기')
    
    df = pd.read_csv('data/read_book.csv')

    df = df.drop("HLDY_AT" , axis=1)

    df = df.drop('FLAG_NM', axis=1)

    df = df.rename(columns={'BOOK_TY_NM':'책_형태'})

    df = df.rename(columns={'FLAG_VALUE':'연령'})

    df = df.loc[df["연령"].isin(['19-29세', '30-39세', '40-49세','50-59세', '60세이상'])]

    

    if st.checkbox('데이터 프레임 보기') :
        st.dataframe( df )

    else :
        st.text('')    

    df = df[df.columns[1]].value_counts()
    
    fig = plt.figure()
    

    plt.pie(df, labels= df.index , autopct="%1.f", startangle=90, wedgeprops={"width":0.7})
    plt.legend()
    plt.title("읽는 책 형태")
    st.pyplot(fig)
 
    
   
    

                         

   


    



    
        
    
    




