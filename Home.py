import streamlit as st
import pandas as pd
import time
@st.dialog("Data Collection")
def data_collection():
  county = st.text_input("Enter the name of your county:")
  town= st.text_input("Enter the name of your town:")
  if  st.button("Submit details"):
     if county and town:
      st.write(f"Excited to know that you come from {town} in {county}")
     else:
         st.write("Enter all the relevant information")
st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.write("Ronald")
st.caption("Caption")

with st.echo():
    st.write("This code should be displayed and executed")

st.divider()
st.subheader("Section 12")
st.write("---------------")

df= pd.read_csv("data.csv")
st.dataframe(df)

st.write("Editable Datafra")

st.metric("Temperature in degrees Celsius", 16, -2)

st.metric("Humidity in %", 77, 8)
if st.button("submit"):
    st.write("You can submit your details")

st.write("Give your rating")
stars = st.feedback("stars")
if stars == 0:
    st.write("You have given us a one star rating")
elif stars == 1:
    st.write("You have given us a two star rating")
elif stars == 2:
    st.write("You have given us a 3 star rating")
elif stars == 3:
    st.write("You have given us a four star rating")
elif stars == 4:
    st.write("You have given us a five star rating")
else:
    pass

terms_conditions =st.checkbox("I agree to the terms and conditions")
if terms_conditions:
    st.write("The user has given the platform authority to ")

st.toggle("Dark Mode")

gender = st.radio("Select your gender", ["Male", "Female"])
if gender == "Male":
    st.write("You have been drafted for WW3")
elif gender== "Female":
    st.write("You are required to offer medical assistance")

team = st.selectbox("Select your favourite team", ["Manchester United", "Chelsea", "Arsenal", "Liverpool"])
if team == "Manchester United":
    st.write("Flory Glory Man United")
elif team == "Chelsea":
    st.write("London is blue")
elif team == "Arsenal":
    st.write("London is red")
elif team == "Liverpool":
    st.write(" You'll never walk alone")
else:
    st.write("You don't have a favourite team")

#breakfast = st.multiselect ("What did you eat for breakfast?")


age = st.number_input("Enter your age", 1,100,2)

st.select_slider("Pick a size for your T=shirt", ["l","Xl","XXL"])

kcpe = st.slider("Enter your KCPE marks", 0, 500,300)

date = st.date_input("Enter the date you want to schedule the appointment", )

appointment_time = st.time_input("Enter the time you want to schedule the appointment",)

name = st.text_input("Enter your name here:")

if name:
    st.write(f"Hello {name}, Welcome to my Streamlit Application")
st.text_area("Enter the article here:", height=250)

uploaded_file = st.file_uploader("Upload your file here")
if uploaded_file:
    st.write("uploaded_file")

st.camera_input("Take a photo of the item")
st.image("img.png", width=300)

col1, col2, col3 = st.columns(3)
with col1:
   first_name= st.text_input("Enter your first name here:")
with col2:
    second_name= st.text_input("Enter  your second name here:")
with col3:
    third_name= st.text_input("Enter your third name here:")

dialog_box = st.selectbox("Do you want the dialog box?", ["No","Yes"])
if dialog_box == "No":
    pass
else:
    data_collection()

with st.expander("Click to see more details"):
    st.write("Some Content")
    st.write("Some Content")
    st.write("Some Content")
    st.write("Some Content")

with st.popover("Settings"):
    st.checkbox("Show Completed")

with st.sidebar:
    st.write("This is the sidebar")

with st.spinner("Running"):
   time.sleep(3)
   st.write("Task Complete")

st.progress(50)
progress_text = "Operation in Progress"
progress_bar = st.progress(0, text=progress_text)
for percent_complete in range (100):
   time.sleep(0.1)
   progress_bar.progress(percent_complete)

time.sleep(1)
progress_bar.empty()

st.toast("Welcome Home", icon="🙂")
st.balloons()
st.write("He was crowned champion! :crown:")

st.success("You have successfully signed up!")
st.info("You are currently using the free plan")
st.warning("You have not yet uploaded your passport photo")
st.error("You have entered an incorrect password")