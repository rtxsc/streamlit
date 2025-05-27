import streamlit as st
import numpy as np
import pandas as pd

import streamlit as st
from streamlit_gsheets import GSheetsConnection
from streamlit_autorefresh import st_autorefresh
import datetime


# /workspaces/streamlit/streamlit_app.py
# /workspaces/streamlit/.streamlit
# /workspaces/streamlit/.streamlit/secrets.toml

# Run the autorefresh about every 60000 milliseconds (1 minute) and stop
# after it's been refreshed 1440 minutes (1 day)
refresh_count = st_autorefresh(interval=60000, limit=1440, key="app_refresh")
x = datetime.datetime.now()
# print(x)

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
count = 0
df = conn.read()
# print(df.columns)
st.write(f"App Refresh Count: {refresh_count} / 1440 as of {x}")
st.write(f"FKE Samarahan Alumni Survey Responses (the not-so-real-time update)")
st.write(f"Alumni from 2009 to 2019 (MQA)")
st.write(f"Alumni from 2020 to Current (ETAC)")
st.write(f"Powered by Streamlit + GitHub Workspace")
st.write(f"---------------------")
# Print results.
for row in df.itertuples():
    count = count + 1
    # st.write(f"Count:",{count})
    st.write(f"{count} : {row.nama} | {row.batch} / Grade: {row.tahun_graduasi} ")

last_ts = row.Timestamp
st.write(f"Latest update: {last_ts}")


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

