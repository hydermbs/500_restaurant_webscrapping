import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)
st.title("Web Scraping Success: 500 Restaurants Examined 👋")
st.write('### In this web data application, I have extracted information from 500 restaurants on https://www.kayak.com/London.28501.restaurantlist.ksp. Despite the website containing data for over 1000 restaurants, I focused on processing data for 500 of them.')
st.markdown(
"""
In this application, I've conducted data extraction and analysis aligned with the Flipdish Ideal Customer Profile (ICP). Our target audience comprises single-owner restaurants that present opportunities for additional product purchases. I initiated the analysis by categorizing customers into the Casual Dining segment. Subsequently, I identified customers without websites and further investigated those with websites but lacking online ordering capabilities.

### Our primary customer segments include:

- Customers with a registered website domain but lacking an active website. This data is available in the 'Customers without Website' section.
- Customers with a functioning website but without online ordering capabilities. You can locate this information in the 'Customers without Online Ordering' section.
"""
)