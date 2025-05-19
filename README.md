# Video Comparision using Rule Based System

This Python project evaluates and compares the quality of two videos based on various visual features. It uses OpenCV and NumPy to analyze key aspects such as sharpness, brightness, contrast, colorfulness, motion blur, edge density, and more to determine which video is visually superior.

---

## Features
- Frame extraction from videos
- Video quality metrics:
  - Brightness: Measures average pixel intensity in HSV color space (ideal range: 100–200).
  - Contrast: Calculates standard deviation of pixel intensities in grayscale.
  - Sharpness: Uses Laplacian variance to assess edge strength.
  - Face Detection: Detects faces using Haar cascades and evaluates their centrality in the frame.
  - Rule-Based Scoring: Prioritizes videos with more centered faces, balanced brightness, high contrast, and high sharpness.

---

## Requirements
- Python 3.x
- OpenCV
- NumPy

### Install dependencies

```bash
pip install opencv-python numpy
