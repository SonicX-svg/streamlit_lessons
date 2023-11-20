import streamlit as st
import pandas as pd
st.write('Hello, *word!* :sunglasess:')
st.header(1234, divider='rainbow')
df = pd.DataFrame({'first section' : (1,2,3,4,5),
      'second section' : (1,2,8,90,0)})
st.write(df)
st.write('down', df, 'up')
