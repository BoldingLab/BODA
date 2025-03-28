# BODA - Biosensor One-photon Data Acquisition

<p align="center">
  <img src="img/spinning-scope.gif" alt="Dual-Color Widefield Miniscope">
</p>

## Overview

This repository contains design files, assembly instructions, and software for a high-resolution dual-color widefield miniscope optimized for fluorescence imaging in freely moving mice. The design features improved optical performance through the use of achromatic doublets and a refined optical path that provides:

- 2.45× magnification (increased from 0.9× in previous designs)
- 2.0mm minimum field of view
- Significantly reduced chromatic aberration
- Enhanced excitation light focusing
- Modular CMOS mount for flexible sensor options

## Repository Structure

```
.
├── assembly/               # Step-by-step assembly instructions
│   ├── Optical-Component-Assembly.md
│   ├── CMOS-Assembly.md
│   ├── LED-Installation.md
│   └── Resin-Print-Post-Processing.md
├── data-acquisition/       # Software for image acquisition
│   ├── data-acquisition.py
│   ├── DAC-README.md
│   └── Napari-Micromanager-DAC.md
├── img/                    # Images and figures
├── Optical-Analysis/       # Optical design analysis
│   ├── emission-system.ipynb
│   ├── excitation-system.ipynb
│   └── lens-data/
├── procurement/            # Bill of materials and sourcing information
└── README.md               # This file
```

## Optical Design

The miniscope uses a precisely calculated optical arrangement to achieve high-quality fluorescence imaging with minimal aberrations:

- **Emission Path**: Three achromatic doublets arranged to maximize resolution while maintaining a 2.0mm FOV
- **Excitation Path**: Two plano-convex lenses to optimize LED illumination
- **Filters**: 59022m emission filter and 59022x excitation filter, with a custom dichroic mirror

The design prioritizes:
1. High native resolution through increased magnification
2. Minimal chromatic aberration using achromatic doublets
3. Efficient excitation light delivery
4. Compact, lightweight form factor (under 4.5g)

## Assembly Process

Follow these steps to build your own miniscope:

1. **3D Printing**: Use the provided STL files to print the housing components using a high-resolution resin printer
2. **Post-Processing**: Clean and cure the printed parts following the [post-processing guide](assembly/Resin-Print-Post-Processing.md)
3. **Optical Assembly**: Install the optical components following the [optical assembly guide](assembly/Optical-Component-Assembly.md)
4. **LED Installation**: Set up the excitation system using the [LED installation guide](assembly/LED-Installation.md)
5. **CMOS Installation**: Prepare and install the camera module using the [CMOS assembly guide](assembly/CMOS-Assembly.md)

## Data Acquisition

Two options are provided for image acquisition:

1. **Simple Python GUI** - A lightweight application for controlling XIMEA cameras with features for:
   - Live viewing
   - Recording
   - Single frame capture
   - Adjustable exposure and downsampling

2. **Napari-Micromanager Integration** - A more advanced option providing:
   - Multi-dimensional acquisition
   - Integration with other microscopy hardware
   - Advanced image analysis capabilities

Setup and usage instructions can be found in the [data-acquisition](data-acquisition/) directory.

## Part Procurement

A complete list of components needed to build the miniscope can be found in the [procurement](procurement/) directory, including:
- Optical components
- Camera components
- Excitation components
- Housing components
- Assembly tools

## Optical Performance

This design offers significant improvements over previous miniscope implementations:
- **Magnification**: Increased from 0.9× to 2.45× (172% improvement)
- **Resolution**: Improved by 2.72× while maintaining a minimum 2.0mm FOV
- **Chromatic Aberration**: Reduced by >167%, eliminating the need to reposition when switching between red and green channels