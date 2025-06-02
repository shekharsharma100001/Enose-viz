import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'e-nose_dataset_12_beef_cuts.xlsx'

sheet_names = pd.ExcelFile(file_path).sheet_names

selected_sheet = st.sidebar.selectbox("Select a sheet", sheet_names)

df = pd.read_excel(file_path, sheet_name=selected_sheet)

# Sensor columns
mq_columns = ['MQ135', 'MQ136', 'MQ137', 'MQ138', 'MQ2', 'MQ3', 'MQ4', 'MQ5', 'MQ6', 'MQ8', 'MQ9']

sensor_options = ['All'] + mq_columns
selected_sensor = st.sidebar.selectbox("Select MQ sensor", sensor_options)


st.title("E-Nose Sensor Data Visualization")
st.subheader(f"Sheet: {selected_sheet}")

#X-axis
x = df['TVC']

if selected_sensor == 'All':

    fig, axes = plt.subplots(4, 3, figsize=(16, 12))
    axes = axes.flatten()

    for i, sensor in enumerate(mq_columns):
        y = df[sensor]
        axes[i].plot(x, y)
        axes[i].set_title(sensor)
        axes[i].set_xlabel("TVC")
        axes[i].set_ylabel(sensor)

    # Hide the unused 12th subplot
    axes[11].axis("off")

    plt.tight_layout()
    st.pyplot(fig)

else:
    # Plot selected sensor only
    y = df[selected_sensor]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, color='blue')
    ax.set_title(f"{selected_sensor} vs TVC")
    ax.set_xlabel("TVC")
    ax.set_ylabel(selected_sensor)
    st.pyplot(fig)
