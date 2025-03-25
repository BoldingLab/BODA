# Napari-Micromanager with Ximea Camera Setup Guide

## Prerequisites
- Windows computer with administrator privileges
- Python 3.8 or later
- Ximea camera hardware

## Quick Setup Steps

### 1. Install Napari-Micromanager
```bash
# Create environment
conda create -n napari-mm python=3.9
conda activate napari-mm

# Install napari and plugin
pip install "napari[all]"
pip install napari-micromanager
```

### 2. Install Ximea Software
1. Download the latest [XIMEA API Software Package](https://www.ximea.com/support/wiki/apis/XIMEA_API_Software_Package)
2. Run the installer, ensuring camera drivers are included
3. Test with Ximea CamTool to verify camera connection

### 3. Integrate Ximea with Micro-Manager
1. Locate `xiapi64.dll` in `C:\XIMEA\API\x64\`
2. Find your Micro-Manager directory:
   ```python
   python -c "from pymmcore_plus import find_micromanager; print(find_micromanager())"
   ```
3. Copy the DLL to the Micro-Manager directory

### 4. Generate Camera Configuration
1. Launch Micro-Manager directly from the installation directory
2. Select "Tools" > "Hardware Configuration Wizard"
3. Create new configuration, add "XIMEACamera" from device list
4. Complete wizard and save configuration file (e.g., `XimeaConfig.cfg`)
5. Test with "Snap" button to capture an image

### 5. Use in Napari
1. Launch napari
2. Go to Plugins > napari-micromanager
3. Load your Ximea configuration file
4. The camera should now be available for use

## Configuration File Usage
- Place the configuration file you'll receive in `[User Directory]/Documents/Micro-Manager/`
- Load via "File" > "Load System Configuration" in Micro-Manager
- Or specify when launching in Python:
  ```python
  import napari
  from napari_micromanager import MicroManagerWidget
  
  viewer = napari.Viewer()
  mm_widget = MicroManagerWidget(viewer)
  mm_widget.load_configuration("/path/to/your/ximea_config.cfg")
  ```

## Troubleshooting
- If camera isn't detected, verify DLL is correctly placed
- For communication issues, check camera connections and test with Ximea CamTool
- If using older Micro-Manager (pre-2018), rename xiapi64.dll to m3apiX64.dll

## Resources
- [Napari-Micromanager Repository](https://github.com/pymmcore-plus/napari-micromanager)
- [Micro-Manager Documentation](https://micro-manager.org/Micro-Manager_User%27s_Guide)
- [Ximea Camera in Micro-Manager](https://micro-manager.org/XIMEA)