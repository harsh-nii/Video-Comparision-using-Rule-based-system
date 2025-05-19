# Video-Comparision-using-Rule-based-system
🔍 Objective
This project compares two 2-second video clips (vid1.mp4 and vid2.mp4) recorded from different camera angles and automatically selects the visually better one using a rule-based system — no machine learning or training data required.

✅ What It Does
Extracts frames from each video

Analyzes visual features:

Sharpness

Brightness

Contrast

Colorfulness

Face Visibility

Applies weighted scoring logic to determine which video looks better

Outputs:

Detailed comparison of each metric

Final decision: vid1.mp4, vid2.mp4, or a Tie

🧠 Why Rule-Based?
Instead of training a model, we used logical heuristics (like Laplacian variance, HSV brightness, contrast, colorfulness, and face detection) to make decisions — this makes the system:

Interpretable

Quick to run

Easy to extend

⚙️ Tech Stack
Python

OpenCV

NumPy

🚀 How to Run
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/your-username/video-comparator.git
cd video-comparator
2. Install Dependencies
bash
Copy
Edit
pip install opencv-python numpy
3. Add Your Videos
Place your two videos in the same folder:

vid1.mp4

vid2.mp4

4. Run the Script
bash
Copy
Edit
python compare_videos.py
For Google Colab:

Mount your Google Drive

Adjust the paths:

python
Copy
Edit
decide_best_video("/content/drive/MyDrive/vid1.mp4", "/content/drive/MyDrive/vid2.mp4")
📊 Sample Output
yaml
Copy
Edit
🔍 Feature Comparison:
Sharpness      : vid1 = 67.23, vid2 = 34.12
Brightness     : vid1 = 122.3, vid2 = 92.8
Contrast       : vid1 = 58.9, vid2 = 40.3
Colorfulness   : vid1 = 23.5, vid2 = 19.1
Face_visibility: vid1 = 40, vid2 = 25

🏁 Final Score (weighted): vid1 = 8, vid2 = 2

✅ Best Video: vid1.mp4
🧩 Future Improvements
Add motion blur detection

Include background clutter analysis

Handle low-light/strobe effects

🙌 Author
Harshini – AI Enthusiast | Pythonista | Open to Collaborations
🌐 LinkedIn | 💻 Portfolio (add your links here)

