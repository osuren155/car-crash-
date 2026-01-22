import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px



df=sns.load_dataset("car_crashes")


st.markdown("<h1 style='text-align:center;'>Car Crashes Data Set</h1>",unsafe_allow_html=True)
st.dataframe(df)   


# bar chart of state wise accidents Data 
st.subheader('States Wise Accidents Data') 
fig= px.bar(df, x='abbrev',y='total', 
            title="Total accidents by state",
            labels={'abbrev':'state','total':'Total accidents'},
            template='plotly_dark', 
            color='total')
st.plotly_chart(fig)
st.markdown("""
### Key Insights
The analysis identifies high-accident states and 
shows that alcohol-influenced accidents are significantly higher 
in three states. One of these states is ND, where the alcohol-related accident rate is recorded at 10.038.
""")


# Top 10 States by Accidents where driver was not distracted 
st.subheader("Top 10 States by Accidents Data")
top10 = df.sort_values('total', ascending=False).head(10)
# Plotly bar chart
fig = px.bar(top10,x='abbrev',y='total',
    color='total',
    title=' States wise Accidents ',
    labels={'abbrev': 'States', 'total': 'Total accidents'}
)
st.plotly_chart(fig) 
st.markdown("""
Road accidents in the US are concentrated in a few high-risk states. 
North Dakota, South Carolina, and West Virginia report the highest accident levels,
with alcohol influence being a major contributing factor. Stronger road safety rules and enforcement are needed in these states.
""")



st.subheader("Accident Cause Distribution Dashboard")
# Sum of accident causes
cause_data = pd.DataFrame({
    "Cause": ["Alcohol", "Speeding", "Not Distracted"],
    
    "Accidents": [df["alcohol"].sum(),
                 df["speeding"].sum(),
                 df["not_distracted"].sum()]
})
fig = px.pie(
    cause_data,
    names="Cause",
    values="Accidents",
    title="Overall Accident Cause Distribution",
    hole=0.4 
)
st.plotly_chart(fig)
st.subheader("Insights")
st.markdown("""
- Alcohol consumption and speeding are the primary contributors to road accidents.  
- Insurance companies should initiate targeted **road safety and awareness campaigns**.  
- **Higher insurance premiums and specialized policy riders** can be introduced for high-risk drivers to mitigate losses.  
""")




# bar chart for state - wise alcohal related car crashes  
st.subheader('State-wise Alcohol Related Car Crashes')
fig = px.bar(df,x='abbrev',y='alcohol',
    title='State-wise Alcohol Related Car Crashes',
    labels={'abbrev': 'State'},
    color='alcohol' ,
 )
st.plotly_chart(fig) 
st.markdown("""
###  Key Insights
- In most states, accident rates fall within a moderate range (approximately 3–6), indicating a relatively consistent overall pattern.

- Three states have been identified where alcohol-influenced accident rates are significantly higher and clearly stand out compared to others.

- Among these high-risk states, **North Dakota (ND)** reports an accident rate of **10.038**, making it one of the highest values in the dataset.

- This trend strongly indicates that alcohol consumption is a major contributing factor to road accidents, particularly in specific high-risk states.
""")



st.subheader("Top 10 States by Insurance Premium")
top10 = df.sort_values('ins_premium', ascending=False).head(10)

fig = px.bar(top10,x='abbrev',y='ins_premium',color='ins_premium',
            title='State-wise Insurance Premium',
             labels={'abbrev': 'States',
                     'ins_premium': 'Insurance Premium'}
) 
st.plotly_chart(fig)
st.markdown("""
### Key Insights
- A high insurance premium typically indicates:
  - A higher probability of accidents, or  
  - Significant insurance losses observed in the past.

- These states can be classified as **high-risk zones** for insurance companies and require closer risk assessment and pricing strategies.
""")







 