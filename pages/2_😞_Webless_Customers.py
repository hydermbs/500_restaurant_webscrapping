#import essential libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Webless Customers", page_icon="😞")

st.header('Webless Customers 😞')

casual_dine = pd.read_csv('Customer with website status.csv')
casual_dine = casual_dine.drop(['Unnamed: 0','Unnamed: 0.1'] ,axis=1)
st.subheader('Choose True to See Entity Has a Functional Website, and False If It Does Not.')


#filter select box for web status 
web_status = st.selectbox( "In this dataset, we have categorized restaurants based on the functionality of their websites.",casual_dine['website_status'].unique())

# Filter the DataFrame based on the user input
filtered_data = casual_dine[casual_dine['website_status'] == web_status]

# Display the filtered DataFrame
st.write(filtered_data)

st.header('Data for Restaurants, Including Information on Website Presence')
# Count the occurrences of True and False
count_values = casual_dine['website_status'].value_counts()


# Create a bar plot using Seaborn based on value counts
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=count_values.index, y=count_values.values, palette="pastel", ax=ax)

# Add labels and title
ax.set(xlabel='Restaurant Working Websites Data', ylabel='Count')

# Show the plot in Streamlit
st.pyplot(fig)