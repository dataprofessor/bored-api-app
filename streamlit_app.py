import streamlit as st
import pandas as pd

st.title('🏀 Bored API app')

selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

st.header('Suggested activity')
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
suggested_activity = pd.read_json(suggested_activity_url)
st.write(suggested_activity)
