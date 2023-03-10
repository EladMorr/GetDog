import sys
from streamlit.components.v1 import html
import pandas as pd
from streamlit.web.cli import main
import streamlit as st
from streamlit_card import card
import requests
from urllib.parse import urlparse
from pydantic import BaseModel
import json
from models import *

st.set_page_config(layout="wide")

def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://media.istockphoto.com/id/1294440250/vector/seamless-gray-pattern-with-dog-paws-and-bones.jpg?s=612x612&w=0&k=20&c=nCTuqIEW5NHVvmsPuNShXRck0_EhzMskcnCY4qd70XI=");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


init = requests.get("http://backend/v1/check")

if ("exist" in init.text) or ("created" in init.text):
    
    def edit_dog(cheap_number):
        request = requests.get("http://backend/v1/GetDogsList")
        json_obj = request.json()
        data = pd.read_json(json_obj)

        for indedx, row in data.iterrows():
            if str(row["cheap_number"]) == str(cheap_number):
                return row

        return "cheap not found.."
        
    def create_card(cheap_number, image, name, age, color, race, about, phoneNumber, ownerName, price):
        string = '''
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            .card {
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
                transition: 0.3s;
                width: 60%;
            }
            .card:hover {
                box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
            }

            .container {
                padding: 2px 16px;
            }
            
        </style>
        </head>
        <body>

        <h1># ''' + str(cheap_number) + ": " + str(name) + ''' :)</h1>
        <div class="card">
        <img src= "''' + str(image) + '''" alt="Image" style="width:100%">
        <div class="container">
            <h4><b>I'm ''' + str(age) + ''' years old</b></h4> 
            <p>My color is ''' + str(color) + '''</p> 
            <p>My race is ''' + str(race) + '''</p> 
            <p>My current owner called ''' + str(ownerName) + '''</p> 
            <p>His phone number is 0''' + str(phoneNumber) + '''</p> 
            <p>My price is ''' + str(price) + '''</p> 
            <p>Others dogs say that i'm ''' + str(about) + '''</p>
        </div>
        </div>

        </body>
        '''

        return string

    st.title("Get a dog")
    st.write('''
            This platform is designed for buying or selling dogs in a normal price.\n
            This site was established without profit and to provide a warm home for all dogs.\n
            So what are you waiting for?\n
            All the cutest dogs are waiting for you :)''')

    menu = ["Home", "Add Dog", "Edit Dog", "Delete Dog"]
    st.sidebar.header('Menu')
    choice = st.sidebar.radio("Choose screen", menu)


    def add_dog(cheap_number, image, name, age, color, race, about, phoneNumber, ownerName, price):
        r = requests.post("http://backend/v1/AddDog", json={
            'cheap_number': cheap_number,
            "image": image,
            "name": name,
            "color": color,
            "age": age,
            "race": race,
            "about": about,
            'phone_number': phoneNumber,
            'owner_name': ownerName,
            'price': price
        })

        st.success("Great, your dog is added !")


    def get_dogs(sorted_price, sorted_age):
        request = requests.get("http://backEnd/v1/GetDogsList")
        json_obj = request.json()
        data = pd.read_json(json_obj)
        data = data[(data["price"] >= sorted_price[0]) & (data["price"] <= sorted_price[1])]
        data = data[(data["age"] >= sorted_age[0]) &
                    (data["age"] <= sorted_age[1])]
        
        for index, row in data.iterrows():
            no_image = "https://artsmidnorthcoast.com/wp-content/uploads/2014/05/no-image-available-icon-6.png"
            url = row["image"]

            try:
                response = requests.head(url)
                proper_url = True if (response.status_code ==
                                    200 or response.status_code == 304) else False
                if proper_url:
                    row["image"] = url
                else:
                    row["image"] = no_image
            except:
                row["image"] = no_image

            st.markdown(create_card(row["cheap_number"],
                                    row["image"],
                                    row["name"],
                                    row["age"],
                                    row["color"],
                                    row["race"],
                                    row["about"],
                                    row["phone_number"],
                                    row["owner_name"],
                                    row["price"]), unsafe_allow_html=True)
    if choice == "Home":
        st.sidebar.header('Sort Panel')
        st.sidebar.subheader('Sort By Price')
        sorted_price = st.sidebar.slider(min_value=0, max_value=10000,
                                label="Select price range:", value=[0, 10000])
        st.sidebar.subheader('Sort By Age')
        sorted_age = st.sidebar.slider(min_value=0, max_value=20,
                                label="Select age range:", value=[0, 20])
        get_dogs(sorted_price, sorted_age)
        
    elif choice == "Add Dog":
        st.header("Add Dog")
        col1, col2 = st.columns(2)
        with col1:
            cheap_number = st.text_input("**Insert your dog cheap number**")
            image_input = st.text_input("Add image from URL")
            name_input = st.text_input("**Your dog name**")
            age_input = st.number_input(
                "**Your dog age**", min_value=0.0, step=0.1)
            color_input = st.text_input("**My color is**")
            race_input = st.text_input("**My race is**")
            about_input = st.text_area("**Tell some about your dog...**")
            phone_number_input = st.text_input("**His phone number is**")
            owner_name_input = st.text_input("**My current owner called**")
            price_input = st.text_input("**My price is**")
            if age_input > 0:
                if st.button("Add"):
                    add_dog(cheap_number, image_input, name_input, age_input, color_input, race_input,
                            about_input, phone_number_input, owner_name_input, price_input)

    elif choice == "Edit Dog":
        st.header("Edit dog")

        request = requests.get("http://backend/v1/GetDogsList")
        json_obj = request.json()
        data = pd.read_json(json_obj)

        with st.expander("View all dogs"):
            st.dataframe(data.drop(["image"], axis=1))

        search_inbox = st.text_input("**Insert dog cheap number**")
        if search_inbox:
            data = edit_dog(search_inbox)
            if str(data) == "cheap not found..":
                st.error(str(data))
            else:
                new_name = st.text_input("**Name**", data["name"])
                new_cheap_number = st.text_input(
                    "**Cheap Number**", data["cheap_number"])
                image_input = st.text_input("**Image**", data["image"])
                age_input = st.number_input(
                    "**Age**", min_value=0.0, step=0.1, value=data["age"])
                color_input = st.text_input("**Color**", data["color"])
                race_input = st.text_input("**Race**", data["race"])
                about_input = st.text_area("**About**", data["about"])
                phone_number_input = st.text_input(
                    "**Phone Number**", data["phone_number"])
                owner_name_input = st.text_input(
                    "**Owner Name**", data["owner_name"])
                price_input = st.text_input("**Price**", data["price"])

                if st.button("Save"):
                    r = requests.put("http://backend/v1/EditDog", json={
                        "cheap_number": new_cheap_number,
                        "image": image_input,
                        "name": new_name,
                        "color": color_input,
                        "age": age_input,
                        "race": race_input,
                        "about": about_input,
                        "phone_number": phone_number_input,
                        "owner_name": owner_name_input,
                        "price": price_input
                    })
                    if "Success" in r.text:
                        st.success("Success")
                    else:
                        st.error("Error")


    elif choice == "Delete Dog":
        request = requests.get("http://backend/v1/GetDogsList")
        json_obj = request.json()
        data = pd.read_json(json_obj)

        with st.expander("View all dogs"):
            st.dataframe(data.drop(["image"], axis=1))
        search_inbox = st.text_input("**Insert dog cheap number to delete:**")

        if search_inbox:
            st.info("Are you sure?")

            yes_button = st.button("YES")
            no_button = st.button("NO")
            if yes_button:
                request = requests.delete(
                    "http://backend/v1/RemoveDog/" + search_inbox)
                
                st.success("Dog deleted")
            elif no_button:
                st.success("Dog is not deleted")
else:
    st.error(init.text)
    
add_bg_from_url()
