import streamlit as st
import requests

# Define the Streamlit app
st.title("Electric Consumption Calculator")

# Fetch device list from the API
device_list_response = requests.get("http://127.0.0.1:8000/devices")
if device_list_response.status_code == 200:
    device_list = device_list_response.json()['devices_list']
   
else:
    st.error("Failed to fetch device list from the API")

# Create a multiselect widget to allow the user to select devices
selected_devices = st.multiselect("Select Electric Device", device_list)

# Create a button to calculate consumption

if st.button("Calculate Consumption"):
    if not selected_devices:
        st.warning("Please select at least one device.")
    else:
        with st.spinner('Calcul de votre conssomation en cours ...'):

        # Send the selected devices to the API
            json_input= {"device_type_conso": {}}
            for device in selected_devices:
                if device not in json_input["device_type_conso"].keys() :
                    json_input["device_type_conso"][device] = 1
                else:
                    json_input["device_type_conso"][device] += 1
                            
            consumption_data_response = requests.post("http://127.0.0.1:8000/calculate_energy", json=json_input)

            

       
            
            if consumption_data_response.status_code == 200:
                consumption_data = int(consumption_data_response.json()['energy_consumed']) + 2850 #2850 => Conso moyenne chauffage par an
                conso_moy_haute = 5300 
                conso_moy_basse = 4200
                col1, col2, col3 = st.columns(3)


                if consumption_data > conso_moy_haute:
                    st.warning("Attention votre consommation est supérieur à la moyenne")
                    col1.metric("Moyenne basse", f"{conso_moy_basse} kwh/an", f" - {(100 - conso_moy_basse/consumption_data*100)} %")
                    col2.metric("Moyenne haute", f"{conso_moy_haute} kwh/an", f" - {(100 - conso_moy_haute/consumption_data*100)} %")
                    col3.metric("Votre consommation", f"{consumption_data} kwh/an", )
                
                elif consumption_data < conso_moy_basse :
                    st.warning("Bravo votre consommation est inférieur à la moyenne")
                    col1.metric("Votre consommation", f"{consumption_data} kwh/an", )
                    col2.metric("Moyenne basse", f"{conso_moy_basse} kwh/an", f" + {(100 - consumption_data/conso_moy_basse*100)} %")
                    col2.metric("Moyenne haute", f"{conso_moy_haute} kwh/an", f" + {(100 - consumption_data/conso_moy_haute*100)} %")

                else:
                    col1.metric("Moyenne basse", f"{conso_moy_basse} kwh/an", f" - {(100 - conso_moy_basse/consumption_data*100)} %")
                    col2.metric("Votre consommation", f"{consumption_data} kwh/an", )
                    col3.metric("Moyenne haute", f"{conso_moy_haute} kwh/an", f" + {(100 - consumption_data/conso_moy_haute*100)} %")  

            else:
                st.error("Failed to fetch consumption data from the API")