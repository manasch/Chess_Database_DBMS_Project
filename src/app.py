import streamlit as st
import streamlit.components.v1 as components

from config import return_html_string, start

def main():    
    st.title("Chess Database")
    st.caption("Manas Chebrolu, PES1UG20CS111")

    components.html(return_html_string(start), height=500, width=500)

if __name__ == "__main__":
    main()
