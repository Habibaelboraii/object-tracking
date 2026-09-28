# 🎥 Object Tracking with OpenCV

A simple **Object Tracking application** built with **Python, OpenCV, and Streamlit**.

The application uses **Background Subtraction (MOG2)** to detect and track moving objects in videos. Users can upload their own video, process it, preview the tracking result, and download the processed video.

## 🚀 Live Demo

Try the application online:

👉 [Object Tracking – Streamlit App](https://object-tracking-n9uxjpteau86y42fm3qnuz.streamlit.app/)

## ✨ Features

* 🎥 Upload your own video.
* 🔍 Detect moving objects using OpenCV.
* 🧠 Use Background Subtraction (MOG2) for object detection.
* 📦 Draw bounding boxes around detected objects.
* ▶️ Preview the processed tracking result.
* ⬇️ Download the final tracking video.
* ☁️ Deployed using Streamlit.

## 🛠️ Technologies Used

* **Python**
* **OpenCV**
* **Streamlit**
* **Google Drive**
* **Background Subtraction (MOG2)**

## 📂 Project Structure

```text
Object-Tracking/
│
├── app.py
├── requirements.txt
└── README.md
```

## 📋 Requirements

* Python 3
* Streamlit
* OpenCV
* gdown

The required packages are included in `requirements.txt`.

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the project folder

```bash
cd Object-Tracking
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

### 5. Open the application

Open the URL displayed in the terminal and upload your video.

## 🎬 How to Use

1. Open the application.
2. View the example object tracking video.
3. Upload a video in one of the supported formats:

   * MP4
   * AVI
   * MOV
   * MKV
4. Wait while the video is processed.
5. View the tracking result.
6. Download the processed video using the download button.

## ☁️ Example Video

The application downloads the example video from Google Drive instead of storing the large video file directly in the GitHub repository.

This helps keep the GitHub repository lightweight.

## 🔗 Project Resources

* 🌐 **Live Demo:** [Streamlit App](https://object-tracking-n9uxjpteau86y42fm3qnuz.streamlit.app/)
* 💻 **Source Code:** Available in this GitHub repository.

## 📌 Notes

* The application is designed to detect **moving objects** in a video.
* Detection is based on **Background Subtraction (MOG2)**.
* Results may vary depending on lighting, camera movement, and video quality.
* The application processes the uploaded video and generates a new tracking video with bounding boxes.

## 👩‍💻 Author

**Habiba Saber Elboraii**

AI & Machine Learning Engineer

---

⭐ If you find this project useful, feel free to star the repository!

