import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Creating my first Streamlit app")

# reading in the data from github
df = pd.read_csv("https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv")

#setting up the sidebar
with st.sidebar:
    st.write("Widget to control the app:")
    check = st.checkbox("View raw data")

# selectbox that controls the pie graph
option = ['Region','Category', 'Segment','Ship Mode']
pick = st.sidebar.selectbox("Choose an option", option)

# creating the pie figure
st.write("""
## Pie chart :pie:

Choose between `Region`, `Category`, `Segment` and `Ship Mode` on the selectbox
in the sidebar to show the Quantity based on those features!
    """)
fig = px.pie(df, values = "Quantity", names=pick, title="Quantity by {}".format(pick))
st.plotly_chart(fig)

# slider that controls our histogram
max = int(round(df["Sales"].max()))
value = st.sidebar.slider("My first slider", 0,max, max)

# creating our histogram
st.write("""
## Histogram of Sales :moneybag:

Here is a standard histogram binning the number of sales by their amount.

The largest number of the sales are for amounts of \$25 and below. Only a few
sales are larger than \$10,000, and only one larger than \$20,000.
        """)
fig = px.histogram(df, x="Sales", range_x=[0,value])
st.plotly_chart(fig)
