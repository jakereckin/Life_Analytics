import streamlit as st
import datetime as dt
import sys
import time
import sys
import pandas as pd
import os
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))
from functions import utils as ut

today = dt.datetime.today().strftime('%m/%d/%Y')
my_attribs = ['Heart Rate',
              'HRV',
              'Pages Read',
              'Journal',
              'Rosary',
              'Meditate Minutes',
              'Brush Teeth',
              'Water (oz)',
              'Shower',
              'Planks',
              'Pushups',
              'Other Workout',
              'Time in Bed',
              'Time awake',
              'Caffeine',
              'Cardio Min',
              'Bible',
              'Physical Readiness',
              'Mental Readiness',
              'Happiness Morning',
              'Happiness Night'
]

conn = ut.create_db()
st.set_page_config('Input Data')
st.sidebar.header('Input Data')

option = st.selectbox(label='Input Type', 
                      options=my_attribs
)

if option in ['Heart Rate',
              'HRV',
              'Pages Read',
              'Meditate Minutes',
              'Brush Teeth',
              'Water (oz)',
              'Planks',
              'Pushups',
              'Caffeine',
              'Cardio Min']:
    chosen_val = st.number_input(label='Select Value', min_value=0, max_value=500)
    enter = st.button('Add to DB')
    if enter:
        this_data = [today, option, chosen_val]
        my_df = pd.DataFrame(data=[this_data],
                             columns=['DATE', 'ATRRIBUTE', 'VALUE'])
        data = list(zip(my_df['DATE'], 
                        my_df['ATRRIBUTE'], 
                        my_df['VALUE'])
        )
        ut.insert_values(conn, data)
        st.write('Added to DB!')
elif option in ['Journal',
                'Rosary',
                'Shower',
                'Bible']:
    enter = st.button('Add to DB')
    vals = ['Y', 'N']
    chosen_val = st.select_slider(label='Select Level', options=vals)
    if enter:
        this_data = [today, option, chosen_val]
        my_df = pd.DataFrame(data=[this_data],
                             columns=['DATE', 'ATRRIBUTE', 'VALUE'])
        data = list(zip(my_df['DATE'], 
                        my_df['ATRRIBUTE'], 
                        my_df['VALUE'])
        )
        ut.insert_values(conn, data)
        st.write('Added to DB!')
elif option in ['Physical Readiness',
                'Mental Readiness',
                'Happiness Morning',
                'Happiness Night']:
    vals = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    chosen_val = st.select_slider(label='Select Level', options=vals)
    enter = st.button('Add to DB')
    if enter:
        this_data = [today, option, chosen_val]
        my_df = pd.DataFrame(data=[this_data],
                             columns=['DATE', 'ATRRIBUTE', 'VALUE'])
        data = list(zip(my_df['DATE'], 
                        my_df['ATRRIBUTE'], 
                        my_df['VALUE'])
        )
        ut.insert_values(conn, data)
        st.write('Added to DB!')
elif option in ['Time in Bed']:
    chosen_val = st.time_input('Time in bed', dt.time(21, 0))
    enter = st.button('Add to DB')
    if enter:
        this_data = [today, option, str(chosen_val)]
        my_df = pd.DataFrame(data=[this_data],
                             columns=['DATE', 'ATRRIBUTE', 'VALUE'])
        data = list(zip(my_df['DATE'], 
                        my_df['ATRRIBUTE'], 
                        my_df['VALUE'])
        )
        ut.insert_values(conn, data)
        st.write('Added to DB!')
elif option in ['Time awake']:
    chosen_val = st.time_input('Time awake', dt.time(4, 0))
    enter = st.button('Add to DB')
    if enter:
        this_data = [today, option, str(chosen_val)]
        my_df = pd.DataFrame(data=[this_data],
                             columns=['DATE', 'ATRRIBUTE', 'VALUE'])
        data = list(zip(my_df['DATE'], 
                        my_df['ATRRIBUTE'], 
                        my_df['VALUE'])
        )
        ut.insert_values(conn, data)
        st.write('Added to DB!')
else:
    chosen_val = st.text_input(label='Enter value')
    enter = st.button('Add to DB')
    if enter:
        this_data = [today, option, chosen_val]
        my_df = pd.DataFrame(data=[this_data],
                             columns=['DATE', 'ATRRIBUTE', 'VALUE'])
        data = list(zip(my_df['DATE'], 
                        my_df['ATRRIBUTE'], 
                        my_df['VALUE'])
        )
        ut.insert_values(conn, data)
        st.write('Added to DB!')