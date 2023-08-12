import streamlit as st
import openai 

openai.api_key = st.secrets["api_key"]

st.title('chatGPT + DALL E')


with st.form(key='my_form'):

    user_input = st.text_input('Prompt')
    size = st.selectbox('Size', ['256x256', '512x512', '1024x1024'])
    submit_button = st.form_submit_button(label='Submit')

if submit_button and user_input:
    gpt_prompt = [{ 
        "role":"system",
        "content":"You are now a DALLE-2 prompt generation tool that Output is english word, Imagine the detail appreareance of the input. Response it Shortly around 30 words"}]
    gpt_prompt.append({
        "role":"user",
        "content":user_input,
    })
    with st.spinner('Waiting for ChatGPT...'):
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt,
        )

    prompt = gpt_response['choices'][0]['message']['content']
    st.write(prompt)

    with st.spinner('Waiting for DALL-E ...'):
        dalle_response = openai.Image.create(
            prompt = prompt,
            size = size,
        )
        st.image(dalle_response['data'][0]['url'])
