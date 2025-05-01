License Plate Recognition with EasyOCR and OpenCV
This project implements a license plate recognition system using EasyOCR and OpenCV. It processes video input to detect and recognize vehicle license plates, highlighting the most frequently detected plate.​

Features
License Plate Detection: Utilizes OpenCV to detect license plates in video frames.

Optical Character Recognition (OCR): Employs EasyOCR for accurate text recognition from detected plates.

Frame Skipping: Processes every nth frame to enhance performance.

Most Frequent Plate Identification: Determines and displays the most frequently detected license plate.

GPU Acceleration: Supports GPU for faster OCR processing (if available).​

Prerequisites
Python 3.6 or higher

pip package manager

Virtual Environment (recommended)​

Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/yadhu21/DIP-Project.git
cd license-plate-recognition
Create and Activate Virtual Environment

On Windows:

bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate
On macOS/Linux:

bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Usage
Prepare Your Video File

Place your video file (e.g., video.mp4) in the project directory.

Update the video_path variable in the script if necessary.​

Run the Script

bash
Copy
Edit
python pro.py
Output

The script will display the video with detected license plates highlighted.

After processing, it will print the most frequently detected license plate.​
GitHub
+5
Stack Overflow
+5
Wikipedia
+5

Configuration
Frame Skipping

Adjust the process_every_n_frames variable to control how many frames are skipped between processing.​

python
Copy
Edit
  process_every_n_frames = 5  # Process every 5th frame
GPU Acceleration

Ensure that your system has a compatible GPU and the necessary CUDA drivers installed. EasyOCR will automatically utilize the GPU if available.​

Project Structure
plaintext
Copy
Edit
license-plate-recognition/
├── .venv/                   # Virtual environment directory
├── license_plate_recognition.py  # Main script
├── requirements.txt         # Python dependencies
├── video.mp4                # Input video file
└── README.md                # Project documentation
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.​

License
This project is licensed under the MIT License.​

Acknowledgments
EasyOCR

OpenCV​

Feel free to customize this README to better fit your project's specifics. Let me know if you need assistance with any other part of your project!
