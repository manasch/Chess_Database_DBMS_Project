import streamlit as st
import pandas as pd
from sql.functions import query_execute

query = st.text_area('Custom Query')
try:
    if query:
        res = query_execute(query)
        st.info("Executed")
        if res:
            df = pd.DataFrame(res)
            df.index += 1
            st.dataframe(df, use_container_width=True)
    else:
        st.warning('Empty')
except Exception as e:
    st.warning(e)
