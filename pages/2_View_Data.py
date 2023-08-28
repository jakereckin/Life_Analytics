import streamlit as st
import datetime as dt
import sys
import time
import sys
import os
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))
from functions import utils as ut

today = dt.datetime.today().strftime('%m/%d/%Y')

st.set_page_config('View Data')
st.sidebar.header('View Data')

conn = ut.create_db()
my_data = ut.select_today(conn)
st.dataframe(data=my_data, use_container_width=True)