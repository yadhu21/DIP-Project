import cv2
import numpy as np
import easyocr
import re
from collections import Counter
from difflib import SequenceMatcher

def is_similar(a, b, threshold=0.8):
    return SequenceMatcher(None, a, b).ratio() > threshold

reader = easyocr.Reader(['en'])
cap = cv2.VideoCapture('pexels-taryn-elliott-5309381 (1080p).mp4')

if not cap.isOpened():
    print("Error: Couldn't open video.")
    exit()

raw_plate_numbers = [] 
last_detected = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break  

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    filtered = cv2.bilateralFilter(gray, 11, 17, 17)
    edges = cv2.Canny(filtered, 30, 200)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    dilated = cv2.dilate(closed, kernel, iterations=1)
    
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:15]

    plate = None
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        aspect_ratio = w / float(h)
        area = w * h
        if 2 < aspect_ratio < 6 and area > 1000:
            plate = gray[y:y+h, x:x+w]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            break

    if plate is not None:
        plate_resized = cv2.resize(plate, (0, 0), fx=2, fy=2)
        plate_thresh = cv2.adaptiveThreshold(plate_resized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY, 11, 2)
        plate_thresh = cv2.morphologyEx(plate_thresh, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))

        result = reader.readtext(plate_thresh)
        if result:
            detected_text = " ".join([detection[1] for detection in result])
            detected_text = re.sub(r'[^A-Z0-9]', '', detected_text.upper())  # Alphanumeric cleanup

            if detected_text and detected_text != last_detected:
                raw_plate_numbers.append(detected_text)
                print("Detected Plate Number:", detected_text)
                last_detected = detected_text
        else:
            print("No text detected.")
    else:
        print("Plate not found.")

    cv2.imshow("Detected Plates", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Step 1: Find the most frequent number plate
counter = Counter(raw_plate_numbers)
most_common_plate, _ = counter.most_common(1)[0]

# Step 2: Correct similar plate entries
corrected_plates = []
for plate in raw_plate_numbers:
    if is_similar(plate, most_common_plate):
        corrected_plates.append(most_common_plate)
    else:
        corrected_plates.append(plate)

# Step 3: Filter out unique plates, keeping only repeated ones
repeated_plates = [plate for plate, count in Counter(corrected_plates).items() if count > 1]

if raw_plate_numbers:
    counter = Counter(raw_plate_numbers)
    most_common_plate, count = counter.most_common(1)[0]
    print(f"\nMost Frequent Detected Plate Number: {most_common_plate} (Detected {count} times)")
else:
    print("\nNo plates were detected.")
