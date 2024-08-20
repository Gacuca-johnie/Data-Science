import streamlit as st


about_page = st.set_page_config(
    page= "views/about-me.py",
    title= "about-me",
    icon=":Material/Account_circle:",
    default= True,
)
project_1_page= st.set_page_config(
    page="Views/sales-dashboard.py",
    title="sales_Dashboard",
    icon=":Material/bar_chart:",
)
project_2_page= st.set_page_config(
    page="Views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

