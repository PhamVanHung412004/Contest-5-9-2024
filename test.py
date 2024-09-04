import streamlit as st
import time

# Initialize session state to keep track of remaining time
if 'remaining_time' not in st.session_state:
    # Set the initial time (3 hours and 30 minutes)
    st.session_state.remaining_time = 3 * 3600 + 30 * 60

# Function to display countdown timer
def countdown():
    while st.session_state.remaining_time:
        hours, remainder = divmod(st.session_state.remaining_time, 3600)
        mins, secs = divmod(remainder, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        
        # Use st.empty to update the time without resetting
        time_placeholder.markdown(f"⏳ Thời gian còn lại: **{timer}**")
        
        time.sleep(1)
        st.session_state.remaining_time -= 1

    time_placeholder.markdown("🎉 **Hết giờ!**")

# Streamlit interface
# st.title("Tham gia thi")

# Button to start countdown
if st.button("Bắt đầu thi"):
    time_placeholder = st.empty()  # Placeholder for the timer
    import a
    countdown()
