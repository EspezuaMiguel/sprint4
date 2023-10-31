import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

#load data
df_vehicles = pd.read_csv('vehicles_us.csv')

# preprocessing fill nan and drop outlier 

df_vehicles['model_year']=df_vehicles.groupby('model', group_keys=False)['model_year'].apply(lambda x:x.fillna(x.median()))
df_vehicles['cylinders']=df_vehicles.groupby('model', group_keys=False)['cylinders'].apply(lambda x:x.fillna(x.median()))
df_vehicles['odometer']=df_vehicles.groupby(['model_year'], group_keys=False)['odometer'].apply(lambda x:x.fillna(x.median()))

# drop outlier prices

# IQR
# Calculate the upper and lower limits
Q1 = df_vehicles['price'].quantile(0.25)
Q3 = df_vehicles['price'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR
 
# Create arrays of Boolean values indicating the outlier rows
upper_array = np.where(df_vehicles['price']>=upper)[0]
lower_array = np.where(df_vehicles['price']<=lower)[0]
 
# Removing the outliers
df_vehicles.drop(index=upper_array, inplace=True)
df_vehicles.drop(index=lower_array, inplace=True)
df_vehicles.reset_index(drop=True, inplace=True)

#''' Detection  and drop outlier by model_year'''
# IQR
# Calculate the upper and lower limits
Q1 = df_vehicles['model_year'].quantile(0.25)
Q3 = df_vehicles['model_year'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR
 
# Create arrays of Boolean values indicating the outlier rows
upper_array = np.where(df_vehicles['model_year']>=upper)[0]
lower_array = np.where(df_vehicles['model_year']<=lower)[0]
 
# Removing the outliers
df_vehicles.drop(index=upper_array, inplace=True)
df_vehicles.drop(index=lower_array, inplace=True)
df_vehicles.reset_index(drop=True, inplace=True)

#  starting web site
st.title('Sprint 4 Project')
st.header('Software Development Tools')
''' table display vehicles_us.csv '''
# plot table
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df_vehicles.columns),
                align='left'),
    cells=dict(values=df_vehicles.transpose().values.tolist(),
               align='left'))
])

st.plotly_chart(fig, theme="streamlit", use_container_width=True)


df_vehicles['manufacturer']  =  df_vehicles['model'].str.split(' ', n=1, expand=True)[0]
df_vehicles['manufacturer_count'] = df_vehicles['manufacturer']
count_vehicles = df_vehicles.groupby(['type','manufacturer'], as_index=False)['manufacturer_count'].count()

fig = px.bar(count_vehicles, x="manufacturer", y="manufacturer_count", color="type", title='Number vehicles by manufacture')
''' Chart manufacture volume'''
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

df_vehicles['condition_count'] = df_vehicles['condition']
count_conditions = df_vehicles.groupby(['condition','model_year'], as_index=False)['condition_count'].count()

fig = px.histogram(count_conditions, x="model_year", y="condition_count", color="condition", nbins=30, title='Histogram - comparison by vehicles condition')
''' Chart Histogram of vehicles condition'''
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

manufacture_comparison = df_vehicles.groupby(['manufacturer'], as_index=False)['manufacturer_count'].count()

#copy price and manufacturer columns
price_manufacture = df_vehicles[['price', 'manufacturer']].copy()
maxlen=[]
for p in price_manufacture['manufacturer'].unique():
      maxlen.append(len(price_manufacture[price_manufacture['manufacturer'] == p]['price']))

maxros =  max(maxlen)
#new_index = pd.Index(range(maxros+1))
print(max(maxlen))

dfm = pd.DataFrame(index=range(maxros))
for p2 in price_manufacture['manufacturer'].unique():
      colupd = price_manufacture[price_manufacture['manufacturer'] == p2]['price'].reset_index(drop=True)

      collen = len(price_manufacture[price_manufacture['manufacturer'] == p2]['price'])

      dfm[p2] = colupd



normalized = st.checkbox('normalize')
# create a figure with two place holder traces
if normalized:
    fig = go.Figure(
        [
            go.Histogram(histfunc="avg",x=dfm[dfm.columns[i]], meta=i, name=i, nbinsx = 50, opacity=0.6, histnorm='probability density')
            for i in range(2)
        ]
    )
else:    
    fig = go.Figure(
        [
            go.Histogram(histfunc="avg",x=dfm[dfm.columns[i]], meta=i, name=i, nbinsx = 50, opacity=0.6)
            for i in range(2)
        ]
    )
# but data for y and name in when country is selected
fig.update_layout(title_text='Histogram - Price comparison between two make vehicles')
fig.update_layout(
    updatemenus=[
        {
            "x": b / 3,
            "y": 1.4,
            "active": None,
            "buttons": [
                {
                    "label": c,
                    "method": "restyle",
                    "args": [{"x": [dfm[c]], "name": c}, [b]],
                }
                for c in dfm.columns
            ],
        }
        for b in range(2)
    ]
)
fig.update_layout(barmode='overlay')
''' select factory comparison'''
st.plotly_chart(fig, theme="streamlit", use_container_width=True)