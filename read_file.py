
import pandas as pd
import numpy as np

import datetime
from pathlib import Path
import plotly.graph_objects as go

import streamlit as st
from io import StringIO
from datetime import datetime, timedelta
from PIL import Image
from pandasai import Agent
import os
from urllib.parse import quote_plus


# Function to check for multiple data types in a column
def check_multiple_dtypes(column):
    return len(set(column.apply(type))) > 1


def load_csv(uploaded_file):
    uploaded_file_name = uploaded_file.name
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file, encoding='utf-8',index_col=False)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    else:
        st.error("Unsupported file type. Please upload a CSV or Excel file.")
    return df,uploaded_file_name



#--#------ Create all the necessary folders and path settings--------------------------------
current_dir= Path(__file__).parent if "__file__" in locals() else Path.cwd()

assets_folder=current_dir.resolve() / "assets"
output_folder=current_dir.resolve() / "output"

#----date initialization-------------
current_date = datetime.now()
current_month_name = current_date.strftime('%B')
target_month = current_date.month - 3     # last 3 months from present month
target_year = current_date.year

# Adjust the year if needed
if target_month <= 0:
    target_month += 12
    target_year -= 1

target_date = datetime(target_year, target_month, 1)

# # Format the date as string in 'YYYY-MM-DD' format
start_date_string = target_date.strftime('%Y-%m-%d')
end_date_string = current_date.strftime('%Y-%m-%d')

# # Convert date strings to date objects
start_datetime = datetime.strptime(start_date_string, '%Y-%m-%d')
end_date_only = datetime.strptime(end_date_string, '%Y-%m-%d')
end_datetime = pd.to_datetime(end_date_only) + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)  # Include full end date

#----end of date----------------

#------------------------cps end-----------------------------------------------------

st.set_page_config(layout="wide", initial_sidebar_state="auto", page_title="Auto_report", page_icon=':moon:')


# pandas_key = '$2a$10$3saJ4BA.6KzozayTfmPs9.WY/w1vzRlOVPVJBJWCg6.9UfNbZd/6G'
#     # Encode the password
# encoded_password = quote_plus(pandas_key)
os.environ["PANDASAI_API_KEY"] ='$2a$10$3saJ4BA.6KzozayTfmPs9.WY/w1vzRlOVPVJBJWCg6.9UfNbZd/6G'#encoded_password



    



with st.sidebar:
    webid_png=Image.open(assets_folder.resolve()/"images"/"webid.png")
    st.logo(webid_png,link="https://www.webid-solutions.com",icon_image=webid_png)
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        df,uploaded_file_name=load_csv(uploaded_file)
    
        # Check each column if any multiple data types in one column
        columns_with_multiple_dtypes = {col: check_multiple_dtypes(df[col]) for col in df.columns}

        # Filter the dictionary to keep only columns without multiple data types
        columns_without_multiple_dtypes = {col: has_multiple_dtypes for col, has_multiple_dtypes in columns_with_multiple_dtypes.items() if not has_multiple_dtypes}

        select_date = st.date_input("Wählen Sie einen Datumsbereich aus:", (start_datetime, end_datetime))   #Select a date range:
        columns_names = df.columns.tolist()

        column_dtypes = df.dtypes#.to_dict()   

        filtered_default_columns_names = columns_names[:2]
        int64_columns = [col for col in df.columns if df[col].dtype == 'int64' or df[col].dtype == 'float64']   # Filter columns with int64 dtype
        object_columns = [col for col in df.columns if df[col].dtype == 'object']   # Filter columns with int64 dtype

        selected_columns = st.multiselect("Select columns to disply:", options=columns_names, default=filtered_default_columns_names )

        selected_filter_column = st.selectbox("Select an integer column for Filtering. Ex: date...", options=columns_without_multiple_dtypes )

        #---Conditions as per the data type
        if pd.api.types.is_integer_dtype(df[selected_filter_column]) or pd.api.types.is_float_dtype(df[selected_filter_column]):
        #if df[selected_filter_column].dtype in ['int64', 'float64']:   ## Numeric column
            min_filter_value = df[selected_filter_column].min(skipna=True)
            max_filter_value = df[selected_filter_column].max(skipna=True)
            filtered_options = df[selected_filter_column].dropna()

        #elif df[selected_filter_column].dtype in ['object']:
        elif pd.api.types.is_object_dtype(df[selected_filter_column]):
            filtered_options = df[selected_filter_column].dropna()
            min_filter_value = filtered_options.iloc[0]
            max_filter_value = filtered_options.iloc[-1]
            
        elif pd.api.types.is_datetime64_any_dtype(df[selected_filter_column]):
            filtered_options = df[selected_filter_column].dropna()
            filtered_options = filtered_options.reset_index(drop=True)
            min_filter_value = filtered_options.iloc[0]
            max_filter_value = filtered_options.iloc[-1]
            
        else:
            start_int_value, end_int_value=None
            st.error("Cannot use this column to filter")

        start_filter_value, end_filter_value = st.select_slider(    "Select a range",    options=filtered_options.sort_values().unique(),   value=(min_filter_value,max_filter_value ))
        
 
        agent = Agent(df)
        question = st.text_input("Ask a question:")
    
        # Step 2: If question is provided, process it with the agent
        if question:
            # Create an instance of Agent
            agent = Agent(df)
            
            # Step 3: Get the answer from the agent
            answer = agent.chat(question)
            
            # Step 4: Display the answer
            st.write(f"Answer: {answer}")
        
        
       

    else:
        st.info("Please upload an excel or csv file!")
        
# Check the data type of the selected column
    # if df[selected_filter_column].dtype == 'int64':
    #     st.write(f"The selected column '{selected_filter_column}' is of type int64.") 


if uploaded_file is not None:
    if selected_columns:
            # Filter the DataFrame based on the selected range
        filtered_df = df[(df[selected_filter_column] >= start_filter_value) & (df[selected_filter_column] <= end_filter_value)]

        with st.expander(f"Tabel view of '{uploaded_file_name}'", expanded=True):
            st.dataframe(filtered_df[selected_columns],use_container_width=True)
        
        with st.container(border=True) :
            c1,c2,c3=st.columns(3)
            x=c1.selectbox("X-axis",options=selected_columns)
            y=c2.selectbox("Y-axis",options=selected_columns)
            chart=c3.radio("Chart type",["Bar",  "Line","Scatter"],index=None,horizontal=True,)  #"Pie",
  
            
            if chart=="Bar":
                is_horizontal = st.radio("", ["Horizontal", "Vertical"], horizontal=True) == "Horizontal"
                st.bar_chart(filtered_df, x=x, y=y,horizontal=is_horizontal)
            #elif chart=="Pie":
                
                #st.bar_chart(filtered_df, x=x, y=y)
                
            elif chart=="Line":
                st.line_chart(filtered_df, x=x, y=y)
                
            elif chart=="Scatter":    
                st.scatter_chart(filtered_df, x=x,  y=y,  color=y, size=y,)
        
    else:
        st.write("No columns selected.")
        
else:
    st.info("Please upload an excel or csv file!")


    
      

# if pd.api.types.is_integer_dtype(df[selected_filter_column]):
#     st.write(f"The selected column '{selected_filter_column}' is of integer type.")
#     # Perform actions for integer type columns
# elif pd.api.types.is_datetime64_any_dtype(df[selected_filter_column]):
#     st.write(f"The selected column '{selected_filter_column}' is of datetime")
                     
# else:
#     st.write(f"The selected column '{selected_filter_column}' is of type {df[selected_filter_column].dtype}.")
  
    



  
