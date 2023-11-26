import streamlit as st
import plotly.express as px
import altair as alt

from app_home import run_home_app 
from app_adult import run_adult_app
from app_student import run_student_app




def main() :
    st.title('성인과 학생의 읽는 책의 형태')
    
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