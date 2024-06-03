import tensorflow as tf
from keras.models import load_model
import streamlit as st

# from db import push

# image = st.file_uploader('chosse a image :')


# st.text

cnn = load_model('brain_tumer.h5')
# cnn.summary()


import numpy as np

def prediction():
    test_image = tf.keras.utils.load_img('out.png', target_size = (64, 64))
    test_image = tf.keras.utils.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = cnn.predict(test_image/255.0)

    output = np.argmax(result[0])

    label = {0:'glioma', 1:'meningioma',2:'notumor', 3:'pituitary'}
    out = label[int(output)]
    print(out)
    return out


from PIL import Image

def save_uploaded_file(uploaded_file, filename):
    with open(filename, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return

def main():
    st.title("Brian Tumor Analysis : ")
    
    name = st.text_input('Patenunt Name ')
    age = st.text_input('Age')


    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image")

        if st.button("Predict"):
            save_uploaded_file(uploaded_file, 'out.png')
            n = prediction()
            st.title(n)
            st.text(f'Sorry, {name} your have {n} type of Brain Tumor diseases 🥲')
            # push(name,age,n)
            
            
            
            
if __name__ == "__main__":
    main()
