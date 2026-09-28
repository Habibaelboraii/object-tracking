import streamlit as st
import cv2
import tempfile
import os
import gdown


# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="Object Tracking",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 Object Tracking Using OpenCV")

st.write(
    "Upload a video and detect moving objects using "
    "Background Subtraction (MOG2)."
)


# =========================
# Download Example Video
# =========================

@st.cache_data
def download_example_video():

    file_id = "11g13oWyU_UXVAXD_U7Tv2xt-GFl1APzM"

    output_path = "example_video.mp4"

    if not os.path.exists(output_path):

        url = f"https://drive.google.com/uc?id={file_id}"

        gdown.download(
            url,
            output_path,
            quiet=False
        )

    return output_path


# =========================
# Example Video
# =========================

st.subheader("📌 Example Video")

st.write(
    "This is an example of object tracking using OpenCV:"
)

try:

    example_video = download_example_video()

    if os.path.exists(example_video):

        st.video(example_video)

    else:

        st.warning("Example video was not found.")

except Exception as e:

    st.error(
        "❌ Could not download the example video from Google Drive."
    )

    st.write(e)


# =========================
# Upload Video
# =========================

st.subheader("📤 Upload Your Video")

uploaded_file = st.file_uploader(
    "Upload your video",
    type=["mp4", "avi", "mov", "mkv"]
)


# =========================
# Process Uploaded Video
# =========================

if uploaded_file is not None:

    st.success("✅ Video uploaded successfully!")

    # Save uploaded video temporarily

    input_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=os.path.splitext(uploaded_file.name)[1]
    )

    input_file.write(uploaded_file.read())
    input_file.close()

    # Open video

    captures = cv2.VideoCapture(input_file.name)

    # Check if video opened

    if not captures.isOpened():

        st.error("❌ Could not open the uploaded video.")

        os.remove(input_file.name)

        st.stop()

    # Background subtractor

    back_subtractor = cv2.createBackgroundSubtractorMOG2()

    # Get video properties

    fps = captures.get(cv2.CAP_PROP_FPS)

    width = int(
        captures.get(cv2.CAP_PROP_FRAME_WIDTH)
    )

    height = int(
        captures.get(cv2.CAP_PROP_FRAME_HEIGHT)
    )

    # If FPS is not detected

    if fps == 0:

        fps = 30

    # Output video

    output_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp4"
    )

    output_path = output_file.name

    output_file.close()

    # Video writer

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    writer = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    st.subheader("🎯 Tracking Result")

    # Placeholder for video frames

    frame_placeholder = st.empty()

    # Progress bar

    total_frames = int(
        captures.get(cv2.CAP_PROP_FRAME_COUNT)
    )

    progress_bar = st.progress(0)

    frame_number = 0

    # =========================
    # Process Frames
    # =========================

    while captures.isOpened():

        ret, frame = captures.read()

        if not ret:

            break

        frame_number += 1

        # Background subtraction

        mask = back_subtractor.apply(frame)

        # Find contours

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # Draw bounding boxes

        for contour in contours:

            if cv2.contourArea(contour) > 500:

                x, y, w, h = cv2.boundingRect(contour)

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    "Object",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

        # Save processed frame

        writer.write(frame)

        # Convert BGR to RGB

        frame_rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        # Display frame

        frame_placeholder.image(
            frame_rgb,
            channels="RGB"
        )

        # Update progress

        if total_frames > 0:

            progress = min(
                frame_number / total_frames,
                1.0
            )

            progress_bar.progress(progress)

    # Release resources

    captures.release()
    writer.release()

    progress_bar.progress(1.0)

    st.success("✅ Object tracking completed!")

    # =========================
    # Final Tracking Video
    # =========================

    st.subheader("🎬 Final Tracking Video")

    with open(output_path, "rb") as video_file:

        video_bytes = video_file.read()

    st.video(video_bytes)

    # =========================
    # Download Button
    # =========================

    st.download_button(
        label="⬇️ Download Tracking Video",
        data=video_bytes,
        file_name="tracked_video.mp4",
        mime="video/mp4"
    )

    # =========================
    # Delete Temporary Files
    # =========================

    os.remove(input_file.name)
    os.remove(output_path)
