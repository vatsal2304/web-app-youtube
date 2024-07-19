import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# from streamlit import config as _config
# from streamlit.web.bootstrap import run

# _config.set_option("server.h
# flag_options=[], is_hello=False)



#Title and Subheader
st.title("Data Analysis")
st.subheader("Data Analysis Using Python And Streamlit")

# Upload Dataset
upload = st.file_uploader("upload your dataset(only in csv form)")
if upload is not None:
    data = pd.read_csv(upload)


# Show Dataset
if upload is not None:
    if st.checkbox("Overview/Structure Of Dataset"):
        st.write(f"Number of Rows: {data.shape[0]}")
        st.write(f"Number of columns: {data.shape[1]}")
        st.write(data.describe(include='all'))

if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Above Age Of 40"):
            st.text(len(data[data['Age']>40]))
            st.write(data[data["Age"]>40])

        if st.button("Below Age Of 40"):
            st.text(len(data[data["Age"]<=40]))
            st.write(data[data["Age"]<=40])

        if st.button("Total Males"):
            st.text(len(data[data["Sex"] == 'male']))
            st.write(data[data["Sex"] == 'male'])

        if st.button("Total Females"):
            st.text(len(data[data["Sex"] == 'female']))
            st.write(data[data["Sex"] == 'female'])

        if st.button("No Age mentioned"):
            st.text(len(data[data['Age'].isnull()]))
            st.write(data[data['Age'].isnull()])

        if st.button("Total null values"):
            st.text(len(data[data.isnull().any(axis=1)]))
            st.write(data[data.isnull().any(axis=1)])
        if st.button("Males And Females"):
            plt.xlabel("Sex")
            plt.ylabel("Count")
            plt.bar(data['Sex'] == 'male', len(data[data['Sex'] == "male"]), width=0.5)
            plt.bar(data['Sex'] == 'female', len(data[data['Sex'] == "female"]), width=0.5)
            plt.show()


if upload is not None:
    if st.checkbox("Check dataType of each column"):
        st.text("DataTypes")
        st.write(data.dtypes)

if upload is not None:
    if st.checkbox("By"):
        st.success('Vatsal Jasani')