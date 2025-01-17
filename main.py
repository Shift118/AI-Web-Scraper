#streamlit creates really simple web apps with few lines of code
import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content,
    )
from parse import parse_with_ollama

# Set the title of the Streamlit app
st.title("AI Web Scraper")

# Input field for the user to enter a website URL
url = st.text_input("Enter a Website URL:")

# Button to trigger the scraping process
if st.button("Scrape Site"):
    # Inform the user that the website is being scraped
    st.write("Scraping the Website")
    
    # Call the scrape_website function to get the HTML content of the website
    result = scrape_website(url)
    
    # Extract the body content from the HTML
    body_content = extract_body_content(result)
    
    # Clean the extracted body content
    cleaned_content = clean_body_content(body_content)
    
    # Store the cleaned content in the session state
    st.session_state.dom_content = cleaned_content
    
    # Expandable section to view the DOM content
    with st.expander("View Dom Content"):
        # Text area to display the cleaned DOM content
        st.text_area("DOM Content", cleaned_content, height=300)

# Check if 'dom_content' is in the session state
if "dom_content" in st.session_state:
    # Text area for the user to describe what they want to parse
    parse_description = st.text_area("Describe what you want to parse:")

    # Button to trigger the parsing process
    if st.button("Parse Content"):
        # Check if the user has provided a parse description
        if parse_description:
            # Inform the user that the content is being parsed
            st.write("Parsing the content")
            
            # Split the DOM content into chunks
            dom_chunks = split_dom_content(st.session_state.dom_content)
            
            # Call the parse_with_ollama function to parse the content based on the description
            result = parse_with_ollama(dom_chunks, parse_description)
            
            # Display the parsing result
            st.write(result)