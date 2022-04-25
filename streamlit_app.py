import streamlit as st
import requests

st.title('🏀 Bored API app')

selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
selected_participants = st.sidebar.slider('Select the number of participants', 1, 10, 1)

st.header('JSON data')
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}&participants={selected_participants}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
st.write(suggested_activity)

st.header('Suggested activity')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=selected_participants, delta='')
with col2:
  st.metric(label='Type of Activity', value=selected_type, delta='')
