import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data 
data = pd.read_csv('hour.csv')

# Page title
st.title('Dashboard Penyewaan Sepeda')

# Sidebar dengan filter musim
st.sidebar.header('Filter')
selected_season = st.sidebar.selectbox('Pilih Musim', data['season'].unique())

# Filter data berdasarkan musim yang dipilih
filtered_data = data[data['season'] == selected_season]

# Visualisasi 1: Rata-rata penyewaan per musim
fig, ax = plt.subplots()
sns.barplot(x='season', y='cnt', data=data, ax=ax, palette='pastel')
plt.title('Rata-rata Jumlah Penyewaan Sepeda per Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Sepeda Disewa')
st.pyplot(fig)

# Visualisasi 2: Hubungan antara kecepatan angin dan jumlah penyewaan
fig, ax = plt.subplots()
sns.scatterplot(x='windspeed', y='cnt', data=filtered_data, ax=ax)
plt.title('Hubungan Kecepatan Angin dan Jumlah Penyewaan (Musim {})'.format(selected_season))
plt.xlabel('Kecepatan Angin')
plt.ylabel('Jumlah Sepeda Disewa')
st.pyplot(fig)