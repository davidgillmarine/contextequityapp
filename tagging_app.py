
import streamlit as st
import pandas as pd

# Load the CSV file
df = pd.read_csv("kumu_moderators.csv")

# Define the list of tags
tag_list = ['hypothesized', 'evidenced', 'unclear', 'int.attr', 'relationships',
'wider.partic', 'gov.context', 'hist.context', 'soc.context',
'econ.context', 'eco.context', 'equitable.gov', 'moderates.impacts']

# Initialize session state to store tags
if "tags" not in st.session_state:
    st.session_state.tags = [ [] for _ in range(len(df)) ]

# Title of the app
st.title("Tagging app")

# Entry navigation
index = st.number_input("Select entry index", min_value=0, max_value=len(df)-1, value=0)

# Display the File name and To
st.write(df.loc[index, "file.name"])
st.write(df.loc[index, "To"])

# Display the description
st.subheader("Description")
st.write(df.loc[index, "Description"])

# Preselect tags from 'From' column if they match tag_list
preselected = []
from_value = str(df.loc[index, "From"])
for tag in tag_list:
    if tag in from_value.split(","):
        preselected.append(tag)

# Multiselect for tags
st.subheader("Select Tags")
selected_tags = st.multiselect("Choose tags for this entry", options=tag_list, default=st.session_state.tags[index] or preselected)

# Save tags
if st.button("Save Tags"):
    st.session_state.tags[index] = selected_tags
    st.success("Tags saved!")

# Comment field
#st.subheader("Add Comment")
#comment_input = st.text_area("Enter your comment", default=st.session_state[index,"comments"])

# Export tagged data
if st.button("Export Tagged Data to CSV"):
    tagged_df = df.copy()
    tagged_df["UserTag"] = [", ".join(tags) for tags in st.session_state.tags]
    tagged_df.to_csv("tagged_kumu_moderators.csv", index=False)
    st.success("Tagged data exported to tagged_kumu_moderators.csv")
