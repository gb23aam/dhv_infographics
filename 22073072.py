#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from IPython.display import Image


# In[2]:


def read_earthquake_data(file_path):
    data = pd.read_csv(file_path)
    return data


# In[3]:


def get_top_places_affected(data):
    places = data['place'].str.split(', ').str[-1].value_counts().head(10)
    return places


# In[4]:


def get_top_magnitude_types(data):
    mag_types = data['magType'].str.split(', ').str[-1]
    top_mag_types = mag_types.value_counts().head(10)
    return top_mag_types


# In[5]:


def plot_histogram_magnitudes(data, axs):
    sns.histplot(data['mag'], bins=20, kde=True, color='skyblue', edgecolor='black', linewidth=1.2, ax=axs[0, 0])
    axs[0, 0].set_xlabel('Magnitude')
    axs[0, 0].set_ylabel('Frequency')
    axs[0, 0].set_title('Distribution of Earthquake Magnitudes', fontsize=18, fontweight='bold', backgroundcolor='lightgrey')

def plot_histogram_depths(data, axs):
    sns.histplot(data['depth'], bins=20, kde=True, color='salmon', edgecolor='black', linewidth=1.2, ax=axs[0, 1])
    axs[0, 1].set_xlabel('Depth (km)')
    axs[0, 1].set_ylabel('Frequency')
    axs[0, 1].set_title('Distribution of Earthquake Depths', fontsize=18, fontweight='bold', backgroundcolor='lightgrey')

def plot_pie_chart_places(places, axs):
    places.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=axs[1, 0], explode=(0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0), colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'], wedgeprops=dict(edgecolor='black', linewidth=1))
    axs[1, 0].set_title('Top 10 Places Most Affected by Earthquakes', fontsize=16, fontweight='bold', backgroundcolor='lightgrey')
    axs[1, 0].set_ylabel('')

def plot_bar_chart_magnitude_types(top_mag_types):
    top_mag_types.plot(kind='barh', color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])
    plt.xlabel('Count')
    plt.ylabel('Magnitude Type')
    plt.title('Distribution of Magnitude Types', fontsize=18, fontweight='bold', backgroundcolor='lightgrey')


# In[6]:


def plot_geographical_distribution(data):
    fig = plt.figure(figsize=(15, 18))
    fig.suptitle('EARTHQUAKE ANALYSIS IN 2023', fontsize=24, fontweight='bold', color='red', backgroundcolor='lightgrey')

    ax = fig.add_subplot(3, 2, (5, 6), projection=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':', edgecolor='gray')
    hb = ax.hexbin(data['longitude'], data['latitude'], gridsize=100, cmap=plt.cm.plasma_r, mincnt=1)
    plt.colorbar(hb, label='Earthquake Density', ax=ax)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('Geographical Distribution of Earthquakes by Magnitude Type', fontsize=18, fontweight='bold', backgroundcolor='lightgrey')
    ax.set_facecolor('lightgrey')  
    plt.grid(False)

    plt.tight_layout(rect=[0, 0.03, 1, 0.94])
    return fig

def save_figure(figure, file_name):
    figure.savefig(file_name, dpi=300)


# In[10]:


data = pd.read_csv('earthquakes_2023_global.csv')

data.head()

places = data['place'].str.split(', ').str[-1].value_counts().head(10)

places

mag_types = data['magType'].str.split(', ').str[-1]

top_mag_types = mag_types.value_counts().head(10)

top_mag_types

fig, axs = plt.subplots(3, 2, figsize=(15, 18))

# Set a suitable title at the top
fig.suptitle('EARTHQUAKE ANALYSIS IN 2023', fontsize=24, fontweight='bold', color='RED')

# Histogram of Magnitudes
sns.histplot(data['mag'], bins=20, kde=True, color='skyblue', edgecolor='black', linewidth=1.2, ax=axs[0, 0])
axs[0, 0].set_xlabel('Magnitude')
axs[0, 0].set_title('Distribution of Earthquake Magnitudes', fontsize=18, fontweight='bold')

# Depth Distribution
sns.histplot(data['depth'], bins=20, kde=True, color='salmon', edgecolor='black', linewidth=1.2, ax=axs[0, 1])
axs[0, 1].set_xlabel('Depth (km)')
axs[0, 1].set_title('Distribution of Earthquake Depths', fontsize=18, fontweight='bold')

# Places most affected by earthquakes
places.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=axs[1, 0], explode=(0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0), colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'], wedgeprops=dict(edgecolor='black', linewidth=1))
axs[1, 0].set_title('Top 10 Places Most Affected by Earthquakes', fontsize=16, fontweight='bold')
axs[1, 0].set_ylabel('')

