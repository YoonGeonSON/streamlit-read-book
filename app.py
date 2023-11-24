import streamlit as st

from app_home import run_home_app 




def main() :
    st.title('초,중,고별 읽는 책의 형태!!!')
    
    menu = ['Home', 'Elementary', 'Middle', 'High']

    choice = st.sidebar.selectbox('학년선택', menu)

    if choice == menu[0] :
        run_home_app()
    elif choice == menu[1] :
        pass
    elif choice == menu[2] :
        pass
    elif choice == menu[3] :
        pass






if __name__ == '__main__' :
    main()