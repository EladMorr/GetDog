import streamlit as st
from streamlit.web.cli import main
import pandas as pd
import mysql.connector
from PIL import Image

# st.markdown("https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2022-08/220805-border-collie-play-mn-1100-82d2f1.jpg")
st.set_page_config(layout="wide")

st.title("Adopt me")
st.write('''
         This platform is designed for dogs adoption.\n
         This site was established without profit and to provide a warm home for all dogs.\n
         Why buy when you can adopt.\n
         So what are you waiting for ?\n
         waiting for you: )''')

dogs_db = pd.DataFrame({
    'images': ["https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2022-08/220805-border-collie-play-mn-1100-82d2f1.jpg",
               "https://cdn-prod.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg"],
    'names': ["Toto", 'Sky'],
    'ages': [3, 6],
    'colors': ["Yellow", "Blonde"],
    'race': ["Pakinez", "Siberian Husky"],
    'about': ["Good with kids", "Everybody loves me"],
    'phone number': ['0554453215', '0564443212'],
    'owner name': ["Elad", "Meital"]
})

def get_dogs():
    for index, row in dogs_db.iterrows():
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
                'Owner Name' : row["owner name"]}
        df = pd.DataFrame(data, index=[0])
        df = df.reset_index(drop=True)

        st.dataframe(df)


get_dogs()


# # Initialize connection.
# # Uses st.experimental_singleton to only run once.
# @st.experimental_singleton
# def init_connection():
#     return mysql.connector.connect(**st.secrets["mysql"])


# conn = init_connection()

# # Perform query.
# # Uses st.experimental_memo to only rerun when the query changes or after 10 min.


# @st.experimental_memo(ttl=600)
# def run_query(query):
#     with conn.cursor() as cur:
#         cur.execute(query)
#         return cur.fetchall()


# rows = run_query("SELECT * from mytable;")

# # Print results.
# for row in rows:
#     st.write(f"{row[0]} has a :{row[1]}:")
