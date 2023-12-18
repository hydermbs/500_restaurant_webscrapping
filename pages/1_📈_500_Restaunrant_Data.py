#import essential libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="500 Restaurant Data", page_icon="📈")
#import data set
df = pd.read_csv('rest_data.csv')
df = df.drop('Unnamed: 0',axis=1)
st.title('500 Resturant Data 📈:')
st.markdown(
    """ 
    In this page you can see the data of 500 restaurant with following details.
    - Name
    - Contact Number
    - Cusine
    - Dining Style
    - Location
    - Website
    - Payment Methods
    """
)
st.write(df)
st.subheader('Graph: Dining Style-based Restaurant Data')
st.markdown(
    """
    I have categorized the data to ascertain the count of restaurants based on their dining styles.
    """
)
dine_style = df['Dining_style'].value_counts()

# Create a bar plot using Seaborn
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=dine_style.index, y=dine_style.values, palette="viridis", ax=ax)

# Add labels and title
ax.set(xlabel='Categories', ylabel='Count')
# Show the plot
st.pyplot(fig)

st.markdown(
    """ 
    **We discovered that Casual Dining establishments constitute a significant portion of our dataset and are closely aligned with our Ideal Customer Profile (ICP). These establishments are more likely to be potential customers for website-related services when compared to Fine Dining establishments.**
    **We are going to discus Casual Dining Only in next pages**
    """
)