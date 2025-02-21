# Camera Control Application

A Python-based GUI application for controlling XIMEA cameras with features for live viewing, recording, and image capture.

## Prerequisites

### Required Hardware
- XIMEA camera (compatible with xiapi)
- USB3 port for camera connection

### Required Software
- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Create a Virtual Environment** (recommended)
   ```bash
   python -m venv venv
   
   # Activate on Windows
   venv\Scripts\activate
   
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

2. **Install Required Packages**
   ```bash
   pip install customtkinter
   pip install tkinterDnD
   pip install opencv-python
   ```

3. **Install XIMEA Software Package**
   - Download and install XIMEA Software Package (xiAPI) from the [XIMEA website](https://www.ximea.com/support/documents/4)
   - Follow XIMEA's installation guide for your operating system
   - Install the Python API:
     ```bash
     pip install ximea
     ```

## Application Features

### Camera Settings
- Adjustable exposure time
- Multiple downsampling options (None, 1/2, 1/4, 1/8)
- Zoom levels (None, 2x, 3x, 7x, 10x)
- FPS display toggle
- Timer display toggle

### Recording Options
- Custom recording name
- Video recording (.avi format)
- Single frame capture (PNG format)
- Live preview window

## Usage

1. **Starting the Application**
   ```bash
   python camera_control.py
   ```

2. **Basic Operation**
   - Enter a recording name (optional - defaults to 'recording')
   - Set exposure time (optional - defaults to 80000)
   - Select desired downsampling rate
   - Select zoom level if needed
   - Toggle timer/FPS display as needed
   - Click "Start" to begin camera feed
   - Use "Take Photo" for single frame capture
   - Click "Stop" to end recording

### Main Controls
- **Start Button**: Initiates camera feed and recording
- **Stop Button**: Ends camera feed and saves recording
- **Take Photo**: Captures current frame as PNG file

### Recording Settings
- Files are saved in the working directory
- Videos are saved as .avi files using MJPG codec
- Photos are saved as PNG files with timestamp

## Troubleshooting

### Common Issues
1. **Camera Not Detected**
   - Ensure camera is properly connected via USB3
   - Verify XIMEA drivers are installed
   - Check camera permissions on your system

2. **Recording Issues**
   - Ensure sufficient disk space
   - Verify write permissions in working directory
   - Check if previous recording was properly closed

3. **Display Issues**
   - Ensure OpenCV is properly installed
   - Check monitor resolution settings
   - Verify GUI framework dependencies

## File Naming Convention

- Videos: `{recording_name}.avi`
- Photos: `{recording_name}_{YYYYMMDD-HHMMSS}.png`

## Notes

- Application window size: 620x480 pixels
- Live preview window: 1296x972 pixels
- Default recording name: "recording"
- Default exposure: 80000
- Video frame rate: 4.6 FPS

## System Requirements

- Operating System: Windows/Linux/macOS
- RAM: 4GB minimum (8GB recommended)
- USB3 port
- Sufficient storage space for recordings

---

*For additional support or issues, please refer to the XIMEA documentation or contact technical support.*