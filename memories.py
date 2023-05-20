import streamlit as st

def main():
    st.title("జ్ఞాపకాల ప్రకటన (Declaration of Memories)")
    
    st.write("Hey ~~Spoorthi~~ Bubby,")
    st.write("There are so many best moments in my college life as it is copy koduthunna anukunnav kadha, nijam cheppu ;) le le neekosam na sontha kavithvam tho raastha:")

    st.write("Dveshathi dveshamaina spoorthi ki vetakaaram tho venky vraayunadhi....")

    # st.write("You have been an incredible friend, always there to:")
    # st.write("- Lend a listening ear")
    # st.write("- Offer words of encouragement")
    # st.write("- Celebrate my victories")

    # st.write("Your kindness, empathy, and unwavering support have made a profound impact on my life.")

    # st.write("As you move on to new adventures, I have no doubt that you will:")
    # st.write("- Shine brightly")
    # st.write("- Achieve great things")
    # st.write("- Stay true to yourself")
    # st.write("- Follow your dreams")
    # st.write("- Embrace the opportunities that come your way")

    st.write("Although it's difficult to say goodbye, I am grateful for the time we've shared and the friendship we've cultivated. Distance may separate us physically, but know that you will always hold a special place in my heart.")

    st.write("Take care of yourself and know that you are loved and cherished by all who know you. Ekkuva over-thinking 🤔 chesesi ah chinna medhadu ni chitakotteyaku yeduti vallu ne gurinchi em anukuntaro ani.")

    st.write("E duniya mottham getla poyina nuv maatram aanandam ga brathikesthav beta.")
    
    st.write("Wishing you all the best in your future endeavors.")
    
    st.write("**Things I miss the most:**")

    st.write("- French Fries with u 🍟")
    st.write("- Center Fresh after D3 🍗 (E sari centerfresh ichinappudu anna anna inkokkati anna ani adagakunda anna anna voddanna ani anu 😉)")
    # st.write("E sari centerfresh ichinappudu anna anna inkokkati anna ani adagakunda anna anna voddanna ani anu 😉")
    st.write("- MIG Talks 🛫")
    
    st.write("Too much emotion... Kasepu aadukundam dha")

    image_file = "4.png"  # Replace with the path to your image file
    # button_clicked2 = st.button("Click this button to learn new word")
    # button_clicked1 = st.button("Click this button to get IIM-A/B/C/L")
    # button_clicked3 = st.button("Your best picture")

    # if button_clicked2:
    #     # Display the picture when the button is clicked
    #     st.write("New word1 Vellillu")
    #     st.write("word usage Vallu momos thineki vellillu")
    #     st.write("New word2 Sadrukunnava")
    #     st.write("word usage Luggages Sadrukunnava")
    #     button_clicked1 = st.button("Click this button to get IIM-A/B/C/L")
    #     if button_clicked1:
    #         # Display the picture when the button is clicked
    #         st.write("IIM vasthadi le ra mowa, nuv stress teeskoku ooke")
    #         button_clicked3 = st.button("Your best picture")

    button_list = ["Ne Favorites 💛", "Ne Noti Aanimuthyalu 👩‍🎤", "Ne Best Pic 🙃", "Memories 🦋"]

    for button_label in button_list:
        # st.button(button_label)
        if button_label == button_list[0]:
            if st.button(button_label):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write("**Fav Drink**")
                    st.image("5.jpg", caption='Maaza', width=200)
                with col2:
                    st.write("**Fav Dress**")
                    st.image("6.jpg", caption='Yellow Kurthi', width=200)
                with col3:
                    st.write("**Fav IPL Team**")
                    st.image("7.jpg", caption='CSK (Yellowe)', width=200)    
        if button_label == button_list[1]:
            if st.button(button_label):
                st.write("New word1: **Vellillu**")
                st.write("- word usage: Vallu momos thineki vellillu")
                st.write("New word2: **Sadrukunnava**")
                st.write("- word usage: Luggages Sadrukunnava")
        if button_label == button_list[2]:
            if st.button(button_label):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write("Ah Shock ayyava 😆")
                with col2:
                    st.image("3.jpg", caption='Ne Selfie', width=200)
                    # st.write("Ah Shock ayyava 😆")
                with col3:
                    st.write("Sorry Sorry idey last")
        if button_label == button_list[3]:
            if st.button(button_label):
                st.image(image_file, caption='First & Last Pic', use_column_width=True)
    
    st.write("**Next time aina vizag vastey cheppu prend 🫠**")
    st.markdown("<center>Bubbye mowa, until next time 🥺.</center>", unsafe_allow_html=True)
    # st.write("")

if __name__ == '__main__':
    main()



