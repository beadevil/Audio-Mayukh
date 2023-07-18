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

# Streamlit app
def main():
    st.title('Save Empty DataFrame as Excel File')
    st.write('Click the button below to save an empty DataFrame as an Excel file.')

    if st.button('Save DataFrame'):
        save_empty_dataframe()

if __name__ == '__main__':
    main()
