import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random


from PIL import Image
logo = Image.open('logo.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run strealit :   streamlit run test2.py 
st.set_page_config(page_title="MILITARY DATA EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
# Define the list of names
names = ["21A21A6159-U.N.V RAVITEJA", "21A21A6106-B.MANIKANTA", "21A21A6105-B.VINAY BHASKAR","21A21A6150-R.POOJA SRI","22A25A6106-V.SAI GANESH","21A21A6134-L.MEGHA SYAM","21A21A6153-SK.N.KHASIM","21A21A6117-J.VENKATA LAKSHMI","21A21A6109-D.PREM KUMAR"]
st.title("EXPLORATORY DATA ANALYSIS ON MILITARY DATASET")
# Add the names to the sidebar
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)
st.sidebar.title("Under The Guidance of :")
st.sidebar.write("Dr.BOMMA RAMAKRISHNA")
# File upload
uploaded_file = st.file_uploader("CHOOSE MILITARY DATASET")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.dataframe(data)

    st.title("military Data Analysis")


    if st.checkbox("Show count of non-null values"):
        st.write(data.count())

    if st.checkbox("Show all Null Values"):
        st.write(data.isnull().sum())
    # Display data
    if st.checkbox("Show data"):
        st.write(data.head())
    if st.checkbox("Show shape"):
           st.write(data.shape)


    if st.checkbox("Describe military Data"):
       st.write(data.describe())
    
   
    

   
    if st.checkbox("Show index"):
        st.write(data.index)

    if st.checkbox("Show columns"):
        st.write(data.columns)

    #if st.checkbox("Show data types"):
        # Convert data types to strings as a workaround for Arrow bug
        #data = data.astype(str)
        #st.dataframe(data.dtypes)

    

    # Remove column with missing values
    
    
    # Bar chart
    if st.checkbox("Show bar chart of Military personnel"):
        plt.figure(figsize=(10, 8))
        sns.barplot(x="Country ", y="Per 1000 capita (total)", data=data)
        st.pyplot()

   
  
    
   
    fill_type = st.radio("Select the fill type for null values:", options=[ "bfill", "ffill","fill"])
    data['ffiiina'] = np.random.randint(1, 10, size=len(data))
    data['bfillna'] = data['Reserve military'].fillna(method='bfill')
    
    if fill_type == "bfill":
        data.fillna(method='bfill', inplace=True)
        st.write("Null values filled with backward fill method.")
        st.write(data)
    elif fill_type == "ffill":
        data.fillna(method='ffill', inplace=True)
        st.write("Null values filled with forward fill method.")
        st.write(data)
    elif fill_type == "fill":
        data.fillna(value=4,inplace=True)
        st.write(data)
    # Sort data by a column and select top 25 rows

     # Correlation matrix
    if st.checkbox("Show correlation matrix of Military Data"):
        data_numeric = data.select_dtypes(include=[np.number])
        corr_matrix = data_numeric.corr()

       
        
        st.write(corr_matrix)
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
        st.pyplot()
    
    if st.checkbox("Show scatter plot of Military personnel vs Military expenditure"):
        plt.figure(figsize=(10, 8))
        plt.scatter(data["Per 1000 capita (total)"],data["Per 1000 capita (active  member)"])
        plt.xlabel("Per 1000 capita (total)")
        plt.ylabel("Per 1000 capita (active  member)")
        st.pyplot()



    if st.checkbox("to modify the dataset values"):
        selected_row = st.selectbox("Select row to modify", data.index)
        current_values = data.loc[selected_row]
        new_values = {}
        for column in data.columns:
            new_value = st.text_input(f"{column} ({current_values[column]})", value=current_values[column])
            new_values[column] = new_value

        if st.button("Update row"):
            data.loc[selected_row] = new_values
            st.write("Row updated.")
            st.write(data)
  
    
    
