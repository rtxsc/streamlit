import streamlit as st
import numpy as np
import pandas as pd

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# /workspaces/streamlit/streamlit_app.py
# /workspaces/streamlit/.streamlit
# /workspaces/streamlit/.streamlit/secrets.toml

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()
# print(df.columns)


# Print results.
for row in df.itertuples():
    st.write(f"Alu: {row.nama} - Email: {row.emel_alumni} - Grade: {row.tahun_graduasi} ")

# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# chart_data = pd.DataFrame(
#      np.random.randn(20, 4),
#      columns=['a', 'b', 'c', 'd'])

# st.line_chart(chart_data)


# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))

# st.dataframe(dataframe.style.highlight_max(axis=0))

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

