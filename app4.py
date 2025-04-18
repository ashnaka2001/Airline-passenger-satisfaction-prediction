import streamlit as st
import pickle
from PIL import Image
import base64

from pygments.styles.dracula import background


# Function to add a background image
def add_background_image(image_file):
    with open(image_file, "rb") as file:
        base64_image = base64.b64encode(file.read()).decode()
        background_style = f"""
            <style>
            .stApp {{
                background-image: url(data:image/jpeg;base64,{base64_image});
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
        
            }}
            .stSidebar {{
                background-color: rgba(30, 30, 30, 0.9); /* Dark background for sidebar */
                border-radius: 10px;
            }}
            h1, h2, h3 {{
                font-family: 'Comic Sans MS', sans-serif;
                color: ##7B3F00; /* Lime Green */
                text-align: center;
            }}
            label, p, div {{
                font-size: 18px;
                font-family: 'Georgia', sans-serif;
                color: #FF2400; /* Orange-Red */
                 font-weight: bold; 
            }}
            .stButton>button {{
                background-color: #80CBC4; /* Light Teal */
                color:white;
                font-size: 30px;
                border-radius: 40px;
            }}
            .prediction-box {{
                background-color: Brown;
                color: black;
                padding: 15px;
                font-size: 20px;
                border-radius: 10px;
                text-align: center;
                margin-top: 20px;
                
            

             st.markdown("""

        st.markdown(background_style, unsafe_allow_html=True)

# Main application function
def main():
    st.sidebar.title('🚀 Main Menu')
    page = st.sidebar.selectbox('Choose an option:', ['🏡 Home', '📊 Prediction','📑 Airline Insights'])

    if page == '🏡 Home':
        st.title("✨AIRLINE PASSENGER SATISFACTION PREDICTION APP✈️")
        add_background_image("64ebefbbd558d77f1a1e0d01a4e050c1.jpg")
        img = Image.open("image1.jpg")
        st.image(img, width=600)
        st.markdown("""
        ### 🤔 What is this app?
        - Helps airlines understand factors that influence passenger satisfaction.
        - Use the **Prediction** tab to try it out!
        """)

    elif page == '📊 Prediction':
        add_background_image("DSC_8219a.jpg")

        st.markdown("<h1>Airline Passenger Satisfaction Predictor</h1>", unsafe_allow_html=True)
        st.subheader("🛫 Enter Passenger Details Below:")

        Type_of_Travel = st.selectbox("✈️ Type of Travel", ['Business Travel', 'Personal Travel'])
        Class = st.selectbox("🎟️ Class", ['Eco', 'Business', 'Eco Plus'])
        Flight_Distance = st.number_input("📏 Enter Flight Distance (km):", step=1.0, format="%f")

        # Rating sliders
        ratings = {
            "Inflight Wi-Fi Service 🖧": "Inflight_wifi_service",
            "Arrival Time Convenience ⏰": "Arrival_time_convenient",
            "Food and Drink 🍴": "Food_and_drink",
            "Online Boarding 💻": "Online_boarding",
            "Seat Comfort 🪑": "Seat_comfort",
            "Inflight Entertainment 🎥": "Inflight_entertainment",
            "On-board Service 🛠️": "On_board_service",
            "Leg Room Service 🦵": "Leg_room_service",
            "Baggage Handling 🎒": "Baggage_handling",
            "Check-in Service 📩": "Checkin_service",
            "Inflight Service 🛫": "Inflight_service",
            "Cleanliness 🧼": "Cleanliness"
        }

        features = []
        for label, var in ratings.items():
            rating = st.slider(label, 0, 5, step=1)
            features.append(rating)

        # Mapping inputs
        Type_of_Travel_map = {'Business Travel': 0, 'Personal Travel': 1}
        Class_map = {'Eco': 1, 'Business': 0, 'Eco Plus': 2}

        features.insert(0, Type_of_Travel_map[Type_of_Travel])
        features.insert(1, Class_map[Class])
        features.insert(2, Flight_Distance)

        # Load scaler and model
        scaler = pickle.load(open('scaler (2).sav', 'rb'))
        model = pickle.load(open('passenger_satisfaction (1).sav', 'rb'))

        # Prediction button
        if st.button("✨ Predict Satisfaction"):
            result = model.predict(scaler.transform([features]))
            if result == 1:
                st.markdown('<div class="prediction-box">🎉 Passenger is Satisfied!</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="prediction-box">😕 Passenger is Neutral or Dissatisfied.</div>',
                            unsafe_allow_html=True)

    elif page == '📑 Airline Insights':
        add_background_image("64ebefbbd558d77f1a1e0d01a4e050c1.jpg")

        st.title("📑 Airline Passenger Satisfaction Insights")

        st.markdown("""
        ## ✈️ Understanding Passenger Satisfaction  

        Airlines are constantly working to enhance the travel experience for passengers. Satisfaction levels depend on: 

        ### 🏆 Key Factors Affecting Satisfaction:  
        - **Comfort:** Seat space, legroom, and amenities.
        - **Service Quality:** Staff responsiveness and onboard assistance.
        - **Punctuality:** Timely departures and arrivals.
        - **Entertainment & Wi-Fi:** Availability and quality of in-flight services.
        - **Food & Beverages:** Meal options and taste.


         ### 📊 Insights for Airlines:  
         - **Personalized service** increases customer loyalty and repeat passengers.  
         - **Comfort & punctuality** improvements enhance overall satisfaction.  
         - **Passenger feedback analysis** helps airlines refine services.
         - **Prioritizing key factors** boosts ratings and trust.
 
  

         ✨ Stay ahead by optimizing services for the best **passenger experience!**  
         """)

# Run the application
main()