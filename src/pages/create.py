import streamlit as st
from config import tables

def main():
    st.subheader("Add Entries")
    
    tbles = tables.keys()
    option = st.selectbox('**Tables**', tbles)





if __name__ == "__main__":
    main()
