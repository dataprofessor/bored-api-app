import streamlit as st

st.title('🏀 Activities to Do')

selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

st.header('Suggested activity')
suggested_activity = f'http://www.boredapi.com/api/activity?type={selected_type}'
st.info(suggested_activity)
