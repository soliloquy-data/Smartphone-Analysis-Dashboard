import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set page title and icon
st.set_page_config(page_title="Smartphone Data Analysis", page_icon="📱")

# Sidebar for navigation
st.sidebar.title("Smartphone Data Analysis & Dashboard")  # Sidebar Title
options = [
    "Intro 🏠", 
    "Overall Analysis 📊", 
    "User-centric Analysis 👥"
]
selection = st.sidebar.radio("Choose an option", options)



# Display intro content
if selection == "Intro 🏠":
    st.title("Smartphone Data Analysis & Dashboard")
    st.markdown("""
    Welcome to the **Smartphone Data Analysis & Dashboard!** This platform offers deep insights into a dataset of smartphones sourced from **[Smartprix](https://www.smartprix.com/mobiles)**, a leading website for smartphone comparisons. The dataset spans from **2014 to November 2024**, showcasing a wide variety of smartphones across different brands, models, and key features.

    ### Data Filtering Criteria
    To ensure quality and relevance, only smartphones with at least a **processor** and **1GB of RAM** are considered, resulting in a refined dataset of **3556 smartphones**.

    ### Analysis Sections
    1. **Overall Analysis**: This section provides a comprehensive look at the entire dataset, focusing on key trends, brand performance, and feature distributions. Users can explore visualizations that highlight market dynamics, brand popularity, and technological advancements over the years. It's ideal for understanding the broader smartphone market and tracking industry shifts.

    2. **User-Centric Data Analysis**: Designed with potential buyers in mind, this section emphasizes key features that matter most to consumers, such as **price range**, **camera quality**, and **battery life**.
    - **Phone Age**: For a more relevant analysis, only smartphones launched after **October 2021** are included. Additionally, we account for the varying durations of software support across brands:
    - **Apple** devices typically receive **5+ years of support**, **High-end Samsung** models receive **3-4 years** of support.
    - **Budget Android brands** like **Xiaomi** and **Realme** may have shorter support windows.
    - **Season of Release**: Smartphones launched in the **Q4 (October–December)** are prioritized for their longer market relevance, as these models often benefit from the holiday season sales and extended shelf life.
       
    As a result of these filters, **1262 smartphones** are considered in the User-Centric Analysis, reflecting the most relevant options for today's buyers.

    👉 **Use the sidebar navigation** to explore different analysis sections and filter the data based on your preferences. The app is designed to help you discover key insights about the smartphone market.

    ### Data Source
    The data used in this app comes from **Smartprix**, which aggregates smartphone specifications, pricing, and reviews from various sources. Only smartphones meeting the criteria outlined above have been included in the analysis, ensuring the data’s relevance and quality.

    All insights presented are derived from publicly available information, providing users with a clear view of the current smartphone landscape.


    ### Purpose Statement

    The **Smartphone Data Analysis & Dashboard** serves as a comprehensive exploration of the smartphone market, designed to showcase my skills in **data analysis**, **data cleaning**, and **presentation**, while highlighting my curiosity and ability to learn new tools.

    By using **Streamlit**, I built an interactive dashboard, opting for it over traditional tools like Power BI or Tableau. This allowed me to create a custom visualization that reflects my **analytical approach** and demonstrates my ability to build user-friendly, data-driven solutions.

    """)


# Show Overall Analysis

