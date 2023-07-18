import streamlit as st
import pandas as pd

def save_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame()

    # Save the DataFrame as an Excel file
    file_path = 'file.xlsx'
    df.to_excel(file_path, index=False)

    # Display a success message
    st.success('Empty DataFrame saved as Excel file.')

def read_excel_file():
    # Read the Excel file as a DataFrame
    file_path = 'file.xlsx'
    df = pd.read_excel(file_path)

    # Display the DataFrame
    st.write(df)

# Streamlit app
def main():
    st.title('Save Empty DataFrame as Excel File')
    st.write('Click the buttons below to save an empty DataFrame as an Excel file or read an existing Excel file as a DataFrame.')

    if st.button('Save DataFrame'):
        save_empty_dataframe()

    if st.button('Read Excel File'):
        read_excel_file()

if __name__ == '__main__':
    main()
