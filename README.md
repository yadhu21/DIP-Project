## 🚗 Automatic Number Plate Recognition (ANPR) from Video

### 👥 Team Members

| Name                | 
| ------------------- | 
| Yadhu Krishnan C K  | 
| Gagan P M           | 

---

### 📌 Problem Statement

Automatic Number Plate Recognition (ANPR) is essential in traffic surveillance, law enforcement, toll collection, and smart city systems. This project aims to detect and recognize vehicle number plates from video footage using image processing and Optical Character Recognition (OCR).

---

### ⚖️ Technologies Used

* **Python**
* **OpenCV** – For image preprocessing and contour detection.
* **EasyOCR** – For text recognition from processed plate images.
* **NumPy** – For image array manipulation.
* **Regular Expressions** – For cleaning and standardizing detected plate text.

---

### ⚙️ Program Flow & Techniques

1. **Video Capture:**

   * Load video using `cv2.VideoCapture`.
   * Frame-by-frame processing to detect number plates.

2. **Preprocessing:**

   * Convert frame to grayscale.
   * Apply bilateral filtering to preserve edges.
   * Detect edges using Canny edge detection.
   * Apply morphological transformations to close gaps and enhance contours.

3. **Contour Filtering:**

   * Find contours and select top 15 based on area.
   * Filter based on aspect ratio and area to locate potential plate regions.
   * Draw bounding box around detected region.

4. **OCR Processing:**

   * Resize the cropped plate region for better OCR accuracy.
   * Apply adaptive thresholding and morphological close operations.
   * Use EasyOCR to extract text and confidence values.
   * Clean detected text using regex to retain only alphanumeric characters.

5. **Post-Processing:**

   * Store all detected plate texts and their confidence scores.
   * Avoid duplicate detections by comparing with the last detected value.
   * Use `difflib.SequenceMatcher` to identify similar plate strings.
   * Determine the most frequent plate detected and calculate average confidence.

---

### 📈 Output

* Prints each detected plate with confidence.
* Displays a live video frame with bounding boxes.
* On completion, prints:

  * Most frequently detected plate.
  * Number of times detected.
  * Average confidence score across similar detections.

---

### 📝 Example Output

```
Detected Plate Number: KL58AB1234 | Confidence: 0.86
Detected Plate Number: KL58AB1234 | Confidence: 0.90

Most Frequent Detected Plate Number: KL58AB1234 (Detected 2 times)
Average Confidence for KL58AB1234: 0.88
```

---

### 📦 How to Run

1. Clone the repository.
2. Install dependencies:

   ```bash
   pip install opencv-python numpy easyocr
   ```
3. Place your video in the working directory.
4. Run the script:

   ```bash
   python anpr_script.py
   ```
## 🚗 Automatic Number Plate Recognition (ANPR) from Video

### 👥 Team Members

| Name        | Role              |
| ----------- | ----------------- |
| Yadhu       | Backend Developer |
| \[Member 2] | Video Processing  |
| \[Member 3] | OCR Integration   |
| \[Member 4] | Documentation     |

---

### 📌 Problem Statement

Automatic Number Plate Recognition (ANPR) is essential in traffic surveillance, law enforcement, toll collection, and smart city systems. This project aims to detect and recognize vehicle number plates from video footage using image processing and Optical Character Recognition (OCR).

---

### ⚖️ Technologies Used

* **Python**
* **OpenCV** – For image preprocessing and contour detection.
* **EasyOCR** – For text recognition from processed plate images.
* **NumPy** – For image array manipulation.
* **Regular Expressions** – For cleaning and standardizing detected plate text.

---

### ⚙️ Program Flow & Techniques

1. **Video Capture:**

   * Load video using `cv2.VideoCapture`.
   * Frame-by-frame processing to detect number plates.

2. **Preprocessing:**

   * Convert frame to grayscale.
   * Apply bilateral filtering to preserve edges.
   * Detect edges using Canny edge detection.
   * Apply morphological transformations to close gaps and enhance contours.

3. **Contour Filtering:**

   * Find contours and select top 15 based on area.
   * Filter based on aspect ratio and area to locate potential plate regions.
   * Draw bounding box around detected region.

4. **OCR Processing:**

   * Resize the cropped plate region for better OCR accuracy.
   * Apply adaptive thresholding and morphological close operations.
   * Use EasyOCR to extract text and confidence values.
   * Clean detected text using regex to retain only alphanumeric characters.

5. **Post-Processing:**

   * Store all detected plate texts and their confidence scores.
   * Avoid duplicate detections by comparing with the last detected value.
   * Use `difflib.SequenceMatcher` to identify similar plate strings.
   * Determine the most frequent plate detected and calculate average confidence.

---

### 📈 Output

* Prints each detected plate with confidence.
* Displays a live video frame with bounding boxes.
* On completion, prints:

  * Most frequently detected plate.
  * Number of times detected.
  * Average confidence score across similar detections.

---

### 📝 Example Output

```
Detected Plate Number: KL58AB1234 | Confidence: 0.86
Detected Plate Number: KL58AB1234 | Confidence: 0.90

Most Frequent Detected Plate Number: KL58AB1234 (Detected 2 times)
Average Confidence for KL58AB1234: 0.88
```

---

### 📦 How to Run

1. Clone the repository.
2. Install dependencies:

   ```bash
   pip install opencv-python numpy easyocr
   ```
3. Place your video in the working directory.
4. Run the script:

   ```bash
   python anpr_script.py
   ```

## Features

- **License Plate Detection**: Utilizes OpenCV to detect license plates in video frames.
- **Optical Character Recognition (OCR)**: Employs EasyOCR for accurate text recognition from detected plates.
- **Frame Skipping**: Processes every nth frame to enhance performance.
- **Most Frequent Plate Identification**: Determines and displays the most frequently detected license plate.
- **GPU Acceleration**: Supports GPU for faster OCR processing (if available).

## Prerequisites

- Python 3.6 or higher
- pip package manager
- [Virtual Environment](https://docs.python.org/3/library/venv.html) (recommended)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://yadhu21/DIP-Project.git
   cd DIP-Project
   ```


2. **Create and Activate Virtual Environment**

   - **On Windows:**

     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```

   - **On macOS/Linux:**

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```


## Usage

1. **Prepare Your Video File**

   - Place your video file (e.g., `pexels-taryn-elliott-5309381 (1080p).mp4`) in the project directory.
   - Update the `video_path` variable in the script if necessary.

2. **Run the Script**

   ```bash
   python pro.py
   ```


3. **Output**

   - The script will display the video with detected license plates highlighted.
   - After processing, it will print the most frequently detected license plate.

## Configuration

- **Frame Skipping**

  Adjust the `process_every_n_frames` variable to control how many frames are skipped between processing.

  
```python
  process_every_n_frames = 5  # Process every 5th frame
  ```


- **GPU Acceleration**

  Ensure that your system has a compatible GPU and the necessary CUDA drivers installed. EasyOCR will automatically utilize the GPU if available.

## Project Structure


```plaintext
DIP-Project/
├── .venv/                   # Virtual environment directory
├── pro.py  # Main script
├── requirements.txt         # Python dependencies
├── pexels-taryn-elliott-5309381 (1080p).mp4.mp4                # Input video file
└── README.md                # Project documentation
```


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [OpenCV](https://opencv.org/)

---

Feel free to customize this README to better fit your project's specifics. Let me know if you need assistance with any other part of your project! 
