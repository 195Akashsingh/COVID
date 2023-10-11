import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import streamlit as st




df = pd.read_csv("data.csv", encoding='windows-1252')
df.head()

st.set_page_config(page_title="Sales Dashboard",
                   page_icon=":bar_chart",
                   layout="wide")
st.title(":bar_chart: Diwali Sales Dashboard")
st.markdown("##")
st.dataframe(df)

State = st.sidebar.multiselect(
"Select the State:",
options = df["State"].unique(),
default=df["State"].unique()
)

Gender= st.sidebar.multiselect(
"Select the Gender:",
options = df["Gender"].unique(),
default=df["Gender"].unique()
)

Occupation= st.sidebar.multiselect(
"Select the Occupation:",
options = df["Occupation"].unique(),
default=df["Occupation"].unique()
)

df_selection= df.query(
    "State ==@State & Gender == Gender & Occupation == Occupation"
)
st.dataframe(df_selection)



total_sales = int(df_selection["Amount"].sum())
average_rating = round(df_selection["Age"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["Amount"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("""---""")


# Graph 1=================================================================================================================================


st.title("Age Distribution with Kernel Density Estimate")
st.write('''This captivating histogram beautifully captures the age distribution within our dataset,
          showcasing a rich variety of customer age groups.
          The Light Sea Green bars stand out against the dark background, highlighting the frequency of different ages''')

fig=plt.figure(figsize=(10, 5))
hist_color = "#20B2AA" 
edge_color = "black"  
sns.histplot(df["Age"], color=hist_color, linewidth=2, edgecolor=edge_color)
sns.set_style("dark")
st.write(fig)


# Graph 2=================================================================================================================================


st.title("Occupation-wise Sales Disaggregation by Gender")
st.write('''This compelling bar plot presents a detailed breakdown of
          sales across various occupations, each distinctively represented by gender''')

fig=plt.figure(figsize=(15, 9))
custom_palette = ["#FF69B4", "#00BFFF"]  
ax = sns.barplot(x="Occupation", y="Amount", data=df, hue="Gender", palette=custom_palette)
sns.set_style('dark')
background_color = "black" 
ax.set_facecolor(background_color)
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

ax.grid(color='#2B60DE', linestyle='--', linewidth=0.5, axis='y', alpha=0.7)
legend = ax.legend()
legend.set_title("Gender")
for text in legend.get_texts():
    text.set_color("white")

ax.set_title("Occupation-wise Amount by Gender", fontsize=18, color='white')
ax.set_xlabel("Occupation", fontsize=16, color='white')
ax.set_ylabel("Amount", fontsize=16, color='white')
st.write(fig)


# Graph 3=================================================================================================================================


st.title('Top Zones by Sales')
st.write('''This dynamic bar chart showcases the top-performing zones in terms of sales,
          offering a clear visual representation of revenue generation across different areas''')

Top_Zone = df.groupby(["Zone"]).sum().sort_values("Amount", ascending=False)
Top_Zone = Top_Zone[["Amount"]].astype(int)
Top_Zone.reset_index(inplace=True)

fig=fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor('black')  
ax.set_facecolor('black')  

plt.title("Zone wise Sale", fontsize=18, color='white')
plt.bar(Top_Zone["Zone"], Top_Zone["Amount"], color='#FF1493', edgecolor='Red', linewidth=1)
plt.xlabel("Zone", fontsize=15, color='white')  
plt.ylabel("Amount", fontsize=15, color='white')

plt.xticks(color='white', rotation=45)  
plt.yticks(color='white')
st.write(fig)


# Graph 4=================================================================================================================================


st.title("Top 10 Occupations by Total Amount")
st.write('The bar chart displays the top 10 occupations based on the total amount in our dataset')
st.write("These occupations represent the highest financial contributions within our records")
Top_occupations = df.groupby(["Occupation"]).sum().sort_values("Amount", ascending=False).head(10)
Top_occupations = Top_occupations[["Amount"]].round(2)
Top_occupations.reset_index(inplace=True)

plt.style.use('dark_background')
fig=plt.figure(figsize=(19, 7))
plt.title("Top 10 Occupations", fontsize=18)
sns.barplot(x="Occupation", y="Amount", data=Top_occupations, palette='viridis')
plt.xlabel("Occupation", fontsize=16)
plt.ylabel("Amount", fontsize=16)
plt.xticks(rotation=45, fontsize=12, ha='right')  
plt.yticks(fontsize=12)
st.write(fig)


# Graph 5=================================================================================================================================


st.title('Financial Trends Across Occupations')
st.write('''The line plot above illustrates the financial trends across various occupations in our dataset.
            Each point on the line represents the amount associated with a specific occupation,
            offering a glimpse into the financial contributions of different professions''')

fig = plt.figure(figsize=(10, 5))
sns.lineplot(x="Occupation", y="Amount", data=df, color='red')
plt.title("Occupation-wise Sales", fontsize=18)
plt.xlabel("Occupation", fontsize=15)
plt.ylabel("Amount", fontsize=15)
plt.xticks(rotation=45)  
plt.grid(True)  

st.write(fig)


# Graph 6=================================================================================================================================


st.title('Gender Distribution Overview')
st.write('''This pie chart provides a visual representation of the gender distribution within our dataset.
          It illustrates the proportion of each gender category,
          giving us insights into the diversity of our data''')
Gender_count=df.Gender.value_counts()
explode =[0,0.1]

colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f']
fig=fig, ax = plt.subplots(figsize=(9, 5))
fig.patch.set_facecolor('#000000') 
ax.set_facecolor('#000000')  
wedges, texts, autotexts = ax.pie(Gender_count.values, labels=Gender_count.index, explode=explode, autopct='%1.1f%%', shadow=True, wedgeprops={'width': 0.3},
       colors=colors, startangle=90)  
for text, autotext in zip(texts, autotexts):
    text.set(color='white', fontweight='bold')  
    autotext.set(color='white', fontweight='bold') 

st.write(fig)



#conclusion=========================================================================


st.title('conclusion')

st.write('''1.The visualization illustrates the diverse age distribution of customers in the dataset, with prominent peaks in the 26-35 age group, represented by Light Sea Green bars against a dark background.
esents the gender distribution in the dataset, showcasing the diversity with 51.2% male and 48.8% female records.''')
st.write('2.The visualization provides a comprehensive breakdown of sales across different occupations, highlighting gender disparities, with distinct representations for each occupation.')
st.write('3.The visualization highlights the top-performing sales zones, emphasizing revenue generation disparities across different areas, with vibrant pink bars against a black background.')
st.write('4.The visualization highlights the top-performing sales zones, emphasizing revenue generation disparities across different areas, with vibrant pink bars against a black background.')
st.write('5.The visualization highlights the top-performing sales zones, emphasizing revenue generation disparities across different areas, with vibrant pink bars against a black background.')
st.write('6.The pie chart visually represents the gender distribution in the dataset, showcasing the diversity with 51.2% male and 48.8% female records.')