# Magnitude Type Distribution
plt.subplot(324)
top_mag_types.plot(kind='barh', color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])
plt.ylabel('Magnitude Type')
plt.xlabel('Count')
plt.title('Distribution of Magnitude Types', fontsize=18, fontweight='bold')

# Geographical Distribution of Earthquakes by Magnitude Type
ax = fig.add_subplot(3, 2, (5, 6), projection=ccrs.PlateCarree())
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':', edgecolor='gray')
hb = ax.hexbin(data['longitude'], data['latitude'], gridsize=100, cmap=plt.cm.plasma_r, mincnt=1)
plt.colorbar(hb, label='Earthquake Density', ax=ax)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Geographical Distribution of Earthquakes by Magnitude Type', fontsize=18, fontweight='bold')

plt.grid(False)

plt.tight_layout(rect=[0, 0.03, 1, 0.94])

fig.savefig('earthquake_analysis_2023.png', dpi=300)


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load the data
data = pd.read_csv('earthquakes_2023_global.csv')

# Compute top places affected by earthquakes
places = data['place'].str.split(', ').str[-1].value_counts().head(10)

# Compute top magnitude types
mag_types = data['magType'].str.split(', ').str[-1]
top_mag_types = mag_types.value_counts().head(10)

# Create the figure and axes
fig, axs = plt.subplots(3, 2, figsize=(20, 23))

# Set a suitable title at the top
fig.suptitle('EARTHQUAKE ANALYSIS IN 2023', fontsize=24, fontweight='bold', color='red')

# Histogram of Magnitudes
sns.histplot(data['mag'], bins=20, kde=True, color='skyblue', edgecolor='black', linewidth=1.2, ax=axs[0, 0])
axs[0, 0].set_xlabel('Magnitude')
axs[0, 0].set_title('Distribution of Earthquake Magnitudes', fontsize=18, fontweight='bold')
axs[0, 0].text(0.5, -0.3, "This plot shows the distribution of earthquake magnitudes in 2023", ha='center', fontsize=12, transform=axs[0, 0].transAxes)

# Depth Distribution
sns.histplot(data['depth'], bins=20, kde=True, color='salmon', edgecolor='black', linewidth=1.2, ax=axs[0, 1])
axs[0, 1].set_xlabel('Depth (km)')
axs[0, 1].set_title('Distribution of Earthquake Depths', fontsize=18, fontweight='bold')
axs[0, 1].text(0.5, -0.3, "This plot displays the distribution of earthquake depths in 2023", ha='center', fontsize=12, transform=axs[0, 1].transAxes)

# Places most affected by earthquakes
places.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=axs[1, 0], explode=(0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0), colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'], wedgeprops=dict(edgecolor='black', linewidth=1))
axs[1, 0].set_title('Top 10 Places Most Affected by Earthquakes', fontsize=16, fontweight='bold')
axs[1, 0].set_ylabel('')
axs[1, 0].text(0.5, -0.3, "This pie chart depicts the distribution of earthquake occurrences in different places", ha='center', fontsize=12, transform=axs[1, 0].transAxes)

# Magnitude Type Distribution
ax = fig.add_subplot(3, 2, (3, 4))
top_mag_types.plot(kind='barh', color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])
plt.ylabel('Magnitude Type')
plt.xlabel('Count')
plt.title('Distribution of Magnitude Types', fontsize=18, fontweight='bold')
ax.text(0.5, -0.15, "This bar chart shows the distribution of different earthquake magnitude types", ha='center', fontsize=12, transform=ax.transAxes)

# Geographical Distribution of Earthquakes by Magnitude Type
ax = fig.add_subplot(3, 2, (5, 6), projection=ccrs.PlateCarree())
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':', edgecolor='gray')
hb = ax.hexbin(data['longitude'], data['latitude'], gridsize=100, cmap=plt.cm.plasma_r, mincnt=1)
plt.colorbar(hb, label='Earthquake Density', ax=ax)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Geographical Distribution of Earthquakes by Magnitude Type', fontsize=18, fontweight='bold')
ax.set_facecolor('lightgrey')  # Set background color for the map
plt.grid(False)
ax.text(0.5, -0.15, "This map illustrates the geographical distribution of earthquakes by magnitude type", ha='center', fontsize=12, transform=ax.transAxes)

# Set background color for the entire figure
fig.patch.set_facecolor('lightgrey')

plt.tight_layout(rect=[0, 0.03, 1, 0.94])

# Add student information
student_info = (
    "     \n\nName : Geetha Babu"
    "     \nStudent ID : 22073072"
)

fig.text(0.5, 0.1, student_info, ha='center', va='center', fontsize=16, wrap=True)


# Save the figure
fig.savefig('earthquake_analysis_2023.png', dpi=300)


# In[ ]:




