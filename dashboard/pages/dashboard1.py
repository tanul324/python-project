import streamlit as st             
import pandas as pd     
import seaborn as sns      
import plotly.express as px                   

st.title("HealthCare Dataset")

#st.image('',use_column_width=True)

df = pd.read_csv(r"C:\Users\TANUL\Desktop\python project\healthcare_dataset.csv")

#display the dataset
st.dataframe(df)

st.sidebar.header("filter options")
Gender = st.sidebar.multiselect ('Gender',
                                options=df['Gender'] .unique(),
                                default=df['Gender'].unique())

#class filters


#age filters
min_age, max_age, = st.sidebar.slider('Age',
                                min_value = int(df['Age'].min()),
                                max_value = int(df['Age'].max()),
                                value = (int(df['Age'].min()),int(df['Age'].max())))

#filter the data based on the user slecetion

filtered_df = df[
    (df['Gender'].isin(Gender))&
    
    (df['Age']>= min_age)&
    (df['Age']<= max_age)
]
st.dataframe(filtered_df)

#create a piechart for gender distribution
st.subheader("Gender")
gender_count = filtered_df['Gender'].value_counts()
fig = px.pie(names=gender_count.index, values=gender_count.values, title='Gender Distribution')
st.plotly_chart(fig)

#create a histogram for age distribution
st.subheader("Age Distribution")
fig = px.histogram(filtered_df, x='Age', nbins=20, title='Age distribution',
                    labels={'Age':'Age','count':'Number of Patients'})
st.plotly_chart(fig)

#create a histogram for age distribution
