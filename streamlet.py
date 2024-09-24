import streamlit as st
import pandas as pd
import time

table = pd.DataFrame({
    "Name": ['Mohamed', 'Hussein', 'Farah', 'Naima', 'Ahmed', 'Farhiya'],
    "Gender": ['Male','Male',  'Male','Female', 'Male', 'Female'],
    "Age": [20,65,43,26,32,18]
})

st.set_page_config(page_title='WELCOME on Board', page_icon= 'icon.png', layout='wide', initial_sidebar_state='auto' )
st.title("Development Web App for Data Analytical with Mechine Learning")
st.markdown("---")

st.header("We're mainly focusing on ML with different Library")

st.markdown("like *Skit-learning*, and many other libarary go through the link below [Google](https://www.google.com), :flag-ae:")

st.latex(r"\begin{vmatrix}13&40&67\\57&32&43\\76&99&88\end{vmatrix}")

json = {
    "a": '1, 2, 3',
    'b': '4, 5, 6'
}

st.json(json)


code = """

print(" Hello World, kindly welcoming me on this - Date creation = '15 Sept 2024' ")

def function_a():
    return = 0;
"""


st.code(code, language="python" )

st.markdown("---")

st.metric(label="Monthly Salary Scale", value="120ms⁻¹", delta="1.4ms⁻¹")




st.table(table)

st.dataframe(table)


st.markdown("---")

def changing():
    print(st.session_state.checker)

status = st.checkbox("Confirmation", value=True, on_change=changing, key='checker')

if status:
    st.write("Cleared to process with next stage")
else:
    st.write('Seeking Confirmation for Sec')
    
    
    

radio_btn = st.radio("What's your nationality?", options=("UK", 'USA', 'JSSR', 'SOMALIA') )

print(radio_btn)


button_btm = st.button("Click me!", on_click=changing)



selection_list = st.multiselect("What's your Favorite car? ", options=("BMW", "Ferari", 'Audi', 'Toyota', 'Ford', 'Ronger Rover'))



st.write(selection_list)


st.markdown('---')


st.markdown("# File Uploder Demo's ")


sawir = st.file_uploader("Please upload your file", type=['png', 'jpg', 'avif'], accept_multiple_files=True)

if sawir is not None:
    for x in sawir:
        st.image(x)
    # st.image(sawir)
    
    st.markdown('---')
    
    
st.slider(min_value=10, max_value=180, value=30, step=10, label='welcome')


bar = st.progress(0)
for x in range(10):
    bar.progress((x+1)*10)
    time.sleep(0.5)
    
    
    
    
    
    
    
    
    
    




st.set_page_config