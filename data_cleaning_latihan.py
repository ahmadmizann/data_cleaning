import pandas as pd
import streamlit as st

def handle_missing_values(df):
    # Tangani missing values jika dipilih
    st.write("## Mengatasi Missing Values")
    # Menampilkan data sebelum handling missing values
    st.write("### Data Sebelum Handling Missing Values:")
    st.write(df)

    # Tangani missing values
    for column in df.columns:
        if df[column].dtype == 'int64' or df[column].dtype == 'float64':
            # Jika tipe data kolom numerik, isi nilai kosong dengan mean
            df[column].fillna(df[column].mean(), inplace=True)
        else:
            # Jika tipe data kolom string, isi nilai kosong dengan modus
            df[column].fillna(df[column].mode()[0], inplace=True)

    # Menampilkan data setelah handling missing values
    st.write("### Data Setelah Handling Missing Values:")
    st.write(df)
    st.write("---")
    return df

# Main program
def main():
    # Judul aplikasi
    st.title("Aplikasi Pre-Processing Data")

    # Load data from user input
    uploaded_file = st.file_uploader("Upload data here (CSV file)", type=["csv"])
    if uploaded_file is not None:
        # Baca data CSV
        df = pd.read_csv(uploaded_file)

        # Tombol untuk memproses data
        if st.button("Process Data"):
            df = handle_missing_values(df)
        # Tombol unduh data hasil proses
            csv = df.to_csv(index=False)
            st.download_button(label="Download Processed Data", data=csv, file_name="processed_data.csv", mime="text/csv")

if __name__ == "__main__":
    main()
