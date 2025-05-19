import cv2
import numpy as np
import os

def calculate_brightness(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    return np.mean(hsv[:, :, 2])

def calculate_contrast(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return np.std(gray)

def calculate_sharpness(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    return laplacian.var()

def detect_faces(frame):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    if len(faces) == 0:
        return 0, 0
    
    # Calculate centrality: closer to center of frame is better
    height, width = gray.shape
    center_x, center_y = width // 2, height // 2
    centrality_score = 0
    for (x, y, w, h) in faces:
        face_center_x = x + w // 2
        face_center_y = y + h // 2
        distance = np.sqrt((face_center_x - center_x) ** 2 + (face_center_y - center_y) ** 2)
        centrality_score += (1 - distance / np.sqrt(center_x ** 2 + center_y ** 2))  # Normalize
    return len(faces), centrality_score / len(faces)

def evaluate_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Could not open video: {video_path}")
    
    brightness_scores = []
    contrast_scores = []
    sharpness_scores = []
    face_counts = []
    centrality_scores = []
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        
        brightness_scores.append(calculate_brightness(frame))
        contrast_scores.append(calculate_contrast(frame))
        sharpness_scores.append(calculate_sharpness(frame))
        face_count, centrality = detect_faces(frame)
        face_counts.append(face_count)
        centrality_scores.append(centrality)
    
    cap.release()
    
    if frame_count == 0:
        return 0, 0, 0, 0, 0
    
    # Average metrics across frames
    avg_brightness = np.mean(brightness_scores)
    avg_contrast = np.mean(contrast_scores)
    avg_sharpness = np.mean(sharpness_scores)
    avg_face_count = np.mean(face_counts)
    avg_centrality = np.mean(centrality_scores) if sum(face_counts) > 0 else 0
    
    return avg_brightness, avg_contrast, avg_sharpness, avg_face_count, avg_centrality

def compare_videos(vid1_path, vid2_path):
    # Evaluate both videos
    vid1_metrics = evaluate_video(vid1_path)
    vid2_metrics = evaluate_video(vid2_path)
    
    vid1_brightness, vid1_contrast, vid1_sharpness, vid1_face_count, vid1_centrality = vid1_metrics
    vid2_brightness, vid2_contrast, vid2_sharpness, vid2_face_count, vid2_centrality = vid2_metrics
    
    # Scoring system
    score1 = 0
    score2 = 0
    
    # Rule 1: Face detection (most important)
    if vid1_face_count > vid2_face_count:
        score1 += 3
    elif vid2_face_count > vid1_face_count:
        score2 += 3
    else:
        # If equal face count, compare centrality
        if vid1_centrality > vid2_centrality:
            score1 += 2
        elif vid2_centrality > vid1_centrality:
            score2 += 2
    
    # Rule 2: Brightness (ideal range 100–200)
    if 100 <= vid1_brightness <= 200 and not (100 <= vid2_brightness <= 200):
        score1 += 2
    elif 100 <= vid2_brightness <= 200 and not (100 <= vid1_brightness <= 200):
        score2 += 2
    else:
        # Prefer brightness closer to 150
        vid1_brightness_diff = abs(vid1_brightness - 150)
        vid2_brightness_diff = abs(vid2_brightness - 150)
        if vid1_brightness_diff < vid2_brightness_diff:
            score1 += 1
        elif vid2_brightness_diff < vid1_brightness_diff:
            score2 += 1
    
    # Rule 3: Contrast (higher is better)
    if vid1_contrast > vid2_contrast:
        score1 += 1
    elif vid2_contrast > vid1_contrast:
        score2 += 1
    
    # Rule 4: Sharpness (higher is better)
    if vid1_sharpness > vid2_sharpness:
        score1 += 1
    elif vid2_sharpness > vid1_sharpness:
        score2 += 1
    
    # Decide winner
    if score1 > score2:
        return 0, f"Best Video: vid1.mp4"
    elif score2 > score1:
        return 1, f"Best Video: vid2.mp4"
    else:
        # Tiebreaker: prefer video with more faces or higher centrality
        if vid1_face_count > vid2_face_count or vid1_centrality > vid2_centrality:
            return 0, f"Best Video: vid1.mp4"
        else:
            return 1, f"Best Video: vid2.mp4"

def main():
    vid1_path = "/content/drive/MyDrive/vid1.mp4"
    vid2_path = "/content/drive/MyDrive/vid2.mp4"
    
    if not (os.path.exists(vid1_path) and os.path.exists(vid2_path)):
        print("Error: Video files not found.")
        return
    
    binary_result, text_result = compare_videos(vid1_path, vid2_path)
    print(text_result)
    print(f"Binary Output: {binary_result}")

if __name__ == "__main__":
           main()
