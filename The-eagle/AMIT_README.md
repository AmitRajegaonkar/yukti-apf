# 🦅 The Eagle - Weapon Detection System Setup Guide

## 📋 Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

The Eagle is a real-time weapon detection system using YOLO (You Only Look Once) deep learning model. It can detect weapons from video feeds and send alerts via Directus, email, and sound notifications.

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** (Recommended: Python 3.12)
- **CUDA-enabled GPU** (Optional but recommended for faster processing)
- **pip** (Python package manager)
- **Git** (for cloning the repository)

---

## 🔧 Environment Setup

### Step 1: Create a Virtual Environment

Creating a virtual environment keeps your project dependencies isolated.

```bash
# Navigate to the project directory
cd d:\sih-2024-main\The-eagle

# Create a virtual environment named 'myenv312'
python -m venv myenv312

# Activate the virtual environment
# On Windows:
myenv312\Scripts\activate

# On Linux/Mac:
source myenv312/bin/activate
```

You should see `(myenv312)` in your terminal prompt, indicating the virtual environment is active.

### Step 2: Install Dependencies

With the virtual environment activated, install all required packages:

```bash
pip install -r requirements.txt
```

**Note:** If you encounter any errors with specific packages (like `dlib` or `torch`), you may need to install them separately based on your system configuration.

---

## ⚙️ Configuration

### Understanding the `.env` File

The `.env` file stores sensitive configuration data and environment-specific settings. This keeps your credentials secure and makes the application portable.

### Step 3: Create Your `.env` File

1. In the project root directory (`d:\sih-2024-main\The-eagle`), create a file named `.env`
2. Add the following variables:

```env
# Directus API Configuration
DIRECT_US_ACCESS_TOKEN=your_directus_access_token_here
ALERT_FACES_FOLDER_ID=your_folder_id_here

# Camera Location Configuration
camera_0_location=Your Camera Location Address Here
```

### Step 4: Configure Environment Variables

Replace the placeholder values with your actual configuration:

#### **DIRECT_US_ACCESS_TOKEN**
- This is your Directus API authentication token
- **How to get it:**
  1. Log in to your Directus instance
  2. Go to Settings → Access Tokens
  3. Create a new token or copy an existing one
  4. Paste it in the `.env` file

**Example:**
```env
DIRECT_US_ACCESS_TOKEN=tCT9YaoHzCXdqRPLQNJVczN15Q7pKnJ7
```

#### **ALERT_FACES_FOLDER_ID**
- This is the folder ID in Directus where detected weapon images will be uploaded
- **How to get it:**
  1. Log in to your Directus instance
  2. Navigate to File Library
  3. Create or select a folder for weapon alerts
  4. The folder ID is in the URL or folder properties

#### **camera_0_location**
- This is the physical location of your camera
- Used in alert notifications to identify where the weapon was detected

**Example:**
```env
camera_0_location=Swami Rd, opp. Cooper Hospital, Navpada, JVPD Scheme, Vile Parle, Mumbai
```

## 🚀 Running the Application

### Option 1: Run the Flask Web Application

This starts the web interface where you can view camera feeds in your browser.

```bash
# Make sure your virtual environment is activated
# (myenv312) should be visible in your terminal

# Run the Flask app
python flaskapp.py
```

The application will start on `http://localhost:5001`

**Access the application:**
- Open your browser and go to: `http://localhost:5001`
- Login page: `http://localhost:5001/`
- Home page: `http://localhost:5001/home`
- Webcam view: `http://localhost:5001/webcam`

### Option 2: Run Standalone Detection (FRT.py)

This runs the detection directly with OpenCV window display.

```bash
python FRT.py
```

This will:
- Open a window showing the camera feed
- Detect weapons in real-time
- Send alerts when weapons are detected
- Press 'q' to quit

---

## 🔍 How It Works

### Detection Flow

1. **Video Capture**: The system captures video from your camera (internal/external)
2. **YOLO Processing**: Each frame is processed by the YOLO model to detect weapons
3. **Alert Triggering**: When a weapon is detected with >70% confidence:
   - 📸 Frame is saved as an image
   - ☁️ Image is uploaded to Directus
   - 📍 Alert is sent to Directus with location
   - 🔊 Sound alert is played
4. **Display**: Processed frames are shown with bounding boxes around detected weapons

### Detected Weapon Types

- Rifle
- Hand Gun
- Knife
- Generic Weapon
- Gun

---

## 🛠️ Troubleshooting

### Common Issues and Solutions

#### **Issue: `ModuleNotFoundError: No module named 'dotenv'`**
**Solution:**
```bash
pip install python-dotenv
```

#### **Issue: CUDA/GPU not detected**
**Solution:**
Check if CUDA is available:
```bash
python "GPU test.py"
```
If it returns `False`, the system will use CPU (slower but functional).

#### **Issue: Camera not found**
**Solution:**
- Check if your camera is connected
- Try changing the camera index in the code:
  - `0` for internal camera
  - `1` for external camera

#### **Issue: Directus upload fails**
**Solution:**
- Verify your `DIRECT_US_ACCESS_TOKEN` is correct
- Check if Directus is running at `http://localhost:8055`
- Ensure the `ALERT_FACES_FOLDER_ID` exists in your Directus instance

#### **Issue: Sound alert not playing**
**Solution:**
- Ensure `Alert_sound.mp3` exists in the project directory
- Check your system volume settings
- Verify pygame is installed: `pip install pygame`

---

## 📁 Project Structure

```
The-eagle/
├── .env                      # Environment variables (DO NOT COMMIT TO GIT)
├── requirements.txt          # Python dependencies
├── flaskapp.py              # Flask web application
├── YOLO_Video.py            # Main detection logic
├── FRT.py                   # Standalone detection script
├── GPU test.py              # GPU availability checker
├── Alert_sound.mp3          # Alert sound file
├── myenv312/                # Virtual environment (DO NOT COMMIT)
└── YOLO-Weights/
    └── Weapon.pt            # YOLO model weights
```

---


### Directus URL Configuration

If your Directus instance is not running on `localhost:8055`, update the URL in `YOLO_Video.py`:

```python
direct_us_url = "http://your-directus-url:port"
```

---

## 🎓 Quick Start Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with all required variables
- [ ] Directus instance running (if using cloud features)
- [ ] YOLO model weights available at `../YOLO-Weights/Weapon.pt`
- [ ] Camera connected and accessible
- [ ] Run the application: `python flaskapp.py`

---

## 📞 Support

If you encounter any issues not covered in this guide, please:
1. Check the error message carefully
2. Verify all environment variables are set correctly
3. Ensure all dependencies are installed
4. Check that your camera and Directus are accessible

---

## 🎉 You're All Set!

Your weapon detection system is now configured and ready to use. Start the application and begin monitoring for weapons in real-time!

```bash
# Activate environment
myenv312\Scripts\activate

# Run the application
python flaskapp.py
```

Happy monitoring! 🦅