elif selection == "Overall Analysis 📊":
    # Load the dataset (adjust this to the correct file path)
    file_path = r"https://raw.githubusercontent.com/soliloquy-data/Smartphone-Analysis-Dashboard/refs/heads/main/Data/data_refined.csv"  # Adjust this to your file path
    df = pd.read_csv(file_path)

    st.title("Overall Analysis")

     # Introduction Summary for Overall Analysis
    st.markdown("""
    The **Overall Analysis** section provides an in-depth examination of various aspects of the smartphone dataset. This section allows you to explore trends, patterns, and relationships across different features, brands, and price points.

    Use the navigation links below to jump to the section you're interested in:
    """)

    # Navigation Links with intros for each section
    st.markdown("""
    
    - [Visualizations of the features in the dataset](#visualizations-of-the-features-in-the-dataset)  
      Explore visual representations of key features across the dataset. This section includes visualizations that help to identify trends and distributions in the data.
      
    - [Brand Distribution](#brand-distribution)  
      Understand the distribution of smartphones across various brands. This section highlights how smartphones are spread across different manufacturers.

    - [Brand Price & Count Analysis](#brand-price-count-analysis)  
      Analyze how different brands perform in terms of price and unit counts. Here, you will find insights into the pricing dynamics and the number of devices each brand offers.

    - [Price Trends](#price-trends)  
      Examine how smartphone prices have evolved over the years. This section provides insights into the historical trends of smartphone pricing and its correlation with advancements in technology.

    - [Price Range Distribution by Brand and Year](#price-range-distribution-by-brand-and-year)  
      See how brands are represented across different price ranges. This section provides a breakdown of brand distribution within different pricing categories.

    - [Analyzing Price Growth for Phones with 5G, NFC, and Fast Charging](#analyzing-price-growth-for-phones-with-5g-nfc-and-fast-charging)  
      A deep dive into price trends for smartphones with advanced features like 5G, NFC, and fast charging. Discover how the prices have changed as these technologies became more prevalent.

    - [The Octa Core Era](#the-octa-core-era)  
      Investigate the rise of Octa-core processors and their impact on smartphone performance and pricing. This section looks at the technological shift and how it has affected the market.
    """)
    st.markdown("""
    👉 All the charts here are interactive—you can hover over the bars , pies and donuts to see more information, and the legend allows you to highlight specific items for a more focused view.
    """)

    
    # Data visualization options
    st.subheader("Visualizations of the features in the dataset")
    st.markdown("""
    In this section a comprehensive analysis of the dataset by visualizing key features and their distributions. You can explore both **categorical** and **numerical** features to understand their distribution and trends.
     """)

    #####################################################

    #### 1. Categorical Feature Analysis:
    
    # Categorical Columns 
    st.markdown("""
    ##### Categorical Feature Analysis
    In this section, you can explore the **categorical features** of the smartphones in the dataset. These features represent distinct categories or groups, such as brands, camera counts, availability of certain features, and more.
    """)
    categorical_column = ['Processor Brand', 'Number of Cores', 'Fast Charge Availability', '5G Support',
    'Number of Rear Cameras', 'Fingerprint Sensor', 'Number of Front Cameras', 'NFC Support', 'Operating System Type']
    # Select a categorical column to plot pie chart
    chosen_column = st.selectbox("Select a column to plot pie chart", categorical_column)
    # Create the DataFrame for the chosen column, and count the occurrences
    dt = df[chosen_column].value_counts().reset_index(name='Count')
    dt.columns = [chosen_column, 'Count']
    # Plot Pie Chart for the chosen column
    pr = px.pie(dt, values='Count', names=chosen_column, hover_data=['Count'],
            title=f'Pie Chart of {chosen_column}')
    st.plotly_chart(pr)
    
    #### 2. Numerical Feature Analysis:
    st.markdown("""
    ##### Numerical Feature Analysis
    After exploring the categorical features, you can select a **numerical feature** to view its distribution through a **histogram**. This helps you analyze the spread of values for attributes like RAM, camera megapixels, battery capacity, and price.
    """)
    numerical_column = [
    'ROM (GB)', 'RAM (GB)', 'Primary Camera (MP)', 'Secondary Camera (MP)', 'Total Rear Camera Megapixels',
    'Front Camera 1 (MP)', 'Front Camera 2 (MP)', 'Total Front Camera Megapixels', 'Display Size (cm)', 
    'Battery Capacity (mAh)', 'Fast Charge Capacity (W)', 'Price (INR)'
    ]
    # Select a numerical column to plot a histogram
    chosen_column = st.selectbox("Select a column to plot histogram", numerical_column)
    # Plot Histogram for the chosen numerical column
    ht = px.histogram(df, x=chosen_column, title=f'Histogram of {chosen_column}',template='plotly_dark',nbins=30)
    ht.update_layout(bargap=0.3)
    st.plotly_chart(ht)

    st.subheader("Brand Distribution")
    st.markdown("""
    The following bar chart visualizes the distribution of smartphone brands within the dataset. It shows how frequently each brand appears, offering an overview of the market share for different smartphone manufacturers. 
    
    By examining this chart, you can quickly identify which brands are most prevalent in the dataset and gain insights into their relative popularity. 
    """)   
    temp=df['Brand'].value_counts().reset_index(name='Count of Phones')
    pr = px.bar(temp, x='Brand',y='Count of Phones', title='Brand Distribution', color='Brand')
    st.plotly_chart(pr)

    #####################################################
    
    # Brand Price Plot #
    # Add Selectbox to choose a brand
    st.subheader("Brand Price & Count Analysis")
    st.markdown("""

    In this section, we analyze both the **total price** and the **count of smartphones** released by different brands over the years. By selecting a specific brand from the dropdown menu, you can observe how the total price and the number of phones released by that brand have changed year by year.

    The **interactive bar chart** allows you to explore the trends and compare how the release count and pricing have evolved for the selected brand.
    """)
    st.markdown("""
    ##### 1. Total Price Analysis
    The **bar chart** visualizes how the total price of smartphones released by the selected brand has evolved over the years. It aggregates the prices of all phones launched in each year to give an overview of the brand's pricing trend.

    - The **x-axis** represents the **Release Year** of the smartphones.
    - The **y-axis** represents the **Total Price (INR)**, which is the sum of prices for all models released in a particular year.
    - Each **block** of the bar mentions the Model Name of the Brand and its price.
    """)
    ## Update the column names according to the new names
    selected_brand = st.selectbox("Select a brand to view price trend", df['Brand'].sort_values().unique())
    # Filter the DataFrame based on the selected brand and select relevant columns
    dt = df[df['Brand'] == selected_brand][['Model Name', 'Release Year', 'Price (INR)']]
    # Create a bar plot showing the price trend for the selected brand
    bary = px.bar(dt, x='Release Year', y='Price (INR)', title=f"Increase in {selected_brand} Phone Price by Year", 
              labels={'Model Name': 'Model', 'Price (INR)': 'Phone Price (INR)'}, hover_data={'Model Name': True, 'Price (INR)': True, 'Release Year': False})
    # Format the y-axis to display prices in a more readable way
    bary.update_layout(yaxis=dict(tickformat=",.0f"))
    st.plotly_chart(bary)
    st.markdown("""
    ##### 2. Count of Phones Released
    The chart also shows the **count of phones released** by the selected brand each year. This part of the chart represents the number of different smartphone models the brand introduced during that year.

    - The **y-axis** will show the **Count of Phones**, which is the number of phones released each year.
    - Each block of the bar again reprsents the Model name of the phone.
    """)
    # Group by 'Release Year' and 'Model Name' to get the count of phones for each model per year
    dt1 = dt.groupby(['Release Year', 'Model Name']).size().reset_index(name='Count of Phones')
    # Create a bar plot with the count of phones released by the selected brand per year, partitioned by phone models
    bar = px.bar(dt1, x='Release Year', y='Count of Phones', color='Model Name', 
             title=f"Increase in {selected_brand} Phones Released Year by Year", 
             labels={'Model Name': 'Model'}, hover_data={'Model Name': True, 'Release Year': False, 'Count of Phones': False})
    st.plotly_chart(bar)

    #####################################################
    
    st.subheader("Price Range Distribution by Brand and Year")
    st.markdown("""
    Building upon the **Brand Count Analysis**, which displayed the number of smartphones released by a brand over the years, we now focus on the **price distribution** of smartphones released in specific years.

    In this section, you can select a brand and compare the price range distribution of phones for two different years. By choosing two different years, you’ll see side-by-side bar charts that showcase the distribution of phones within predefined price bins, ranging from budget-friendly options to premium models. 

    This analysis offers valuable insights into how the brand’s pricing strategy has evolved and how it has shifted its focus across different price segments over time.
    """)
    # Select brand and years for the price range distribution
    selected_brand_1 = st.selectbox("Select a brand to view count", df['Brand'].sort_values().unique())
    col1,col2=st.columns(2)
    with col1:
        selected_year_1 = st.selectbox("Select a year to view count trend", df['Release Year'].sort_values().unique())
    with col2:
        selected_year_2 = st.selectbox("Select a second year to view count trend", df[df['Release Year'] != selected_year_1]['Release Year'].sort_values().unique())

    # Define price bins and labels
    price_bins = [0, 15000, 30000, 50000, 75000, 100000, 125000, 150000, 200000]  # Price ranges (0-15k, 15k-30k, ...)
    price_labels = ['0-15k', '15k-30k', '30k-50k', '50k-75k', '75k-1L', '1L-1.25L', '1.25L-1.5L', '1.5L-2L']

    # Filter data for the first selected year and brand
    df_filtered_1 = df.loc[(df['Release Year'] == selected_year_1) & (df['Brand'] == selected_brand_1)]
    df_filtered_1['price_range'] = pd.cut(df_filtered_1['Price (INR)'], bins=price_bins, labels=price_labels, right=False)
    price_range_count_1 = df_filtered_1['price_range'].value_counts().reset_index(name='Count')

    # Filter data for the second selected year and brand
    df_filtered_2 = df.loc[(df['Release Year'] == selected_year_2) & (df['Brand'] == selected_brand_1)]
    df_filtered_2['price_range'] = pd.cut(df_filtered_2['Price (INR)'], bins=price_bins, labels=price_labels, right=False)
    price_range_count_2 = df_filtered_2['price_range'].value_counts().reset_index(name='Count')

    # Create two columns for the side-by-side layout
    col1, col2 = st.columns(2)

    # Create the first bar chart for the first year in the first column
    with col1:
        bar_1 = px.bar(price_range_count_1, x='price_range', y='Count', title=f"Phone Price Range Distribution for {selected_year_1}",
                   labels={'price_range': 'Price Range', 'Count': 'Count of Phones'})
        st.plotly_chart(bar_1)

    # Create the second bar chart for the second year in the second column
    with col2:
        bar_2 = px.bar(price_range_count_2, x='price_range', y='Count', title=f"Phone Price Range Distribution for {selected_year_2}",
                   labels={'price_range': 'Price Range', 'Count': 'Count of Phones'})
        st.plotly_chart(bar_2)
        
    #################################################

    st.subheader('Price Trends')
    st.markdown("""
    Android devices exhibit a consistent upward trend in price, particularly in the last few years, driven by more premium options entering the market.
    
    iOS devices, on the other hand, have a larger price range and show more significant fluctuations in price, with a substantial jump between 2014 and 2018 as Apple introduced newer, more expensive models reflecting Apple's premium positioning and innovation.
    
    The price gap between Android and iOS remains wide, with **iOS devices positioning themselves in the premium segment**, while **Android continues to cater to a broader spectrum of prices**, including both budget and premium models.
    
    
    """)
    # For Android devices
    temp_android = df[df['Operating System Type'] == 'Android']
    temp_android = temp_android.groupby('Release Year')['Price (INR)'].mean().reset_index()
    temp_android['os_type'] = 'Android'  # Labeling the operating system

    # For iOS devices
    temp_ios = df[df['Operating System Type'] == 'iOS']
    temp_ios = temp_ios.groupby('Release Year')['Price (INR)'].mean().reset_index()
    temp_ios['os_type'] = 'iOS'  # Labeling the operating system

    # Combine both Android and iOS datasets
    combined_temp = pd.concat([temp_android, temp_ios])

    # Plotting the price trends
    fig = px.line(combined_temp, x='Release Year', y='Price (INR)', color='os_type',
              title="Price Trends for Android and iOS Devices Over the Years",
              labels={'Price (INR)': 'Average Price', 'Release Year': 'Release Year'},
                line_shape='linear', color_discrete_sequence=['#FF007F','#00BFFF'])
    st.plotly_chart(fig)
    st.markdown("""
    The effect of pandemic appears to have temporarily influenced the pricing trend. For Android, the shift to premium models continued, while for iOS, the pandemic led to a brief price drop, followed by a rebound in the post-pandemic period, particularly for premium iPhones.
    
    By 2024, Android devices have seen substantial price increases, with an average price of ₹28,188, signaling a shift toward more premium offerings. Meanwhile, iOS devices have seen even higher price points, averaging ₹121,207 in 2024, reaffirming their position in the premium segment.
    """)
    
    st.markdown("""<div style="text-align: center;font-size: 20px; font-weight: bold;">Explore Average Price Trends of Selected Brands Over Time </div>""", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    User can explore the price trends of various brands over time by selecting one or more brands, you can see how their average prices have changed year by year. 
    
    This can be particularly helpful for understanding pricing strategies, brand positioning, or how the prices of different brands compare within a particular time period.
    """)
    selected_brands = st.multiselect("Select  brands to view average price trends",df['Brand'].sort_values().unique())
    if len(selected_brands) > 0:
         filtered_df = df[df['Brand'].isin(selected_brands)]
         price_trends = filtered_df.groupby(['Release Year', 'Brand']).agg(mean_price=('Price (INR)', 'mean')).reset_index()
         fig = px.line(price_trends, x='Release Year', y='mean_price', color='Brand',
                  title="Average Price Trends for Selected Brands Over the Years",
                  labels={'mean_price': 'Average Price', 'release_year': 'Release Year'})
         st.plotly_chart(fig)
    else:
        st.write("Please select brand to view the trends.")

    #####################################################

    st.subheader("Analyzing Price Growth for Phones with 5G, NFC, and Fast Charging")
    st.markdown("""
    In this section, analyze the price trends of smartphones that have 5G, NFC, and Fast Charging features. You can choose a feature and view how the minimum price of smartphones with that feature has evolved over time.
    
    This analysis helps uncover how the introduction and proliferation of these features influence smartphone pricing. 
    
    When you hover over the points on the line chart, it will display additional details such as:
    - Model Name: The name of the smartphone model that corresponds to the minimum price for that year.
    -Minimum Price: The lowest price recorded for that smartphone in that specific year.
    """)
    # Updated feature list based on renamed columns
    feature = ['Fast Charge Availability', '5G Support', 'NFC Support']
    select_feature = st.selectbox("Select a feature to view the min price trend", feature)
    # Filter the data for phones with the selected feature
    temp_df = df[df[select_feature] == 'Yes'][['Release Year', 'Price (INR)', 'Brand', 'Model Name']]
    # Group by 'Release Year', find the minimum price, and get the phone name for the minimum price
    df_grouped = temp_df.loc[temp_df.groupby('Release Year')['Price (INR)'].idxmin()][['Release Year', 'Price (INR)', 'Model Name']].reset_index(drop=True)
    # Create a line plot to show the trend of prices over the years
    fig = px.line(df_grouped, x='Release Year', y='Price (INR)',
              title=f'Price Trend of Phones with {select_feature} over Time',
              labels={'Release Year': 'Release Year', 'Price (INR)': 'Minimum Price (INR)'},
              markers=True, hover_data={'Price (INR)': True, 'Model Name': True},
              line_shape='spline', color_discrete_sequence=['#FF007F'])  # Include name on hover
    st.plotly_chart(fig)
    # Multi-select for brands
    st.markdown("""
    Also choose brands to compare the price trends of their phones with the selected feature.
    """)
    selected_brands = st.multiselect("Select brands to compare", df['Brand'].sort_values().unique())
    if len(selected_brands) > 0:
        temp_df = df[df[select_feature] == 'Yes'][['Release Year', 'Price (INR)', 'Brand', 'Model Name']]
        temp_df_brands = temp_df[temp_df['Brand'].isin(selected_brands)]
        # Group by 'Release Year' and get the minimum price for each brand, then reset the index
        df_grouped = temp_df_brands.loc[temp_df_brands.groupby(['Release Year', 'Brand'])['Price (INR)'].idxmin()]\
                               [['Release Year', 'Price (INR)', 'Brand', 'Model Name']].reset_index(drop=True)
        # Create a line plot with the selected brands
        fig = px.line(df_grouped, x='Release Year', y='Price (INR)', color='Brand',
                  title=f'Price Trend of Phones for Selected Brands with {select_feature} Over Time',
                  labels={'Release Year': 'Release Year', 'Price (INR)': 'Minimum Price (INR)', 'Brand': 'Brand'},
                  markers=True, hover_data={'Price (INR)': True, 'Model Name': True}, line_shape='spline')
        st.plotly_chart(fig, key="price_trend_chart_{}".format("_".join(selected_brands)))

    else:
        st.warning("Please select at least one brand to compare.")

    #####################################################
    
    st.subheader('The Octa Core Era')
    st.markdown("""
    The smartphone market has witnessed significant advancements in processor technology over the years. One of the most notable trends is the shift towards Octa-Core processors primarily in Android phones, 
    driven by increasing demands for better multitasking, higher performance, and more efficient power management and also its versatilty to support from budget, mid-range and high-end smartphones.

    This analysis sheds light on how this transition is reflected in the pricing trends and market share of these processors over time.
    """)
    

    # Filter the dataset by different years
    df_1 = df[df['Release Year'] <= 2016]
    df_2 = df[(df['Release Year'] <= 2020) & (df['Release Year'] >= 2017)]
    df_3 = df[df['Release Year'] >= 2021]

    # Plot for the years 2012-2016
    fig = px.bar(df_1.groupby('Number of Cores')['Processor Brand'].value_counts().reset_index(),
             x='Number of Cores', y='count', color='Processor Brand',
             title="Core Count vs Processor Brand Distribution (2012-2016)")
    fig.update_layout(xaxis_title='Number of Cores', yaxis_title='Count of Processors')
    st.plotly_chart(fig)

    st.markdown("""
    In the early years (2012-2016), processors with fewer cores such as Dual-Core dominated the market and no exact trend can be seen.
    """)

    # Plot for the years 2017-2020
    fig = px.bar(df_2.groupby('Number of Cores')['Processor Brand'].value_counts().reset_index(),
             x='Number of Cores', y='count', color='Processor Brand',
             title="Core Count vs Processor Brand Distribution (2017-2020)")
    fig.update_layout(xaxis_title='Number of Cores', yaxis_title='Count of Processors')
    st.plotly_chart(fig)

    st.markdown("""
    From 2017 to 2020, there was a clear transition towards Octa-Core processors as brands began to offer more powerful and efficient options to meet the growing needs of consumers.
    """)

    # Plot for the years 2021-2024
    fig = px.bar(df_3.groupby('Number of Cores')['Processor Brand'].value_counts().reset_index(),
             x='Number of Cores', y='count', color='Processor Brand',
             title="Core Count vs Processor Brand Distribution (2021-2024)")
    fig.update_layout(xaxis_title='Number of Cores', yaxis_title='Count of Processors')
    st.plotly_chart(fig)

    st.markdown("""
    A near-complete shift towards Octa-Core processors, now the standard for most devices.
    """)

    st.markdown("""
    Following the analysis of core count distributions across different time periods,lets now extend our focus to the more recent period from **2021 to 2024** to dive deeper into how **Octa-Core processors** have evolved, 
    particularly in terms of pricing, brand adoption, and market trends.
    
    ##### The table below provides a detailed breakdown of several **Octa-Core processor brands**:
    """)
    # Filter the dataset for Octa-Core processors
    temp_0 = df_3[df_3['Number of Cores'] == 'Octa']
    # Group by processor brand and aggregate the price information
    temp_0 = temp_0.groupby('Processor Brand').agg({'Price (INR)': ['mean', 'median', 'min', 'max', 'count']}).reset_index()
    temp_0 = np.round(temp_0, 0)
    # Rename the columns for easier access
    temp_0.columns = ['Processor Brand', 'Mean Price', 'Median Price', 'Min Price', 'Max Price', 'Count']
    # Calculate the variance (max - min) for price
    temp_0['Variance (Max-Min)'] = temp_0['Max Price'] - temp_0['Min Price']
    # Reset index and set 'Processor Brand' as index for better readability
    temp_0.reset_index(drop=True, inplace=True)
    temp_0.set_index('Processor Brand', inplace=True)
    # Display the table sorted by 'Count', 'Variance (Max-Min)', and 'Mean Price'
    st.write(temp_0.sort_values(by=['Count', 'Variance (Max-Min)', 'Mean Price'], ascending=[False, False, True]))
    st.markdown("""
    
    The data reveals how these two brands— **Snapdragon** and **MediaTek Dimensity**—dominate the market, both in terms of volume and pricing range

    Other brands such as MediaTek Helio, Unisoc, and Samsung Exynos have smaller counts and more varied price ranges, indicating either niche positioning or lower market penetration compared to the top two brands.

    The variance values also illustrate significant price differences within these brands, especially **Snapdragon**, where the price spread is the widest, suggesting diverse offerings catering to different market segments.
    """)

    st.markdown("""
    Seeing as how **Snapdragon** and **MediaTek Dimensity** dominate the market,let us dive deeper to see:
    - Which processor models among them are used more and the minimum price of the phones containing the models,
    - The size of RAM they support
    - And also figure out if certain brands of phones use more Snapdragon or MediaTek processors.
    """)
    

    st.markdown("""<div style="text-align: center;font-size: 25px; font-weight: bold;">Processor Model Distribution </div>""", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    # Filter for Snapdragon Octa-Core processors
    temp = df_3[(df_3['Number of Cores'] == 'Octa') & (df_3['Processor Brand'] == 'Snapdragon')]
    # Group by processor model and aggregate count and minimum price
    temp1 = temp.groupby('Processor Model').agg({'Price (INR)': ['count', 'min']}).reset_index()
    temp1.columns = ['Processor Model', 'Count', 'Min Price']
    # Create a bar plot for Snapdragon Octa-Core processor models
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(25, 13))
    sns.barplot(data=temp1, x='Processor Model', y='Count', hue='Min Price', palette='plasma', ax=ax)
    ax.set_xlabel('Processor Model', fontsize=25)
    ax.set_ylabel('Count of Processors', fontsize=25)
    ax.set_title('Count vs Processor Model (Snapdragon Octa-Core)', fontsize=25)
    plt.xticks(rotation=45, ha="right", fontsize=23)
    plt.yticks(rotation=45, ha="right", fontsize=23)
    plt.legend(fontsize=25, title="Min Price", title_fontsize=23, loc="upper right", markerscale=7)
    plt.tight_layout()
    st.pyplot(fig)
    
    # Filter for MediaTek Dimensity Octa-Core processors
    temp = df_3[(df_3['Number of Cores'] == 'Octa') & (df_3['Processor Brand'] == 'MediaTek Dimensity')]
    # Group by processor model and aggregate count and minimum price
    temp1 = temp.groupby('Processor Model').agg({'Price (INR)': ['count', 'min']}).reset_index()
    temp1.columns = ['Processor Model', 'Count', 'Min Price']
    # Create a bar plot for MediaTek Dimensity Octa-Core processor models
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(23, 12))
    sns.barplot(data=temp1, x='Processor Model', y='Count', hue='Min Price', palette='plasma', ax=ax)
    ax.set_xlabel('Processor Model', fontsize=25)
    ax.set_ylabel('Count of Processors', fontsize=25)
    ax.set_title('Count vs Processor Model (MediaTek Dimensity Octa-Core)', fontsize=25)
    plt.xticks(rotation=45, ha="right", fontsize=23)
    plt.yticks(rotation=45, ha="right", fontsize=23)
    plt.legend(fontsize=23, title="Min Price", title_fontsize=20, loc="upper right", markerscale=5)
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("""
    
    - Snapdragon tends to have a broader spread of devices across budget and mid-range segments, with a stronger focus on high-end devices in the 8 series.
    
    - MediaTek also offers a variety of processors across budget and mid-range segments, but has fewer high-end options. 
    It has gained popularity in the mid-range and budget market, with a significant focus on affordable devices.
    
    Both brands have processors covering budget (₹5,000 - ₹15,000), mid-range (₹15,000 - ₹30,000), and high-end (₹30,000 and above) markets, 
    but **Snapdragon** leads in the high-end space with its 8 series processors. **MediaTek focuses** more on the budget and mid-range with models like the 1200, 1300, and 6100.
    """)

    st.markdown("""<div style="text-align: center;font-size: 25px; font-weight: bold;">RAM Distribution </div>""", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        temp = df_3[(df_3['Number of Cores'] == 'Octa') & (df_3['Processor Brand'] == 'Snapdragon')]
        ram_distribution = temp.groupby('RAM (GB)').agg(price=('Price (INR)', 'mean'), count=('RAM (GB)', 'size')).reset_index()
        ram_distribution.rename(columns={'price': 'Mean Price'}, inplace=True)
        ram_distribution['Mean Price'] = ram_distribution['Mean Price'].round(0)
        fig = px.pie(ram_distribution, names='RAM (GB)', values='count', title="Distribution of RAM's for Octa-core Snapdragon",
                 hover_data={'Mean Price': True}, hole=0.4)
        st.plotly_chart(fig)
    with col2:
        temp = df_3[(df_3['Number of Cores'] == 'Octa') & (df_3['Processor Brand'] == 'MediaTek Dimensity')]
        ram_distribution = temp.groupby('RAM (GB)').agg(price=('Price (INR)', 'mean'), count=('RAM (GB)', 'size')).reset_index()
        ram_distribution.rename(columns={'price': 'Mean Price'}, inplace=True)
        ram_distribution['Mean Price'] = ram_distribution['Mean Price'].round(0)
        fig = px.pie(ram_distribution, names='RAM (GB)', values='count', title="Distribution of RAM's for Octa-core MediaTek",
                 hover_data={'Mean Price': True}, hole=0.4)
        st.plotly_chart(fig)
        
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
        * The 8 GB RAM size is the most popular for Snapdragon devices, reflecting its balance of performance and affordability in the mid-range category.
        
        * As the RAM size increases, the mean price also increases significantly, devices move into the premium segment, with 16 GB and 18 GB RAM typically found in flagship devices.
        """)

    with col4:
        st.markdown("""
        * MediaTek's pricing strategy is focused on providing affordable devices across various RAM sizes, particularly for mid-range and high-end models. Their devices tend to be more budget-friendly compared to Snapdragon, especially in the 12 GB and 16 GB RAM categories.

        * MediaTek’s strength lies in affordable devices, while also having a growing presence in the premium and high-end markets. The 6 GB and 8 GB RAM configurations offer the best balance of cost and performance.
        """)
        
    st.markdown("""
    * Mid Range Market : Both Snapdragon and MediaTek are heavily focused on the mid-range market, with 8 GB RAM being the most popular choice. However, **Snapdragon** positions itself as a more premium option with higher prices for devices in the same RAM categories.

    * Price Difference: **MediaTek** tends to offer more affordable options at similar RAM configurations, particularly in the mid-range, making it appealing to consumers looking for value for money. Snapdragon devices are more expensive at equivalent RAM sizes, reflecting the premium nature of many Snapdragon-powered devices.

    * High-End Segment: **Snapdragon dominates the high-end market**, offering more devices with 12 GB and 16 GB RAM at significantly higher price points, positioning itself in the flagship or gaming phone space.  
    """)


    
    st.markdown("""<div style="text-align: center;font-size: 25px; font-weight: bold;">Brand Distribution </div>""", unsafe_allow_html=True)
    col5, col6 = st.columns(2)
    with col5:
        temp = df_3[(df_3['Number of Cores'] == 'Octa') & (df_3['Processor Brand'] == 'Snapdragon')]
        brand_distribution = temp.groupby('Brand').agg(price=('Price (INR)', 'mean'), count=('Brand', 'size')).reset_index()
        brand_distribution.rename(columns={'price': 'Mean Price'}, inplace=True)
        brand_distribution['Mean Price'] = brand_distribution['Mean Price'].round(0)
        fig = px.pie(brand_distribution, names='Brand', values='count', title="Distribution of Brands for Octa-core Snapdragon",
                 hover_data={'Mean Price': True}, hole=0.4)
        st.plotly_chart(fig)
    with col6:
        temp = df_3[(df_3['Number of Cores'] == 'Octa') & (df_3['Processor Brand'] == 'MediaTek Dimensity')]
        brand_distribution = temp.groupby('Brand').agg(price=('Price (INR)', 'mean'), count=('Brand', 'size')).reset_index()
        brand_distribution.rename(columns={'price': 'Mean Price'}, inplace=True)
        brand_distribution['Mean Price'] = brand_distribution['Mean Price'].round(0)
        fig = px.pie(brand_distribution, names='Brand', values='count', title="Distribution of Brands for Octa-core MediaTek",
                 hover_data={'Mean Price': True}, hole=0.4)
        st.plotly_chart(fig)

    col7, col8 = st.columns(2)
    with col7:
        st.markdown("""
    * Samsung leads in terms of both volume and premium positioning. This suggests that **Snapdragon-powered Samsung devices** are predominantly in the premium segment

    * Xiaomi, vivo, and realme have a solid market share and cater mainly to the mid-range to budget segments.

    * Motorola, POCO, and OPPO are positioned in the budget and mid-range markets, with affordable pricing to attract a broader consumer base. 
    """)
        
    with col8:
        st.markdown("""
    * MediaTek provides a diverse range of devices from affordable to premium, with a strong presence in the mid-range and budget segments.

    * Realme and vivo dominate the mid-range segment, with vivo focusing slightly more on premium features and realme providing affordable options.

    * Doogee, Ulefone, and Blackview focus on rugged or specialized markets, offering higher prices for premium, durable devices.

    """)
    st.markdown("""
    Snapdragon has a stronger presence in the premium market and delivers more diverse performance, while MediaTek has carved out a niche for itself in the mid-range to budget segment, offering value-driven options that perform well for their price.
    """)
        
    
    ##############################################################################################################################

   # Show User-centric Analysis
