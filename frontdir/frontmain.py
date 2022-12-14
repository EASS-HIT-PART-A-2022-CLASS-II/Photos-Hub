import streamlit as st
from PIL import Image
import requests
import pandas as pd
import json
import base64
import io
from html.parser import HTMLParser

def main():
    new_height = 720
    st.title("Photos-Hub")
    menu = ["Home", "Pictures", "masteryi","karthus", "poppy","Champions", "Login", "Sign-Up"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.checkbox("Login"):
            st.success("Logged in as {}".format(username))

            task = st.selectbox("Task", ["Upload Picture", "Remove Picture"])
            if task == "Upload Picture":
                pass

    elif choice == "Sign-Up":
        st.subheader("Create New Account")
        new_user = st.text_input("Usernane")
        new_password = st.text_input("Password", type="password")

        if st.button("Sign Up"):
            st.success("Successfully Created Account : {}".format(new_user))
            st.info("Proceed to Login page.")

    elif choice == "Pictures":
        st.subheader("Pictures Of Champions")

        ####### PICTURE OF VI AND JINX ########
        image_path = "/app/frontdir/league-of-legends/vi-jinx.png"

        image = Image.open(image_path)
        # resizing the image to 720p
        new_width = int(new_height / image.height * image.width)
        image.resize((new_width, new_height))
        st.image(image, caption="Jinx-Vi")
        st.button("Download", key="3")

        ####### PICTURE OF MASTER YI ########
        image = Image.open("/app/frontdir/league-of-legends/masteryi.png")
        # resizing the image to 720p
        new_width = int(new_height / image.height * image.width)
        image.resize((new_width, new_height))
        st.image(image, caption="Master Yi")
        st.button("Download", key="4")

        ####### PICTURE OF KARTHUS ########
        image = Image.open("/app/frontdir/league-of-legends/karthus.png")
        # resizing the image to 720p
        new_width = int(new_height / image.height * image.width)
        image.resize((new_width, new_height))
        st.image(image, caption="Karthus")
        st.button("Download", key="5")

    elif choice == "masteryi":
        new_title = '<p style="font-family:sans-serif; color:black; font-size: 42px;">Here you can view champion information !</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.markdown("To display :red[Master-Yi], simply input 'masteryi' ")
        if st.text_input("Champion name") == "masteryi":
            dfs = []
            response = requests.get("http://backend:90/v1/champions/masteryi")
            content = json.loads(response.text)
            dfs.append(pd.DataFrame([content]))
            df = pd.concat(dfs, ignore_index=True, sort=False).transpose()

            image = Image.open("/app/frontdir/league-of-legends/masteryi.png")
            # resizing the image to 720p
            new_width = int(new_height / image.height * image.width)
            image.resize((new_width, new_height))
            st.image(image, caption="Master Yi")
            st.table(df)

    elif choice == "karthus":
        new_title = '<p style="font-family:sans-serif; color:black; font-size: 42px;">Here you can view champion information !</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.markdown("To display :green[Karthus], simply input 'karthus' ")
        if st.text_input("Champion name") == "karthus":
            dfs = []
            response = requests.get("http://backend:90/v1/champions/karthus")
            content = json.loads(response.text)
            dfs.append(pd.DataFrame([content]))
            df = pd.concat(dfs, ignore_index=True, sort=False).transpose()

            image = Image.open("/app/frontdir/league-of-legends/karthus.png")
            # resizing the image to 720p
            new_width = int(new_height / image.height * image.width)
            image.resize((new_width, new_height))
            st.image(image, caption="Karthus")
            st.table(df)

    elif choice == "poppy":
        new_title = '<p style="font-family:sans-serif; color:black; font-size: 42px;">Here you can view champion information !</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.markdown("To display :blue[Poppy], simply input 'poppy' ")
        if st.text_input("Champion name") == "poppy":      
            dfs = []
            response = requests.get("http://backend:90/v1/champions/poppy")
            json_obj = json.loads(response.text)
            content = json_obj["champion"]
            dfs.append(pd.DataFrame([content]))
            df = pd.concat(dfs, ignore_index=True, sort=False).transpose()

            st.markdown(json_obj["image"], unsafe_allow_html=True)
            st.table(df)

    elif choice == "Champions":
            new_title = '<p style="font-family:sans-serif; color:black; font-size: 42px;">Here you can display information about several champions !</p>'
            st.markdown(new_title, unsafe_allow_html=True)
            st.markdown("Try input one of the names : :red['masteryi'], :green['karthus']")
            name = st.text_input("Champion name")
            while(True):
                if(name!=None or name!= ""):
                    break
            dfs = []
            response = requests.get(url="http://backend:90/v1/champions/get-champion-by-name", params={"champion_name":name})
            content = json.loads(response.text)
            dfs.append(pd.DataFrame([content]))
            df = pd.concat(dfs, ignore_index=True, sort=False).transpose()
            image = Image.open("/app/frontdir/league-of-legends/{}.png".format(name))
            # resizing the image to 720p
            new_width = int(new_height / image.height * image.width)
            image.resize((new_width, new_height))
            st.image(image, caption="{name}")
            st.table(df)


if __name__ == "__main__":
    main()