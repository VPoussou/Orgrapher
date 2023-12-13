
import streamlit as st
import asyncio

class Timer:
    def __init__(self, seconds):
        self.seconds = seconds

    text = st.empty()
    async def count_down(self):
        while self.seconds:
            mins, secs = divmod(self.seconds, 60)
            time_now = '{:02d}:{:02d}'.format(mins, secs)
            self.text.text(f"{time_now}")
            await asyncio.sleep(1)
            self.seconds -= 1
        self.text.text("Time Up!")

timers = []

st.sidebar.title("Other Options")
bootoon = st.sidebar.button("Add 'twerk'")
async def the_twerker():
    if bootoon:
        st.sidebar.write("Twerk")

async def main():
    st.title("Pomodoro")
    time_minutes = st.number_input('Enter the time in minutes ', min_value=1, value=25)
    time_in_seconds = time_minutes * 60
    if st.button("Start"):
        timer = Timer(time_in_seconds)
        timers.append(timer)
        await timer.count_down()

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(the_twerker())
