import cv2
import numpy as np
import pickle
import streamlit as st

st.set_page_config(
    page_title="Smart_Parking"
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.sidebar.title("Menu")

rectW, rectH = 107, 48

cap = cv2.VideoCapture('carPark.mp4')

with open('carParkPos', 'rb') as f:
    posList = pickle.load(f)
frame_counter = 0


def check(imgPro):
    spaceCount = 0
    for pos in posList:
        x, y = pos
        crop = imgPro[y:y+rectH, x:x+rectW]
        count = cv2.countNonZero(crop)
        if count < 900:
            spaceCount += 1
            color = (0, 255, 0)
            thick = 5
        else:
            color = (0, 0, 255)
            thick = 2

        cv2.rectangle(img, pos, (x+rectW, y+rectH), color, thick)
    cv2.rectangle(img, (45, 30), (250, 75), (180, 0, 180), -1)
    cv2.putText(img, f'Free: {spaceCount}/{len(posList)}', (50, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

# Streamlit app
st.title('Car Parking Space Detection')
st.sidebar.header('Settings')

# Placeholder for displaying video frames
frame_placeholder = st.empty()

# Placeholder for displaying available parking slots
slots_placeholder = st.empty()

# Loop for processing video frames
while True:
    ret, img = cap.read()
    if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        frame_counter = 0
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 1)
    Thre = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    blur = cv2.medianBlur(Thre, 5)
    kernel = np.ones((3, 3), np.uint8)
    dilate = cv2.dilate(blur, kernel, iterations=1)
    check(dilate)

    # Convert image to RGB for displaying in Streamlit
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Display image frame in Streamlit
    frame_placeholder.image(img_rgb, channels='RGB')

    # Update available parking slots count
    spaceCount = 0
    for pos in posList:
        x, y = pos
        crop = dilate[y:y+rectH, x:x+rectW]
        count = cv2.countNonZero(crop)
        if count < 900:
            spaceCount += 1
    slots_placeholder.write(f'Available Parking Slots: {spaceCount}/{len(posList)}')

    # Add delay to match video frame rate
    cv2.waitKey(10)