elif selection == "User-centric Analysis 👥":
    st.title("User-centric Analysis")
    file_path_1=r"https://raw.githubusercontent.com/soliloquy-data/Smartphone-Analysis-Dashboard/refs/heads/main/Data/data_refined_user.csv"
    df1 = pd.read_csv(file_path_1)
    st.markdown("""

    Welcome to the **Smartphone Selection Tool** – an interactive platform designed to help you find the ideal smartphone that meets your exact preferences and needs.

    This analysis focuses on key factors that matter to most users :

    - **Your Smartphone, Your Criteria**: Filtering by Brand , Release Year, and Price Range to narrow down the best options based on your preferences and budget.
  
    - **Top 7's By Key Features** : Feature Selection to showcase smartphones with the highest specifications in each year and brand, helping you compare the most feature-rich options available.

    With these tools, you can find a smartphone that perfectly fits your needs, whether you're looking for budget-friendly choices or high-end devices with the latest features.

    """)


    # Filter data based on user input
    st.subheader("Your Smartphone, Your Criteria")

    st.markdown(""" 
    Use the filters below to explore smartphones based on your specific criteria:

    - **Brand**: Select your preferred brand, or view options from a variety of manufacturers.
    - **Release Year**: Filter devices based on their release year to track the evolution of smartphone technology.
    - **Price Range Breakdown**: Smartphones range from budget-friendly options below ₹10,000 to premium models priced up to ₹2,00,000, select a price range to view devices within that category and discover which options best match your needs.

    The data is dynamically filtered based on your selections, providing you with a tailored list of smartphones to help you make an informed decision.

    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        brand_options = ['All Brands'] + list(df1['Brand'].unique())
        selected_brand = st.selectbox("Select a brand", brand_options)
        if selected_brand != 'All Brands':
            df_brand = df1[df1['Brand'] == selected_brand]
        else:
            df_brand = df1  # Handle 'All Brands' case

    with col2:
        year_options = ['All years'] + list(df1['Release Year'].unique())
        selected_year = st.selectbox("Select a year", year_options)
        if selected_year != 'All years':
            df_year = df_brand[df_brand['Release Year'] == selected_year]
        else:
            df_year = df_brand  # Handle 'All years' case

    with col3:
        price_bins_1 = [0, 10000, 15000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 125000, 150000, 200000]
        price_labels_1 = ['0-10k', '10k-15k', '15k-20k', '20k-30k', '30k-40k', '40k-50k', '50k-60k', '60k-70k', '70k-80k', '80k-90k', '90k-1L', '1L-1.25L', '1.25L-1.5L', '1.5L-2L']
        selected_price_range = st.selectbox("Price Range", price_labels_1)
    
    if selected_price_range == "1.25L-1.5L":
        st.write("🎉 You Sassy Rich Member of Society 🎉")
        st.snow()  # Trigger the Streamlit built-in snow effect
    elif selected_price_range == "1.5L-2L":
        st.write("🎉 You Sassier Rich Member of Society 🎉")
        st.snow()  # Trigger the Streamlit built-in snow effect

    # Apply price bins to the data
    df_year['Price Range'] = pd.cut(df_year['Price (INR)'], bins=price_bins_1, labels=price_labels_1, right=False)

    # Filter data based on the selected price range
    filtered_df = df_year[df_year['Price Range'] == selected_price_range]

    # Sort data by 'Price (INR)'
    filtered_df = filtered_df.sort_values(by='Price (INR)', ascending=False)

    # Assign the index to 'Model Name'
    filtered_df.index = filtered_df['Model Name']

    # Show the filtered data with selected columns
    st.write(filtered_df[['Brand', 'Price (INR)','Processor Brand', 'Processor Model', 'Number of Cores', 'ROM (GB)', 
                      'RAM (GB)', 'Primary Camera (MP)', 'Secondary Camera (MP)', 'Tertiary Camera (MP)', 
                      'Quaternary Camera (MP)', 'Quinary Camera (MP)', 'Total Rear Camera Megapixels', 
                      'Number of Rear Cameras', 'Front Camera 1 (MP)', 'Front Camera 2 (MP)', 'Front Camera 3 (MP)', 
                      'Total Front Camera Megapixels', 'Number of Front Cameras', 'Display Type', 
                      'Display Size (cm)', 'Battery Capacity (mAh)', 'Fast Charge Availability', 
                      'Fast Charge Capacity (W)', 'Operating System Type', 'Operating System Version', 
                      '5G Support', 'Fingerprint Sensor', 'NFC Support' ]])
    st.markdown("""
    
    ##### Visualize Smartphone Data Through a Bar Graph

    To better understand how different features of smartphones relate to their price, you can visualize the data using a bar chart.

    - **Price vs Model Name**: The bar chart will display the price of each smartphone on the y-axis and the model name on the x-axis.
    
    - **Color by Feature**: Select a feature from the dropdown menu to color the bars dynamically. This will give you a visual representation of how the selected feature varies across different models within your chosen brand and price range.  
    """)
    
    # Streamlit user input for selecting a feature to color the bars
    feature_options = ['RAM (GB)', 'ROM (GB)','Processor Brand' ,'Battery Capacity (mAh)','Total Front Camera Megapixels','Total Rear Camera Megapixels',
                      'Display Size (cm)','Fast Charge Capacity (W)','5G Support', 'Fingerprint Sensor', 'NFC Support']
    selected_feature = st.selectbox("Select a feature to color the bars", feature_options)
    filtered_df[selected_feature] = filtered_df[selected_feature].astype(str)
    # Create a bar plot with dynamic color based on the selected feature
    if  selected_brand != 'All Brands' and selected_year != 'All years' :
        fig = px.bar(filtered_df, x='Model Name', y='Price (INR)',color=selected_feature, 
        title=f"Price vs Model Name Colored by {selected_feature}",
        labels={"Price (INR)": "Price (INR)", "Model Name": "Phone Model"},
        color_continuous_scale='Cividis')  # You can change the color scale if needed
        st.plotly_chart(fig)
        
    else:
        st.write("Please select both brand and year to see the chart.")

    #####################################################
    
    st.subheader("Top 7's By Key Features")
    st.markdown("""
    In this section, you can explore the **top 7 smartphones** based on the **most important features** for a given year. Whether you're looking for a phone with the **best RAM**, **largest storage**, **most powerful camera**, or **longest battery life**, we’ve got you covered.

    1. **Select a Year**: Choose the year you want to explore. This allows you to filter phones released within that specific time frame.
    2. **Select a Brand**: Choose a brand to narrow down the list, or select 'All Brands' to see phones from all manufacturers.
    3. **View Top 7 Smartphones**: Based on your selection, the top 7 smartphones will be displayed, sorted by their **performance** in various categories such as **RAM**, **ROM**, **camera capabilities**, **battery**, and **fast charging** etc. Use the fullscreen option in right-top corner of the table for a better view.

    """)


    # Dropdown for selecting year
    selected_year = st.selectbox("Select a Year to view the 7 best phones with highest features", df1['Release Year'].unique())

    # Dropdown for selecting brand
    selected_brand = st.selectbox("Select a Brand to view the 7 best phones with highest features", ['All Brands'] + list(df1['Brand'].unique()))

    # Filter phones by selected year and brand
    if selected_brand != 'All Brands':
        df_filtered = df1[(df1['Release Year'] == selected_year) & (df1['Brand'] == selected_brand)]
    else:
        df_filtered = df1[df1['Release Year'] == selected_year]

    # Sort by the highest features
    top_7 = df_filtered.sort_values(
    by=['ROM (GB)', 'RAM (GB)', 'Total Rear Camera Megapixels', 'Number of Rear Cameras', 'Total Front Camera Megapixels',
        'Number of Front Cameras', 'Battery Capacity (mAh)', 'Fast Charge Availability'],
    ascending=[False, False, False, False, False, False, False, False]
    )[['Model Name', 'Price (INR)', 'ROM (GB)', 'RAM (GB)', 'Processor Brand', 'Total Rear Camera Megapixels', 
   'Number of Rear Cameras', 'Total Front Camera Megapixels', 'Number of Front Cameras', 'Battery Capacity (mAh)', 
   'Fast Charge Availability', '5G Support', 'NFC Support']].head(7)

    top_7.reset_index(drop=True, inplace=True)
    top_7.set_index('Model Name', inplace=True)  # Assigning Model Name to index

    # Show top 7 phones
    st.write(top_7)


    # Feature selection dropdowns
    st.markdown("""<div style="text-align: center;font-size: 20px; font-weight: bold;">Compare Top 7 Smartphones by Specific Features </div>""", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    In this section, you can **narrow down the top 7 smartphones** by selecting up to **3 key features** that matter most to you. Whether you're interested in **RAM**, **storage capacity**, **camera quality**, or **battery life**, you can customize your comparison to highlight the phones that excel in those areas.

    This allows you to focus on the specific features that are most important, enabling for a more personalized comparison.
    """)
    
    features = ['ROM (GB)', 'RAM (GB)', 'Processor Brand', 'Total Rear Camera Megapixels', 'Number of Rear Cameras',
            'Total Front Camera Megapixels', 'Number of Front Cameras', 'Battery Capacity (mAh)','Fast Charge Availability',
            '5G Support', 'NFC Support']

    # Use multiselect for selecting multiple features (limit to 3 selections)
    selected_features = st.multiselect("Choose up to 3 features to view top 7 smartphones",features,
    max_selections=3) # Limit the number of features to 3


    # Ensure that at least one feature is selected
    if len(selected_features) > 0:
    # Sort by the selected features, with descending order for the features and ascending for Price (INR)
        top_7_sorted = top_7.sort_values(
        by=selected_features + ['Price (INR)'],
        ascending=[False] * len(selected_features) + [True]).head(7)  # Features descending, Price ascending
        st.write(f"##### Top 7 Smartphones Based on {', '.join(selected_features)}")
        # Display the top 7 smartphones with their selected features and price
        st.write(top_7_sorted[['Price (INR)'] + selected_features])

        st.write("Please select at least one feature to compare the top 7 smartphones.")

