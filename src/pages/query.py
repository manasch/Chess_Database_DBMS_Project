import streamlit as st
from sql.functions import query_execute

query = st.text_area('Custom Query')
res = query_execute(query)
st.write(res)
