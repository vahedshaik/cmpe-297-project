from google.cloud import aiplatform
import streamlit as st
import pandas as pd
import base64
import json
from PIL import Image

project_id = "green green-123456"

endpoint_id = "2123429254823207234854"

# Streamlit App
# st.title('Advanced Deep Learning Emotion classification')
title = '<h1 style="font-family:sans-serif; color:#e75480; font-size: 42px;">Advanced Deep Learning Emotion classification</h1>'
st.markdown(title, unsafe_allow_html=True)
st.subheader('Model is finetuned on pretrained bert')

user_input = st.text_input("Type in your text here", 'wish me luck!')
submit = st.button('Run')
location = "us-central1"
bucket_name = "gs://green--green-123456aip-20211209030626"

aiplatform.init(project=project_id, staging_bucket=bucket_name)

endpoint_display_name = "finetuned-bert-classifier-endpoint"
filter = f'display_name="{endpoint_display_name}"'

for endpoint_info in aiplatform.Endpoint.list(filter=filter):
    print(
        f"Endpoint display name = {endpoint_info.display_name} resource id ={endpoint_info.resource_name} "
    )

endpoint = aiplatform.Endpoint(endpoint_info.resource_name)
print(endpoint.list_models())

dict = {'anger':'images/anger.jpeg', 
        'fear':'images/fear.jpeg',
        'Joy':'images/joy.jpeg', 
        'love':'images/love.png', 
        'Sadness':'images/sadness.jpeg'}

def get_predictions(test_instance):
    print(f"Input text: \n\t{test_instance.decode('utf-8')}\n")
    b64_encoded = base64.b64encode(test_instance)
    test = [{"data": {"b64": f"{str(b64_encoded.decode('utf-8'))}"}}]
    prediction = endpoint.predict(instances=test)
    return prediction.predictions[0]

if submit:
    user_input_as_bytes = str.encode(user_input)
    result = get_predictions(user_input_as_bytes)
    path = dict[result]
    image = Image.open(path)
    new_title = '<p style="font-family:sans-serif; color:#e75480; font-size: 42px;">' + result + '</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.image(image, width=300)
