#streamlit creates really simple web apps with few lines of code
import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content,
    )

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the Website")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    st.session_state.dom_content = cleaned_content
    
    with st.expander("View Dom Content"):
        st.text_area("DOM Content", cleaned_content, height= 300)
        
if "dom_content" in st.session_state:
    parse_description = st.text_area("Descripe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")
            dom_chunks = split_dom_content(st.session_state.dom_content)