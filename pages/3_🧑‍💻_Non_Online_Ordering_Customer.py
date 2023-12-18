#import essential libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Non-Online Ordering Customer", page_icon="🧑‍💻")

st.header('Non-Online Ordering Customer 🧑‍💻')

st.markdown(
    """
    **Details on the availability of online ordering services for the restaurant.**
    """
    )

web_order = pd.read_csv('customer with online status.csv')
web_order = web_order.drop(['Unnamed: 0','Unnamed: 0.1', 'Online_order'] ,axis=1)
count_online = web_order['online_order'].value_counts()
st.subheader('Choose True To See The Entity Has an Online Ordering, and False If It Does Not.')

#filter select box for web status 
online_status = st.selectbox( 'Select One', web_order['online_order'].unique())

# Filter the DataFrame based on the user input
filtered_online = web_order[web_order['online_order'] == online_status]



# Display the filtered DataFrame
st.write(filtered_online)

st.header('Restaurant Data with Details on Online Ordering')

#create a bar plot for the online order
sns.set(style= 'whitegrid')
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=count_online.index, y=count_online.values, palette="pastel", ax=ax)

# Add labels and title
ax.set(xlabel='Restaurant Online Ordering Data', ylabel='Count')

# Show the plot in Streamlit
st.pyplot(fig)