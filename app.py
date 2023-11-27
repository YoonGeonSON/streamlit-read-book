import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

from app_home import run_home_app 
from app_adult import run_adult_app
from app_student import run_student_app





def main() :
    st.title('학생과 성인의 읽는 책의 형태')
    
    menu = ['Home', 'Adult', 'Student']

    choice = st.sidebar.selectbox('카테고리', menu)

    if choice == menu[0] :
        run_home_app()
    elif choice == menu[1] :
        run_adult_app()
    elif choice == menu[2] :
        run_student_app()
    






if __name__ == '__main__' :
    main()