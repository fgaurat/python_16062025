import streamlit as st
from CustomerDAO import CustomerDAO

def main():
    st.set_page_config(layout="wide")
    dao = CustomerDAO('../customers.db')
    customers = dao.findAll()

    st.write("# Hello")
    name = st.text_input("Name", "")
    if st.button('Say Hello'):
        st.write("Hello", name)
    
    st.table(customers)

if __name__=='__main__':
    main()
