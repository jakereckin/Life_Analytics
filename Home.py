import streamlit as st
import sys
import time
import sys
import os
import datetime as dt
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))
from pages.functions import utils as ut

today = dt.datetime.today().strftime('%m/%d/%Y')
st.set_page_config('Home')
st.header(f'Today is: {today}')
#conn = ut.create_db()
#ut.drop_life(conn)
#ut.create_values(conn)