

import streamlit as st
import pickle
model = pickle.load(open('RF_price_predicting_model.pkl','rb'))


def main():
    string = ("Car Price Predictor ")
    st.set_page_config(page_title= string,page_icon='🚗')
    st.title("Car Price Predictor 🚗")
    st.markdown("##### Are you planning to sell your car !?\n##### So let's try evaluating the price.. 🤖 ")
    st.image("https://purepng.com/public/uploads/large/purepng.com-orange-lamborghini-aventador-coupe-carcarvehicletransportlamborghini-9615246601873c5bq.png",width = 400)
    st.write('')
    st.write('')
    years = st.number_input("In which year the car was purchased?",2000,2022,step = 1,key='year')
    Years_old = 2022-years
    
    Present_Price = st.number_input("What is the Ex-Showroom price of the car? (INR in lakhs)",0.00,60.00,step = 0.5,key='Present Price')
    Kms_Driven = st.number_input("What is the Distance covered by the car in KMS? ",0.00,60000.00,step = 500.00,key='Drove')

    Owner = st.radio("The number of owners for the car previously?",(0,1,3),key='owner')
    Fuel_Type_Petrol = st.selectbox("Fuel type of the car?", ("Petrol","Diesel","CNG"),key ='Fuel')
    if(Fuel_Type_Petrol== "Petrol"):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    elif(Fuel_Type_Petrol== "Diesel"):
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0
    
    
    Seller_Type_Individual = st.selectbox("Are you a Dealer or an Individual?",("Dealer","Individual"),key = "Dealer")
    if(Seller_Type_Individual== "Individual"):
        Seller_Type_Individual =1        
    else:
        Seller_Type_Individual =0
        
    Transmission_Manual = st.selectbox("What is the Transmission Type?",("Manual","Automatic"),key = "Manual")
    if(Transmission_Manual=="Manual"):
        Transmission_Manual=1
    else:
        Transmission_Manual=0
        
    if st.button("Estimate Price",key = "predict"):
        try:
            Model = model
            prediction = Model.predict([[Present_Price,Kms_Driven,Owner,Years_old,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,
                                         Transmission_Manual]])
            output = round(prediction[0],2)
            if output <0:
                st.warning("You will not be able to sell this car!!")
            else:
                st.success("You can sell this car for {} lakhs 👏".format(output))
        except:
            st.warning("OOPs!!Something got wrong\n Please Try again")
   



if __name__ == "__main__":
    main()