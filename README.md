# Object Tracking with OpenCV

A simple Streamlit application that detects moving objects in video using OpenCV's Background Subtraction (MOG2). It includes an example video, lets you upload a video, previews the processed result, and provides a download button.

## Google Drive Link

**Project or demo files:** [Add your Google Drive sharing link here](https://drive.google.com/file/d/1eMhQT5Vilk0mjy-QmaysiV3xKg0YxMo5/view?usp=sharing).
## Requirements

- Python 3
- The packages listed in `requirements.txt`

## Run Locally

1. Download the project files or clone the repository.
2. Open a terminal in the project directory.
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

5. Open the URL shown in the terminal and upload a video.

## Using the App

- The app displays `tracked_example.mp4` as a demo when the file is present next to `app.py`.
- Upload a video in MP4, AVI, MOV, or MKV format.
- After processing, preview the result and download it as `tracked_video.mp4`.

## Notes

- Detection is based on motion and background subtraction, so results may vary with lighting and video conditions.
- The app draws bounding boxes around moving objects; it does not assign persistent identities to objects across frames.
