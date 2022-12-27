import streamlit as st
from streamlit.web.cli import main
import pandas as pd
import mysql.connector
from streamlit.components.v1 import html

# st.markdown("https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2022-08/220805-border-collie-play-mn-1100-82d2f1.jpg")
st.set_page_config(layout="wide")
# st.markdown(
#    f'''
#    <style>
#         p {
#         background-image: url('https://img.freepik.com/free-photo/grunge-paint-background_1409-1337.jpg?w=2000');
#         }
#    </style>
#    ''',
#    unsafe_allow_html=True)

st.title("Get a dog")
st.write('''
         This platform is designed for buying or selling dogs in a normal price.\n
        This site was established without profit and to provide a warm home for all dogs.\n
        So what are you waiting for?\n
        All the cutest dogs are waiting for you :)''')

dogs_db = pd.DataFrame({
    'images': ["https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2022-08/220805-border-collie-play-mn-1100-82d2f1.jpg",
               "https://cdn-prod.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg"],
    'names': ["Toto", 'Sky'],
    'ages': [3, 6],
    'colors': ["Yellow", "Blonde"],
    'race': ["Pakinez", "Siberian Husky"],
    'about': ["Good with kids", "Everybody loves me"],
    'phone number': ['0554453215', '0564443212'],
    'owner name': ["Elad", "Meital"],
    'price': [300, 680]
}, index=["1", "2"])

dogs_db2 = dogs_db

menu = ["Home", "Add Dog", "Edit Dog", "Delete Dog", "About"]
st.sidebar.header('Menu')
choice = st.sidebar.radio("Choose screen", menu)


def add_dog(image, name, age, color, race, about, phoneNumber, ownerName, price):
    df1 = pd.DataFrame({
        "images": image,
        "names": name
    }, index=["3"])
    dogs_db2 = dogs_db.append(df1)
    st.dataframe(dogs_db2)
    st.success("Great !!! your dog is added !")
#     st.experimental_rerun()


def get_dogs():
    st.dataframe(dogs_db2)
    for index, row in dogs_db2.iterrows():
        st.image(row["images"],
                 width=400)
        st.write("""
                                        Hello nice to meet tou :)
                                        """)
        data = {'My Name': row["names"],
                'My Age': row["ages"],
                'My Color': row["colors"],
                'My Race': row["race"],
                'About me': row["about"],
                'Owner Number': row["phone number"],
                'Owner Name': row["owner name"],
                'price': row["price"]}

        df = pd.DataFrame(data, index=[0])
        df = df.reset_index(drop=True)
        st.dataframe(df)


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


if choice == "Home":
    get_dogs()
    st.sidebar.header('Sort by price')
    st.sidebar.slider(min_value=0, max_value=1000,
                      label="Select maximum price:")

elif choice == "Add Dog":
    st.header("Add Dog")
    col1, col2 = st.columns(2)
    with col1:
        options = ["Take a picture", "Upload from computer", "URL"]
        image_input = st.selectbox("**Add a picture of your dog**", options)
        if image_input == "Take a picture":
            st.camera_input("Take a picture")
        elif image_input == "Upload from computer":
            st.file_uploader("Upload from computer")
        elif image_input == "URL":
            st.text_input("Add image from URL")
        name_input = st.text_input("**Your dog name**")
        age_input = st.number_input("**Your dog age**")
        if age_input < 0:
            st.error("**Age cannot be less than 0**")
        color_input = st.text_input("**Describe the color of your dog**")
        race_input = st.text_input("**What is the race of your dog?**")
        about_input = st.text_area("**Tell some about your dog...**")
        phone_number_input = st.text_input("**Insert your phone number**")
        owner_name_input = st.text_input("**Owner name**")
        price_input = st.text_input(
            "**What is your price? (it's better for free :))**")
        if age_input > 0:
            if st.button("Add"):
                add_dog(image_input, name_input, age_input, color_input, race_input,
                        about_input, phone_number_input, owner_name_input, price_input)
                st.session_state = False

add_bg_from_url()
