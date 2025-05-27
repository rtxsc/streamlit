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
refresh_count = 111
refresh_count = st_autorefresh(interval=10000, limit=1440, key="app_refresh")
x = datetime.datetime.now()

count = 0
prev_count = 0

# print(df.columns)
st.caption(f"App Refresh Count: {refresh_count} / 1440 as of {x}")
st.subheader(f"GAPC2021 FKE Samarahan Alumni Survey Responses")
st.caption(f"<the not-so-real-time update>")
st.badge("Alumni from 2009 to 2019 (MQA) <|> 2020 to Current (ETAC)", icon=":material/check:", color="green")
st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)
st.divider()

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()
# Print results.
for row in df.itertuples():
    count = count + 1
    st.write(f"[{count}] &nbsp;&nbsp; {row.nama}")
    st.caption(f"{row.batch} | Graduated {row.tahun_graduasi}")
st.badge("New")
st.badge(f"[{count}] &nbsp; {row.nama} &nbsp;&nbsp; {row.batch} | Graduated {row.tahun_graduasi}", color="blue")
last_ts = row.Timestamp
st.caption(f"Latest update: {last_ts}")

st.code(f"Powered by Streamlit + GitHub Workspace")


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

