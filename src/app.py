import streamlit as st
import streamlit.components.v1 as components
import config

def load_css(fname):
    with open(fname) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():    
    st.title("Chess Database")
    st.caption("Manas Chebrolu, PES1UG20CS111")
    components.iframe('http://localhost:8000/', width=500, height=500)

if __name__ == "__main__":
    # load_css("./src/styles/style.css")
    main()
