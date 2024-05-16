import streamlit as st
import emoji

st.title("Streamlit App with Emoji Package")

emoji_list = [":smile:", ":heart:", ":rocket:", ":sun_with_face:", ":pizza:"]

selected_emoji = st.selectbox("Select an emoji:", emoji_list)

if st.button("Get Emoji Description"):
    emoji_description = emoji.demojize(selected_emoji)
    st.write(f"Description of {selected_emoji}: {emoji_description}")
