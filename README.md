
# OpenPose Installation and Usage Guide

## Introduction

This README provides detailed instructions for setting up and using OpenPose, an open-source real-time multi-person keypoint detection library for body, face, and hand estimation. The guidelines are based on version 1.7.0 of OpenPose.

## Downloading Models

If you don't have the `models` directory:

1. **Clone the OpenPose Repository:**
   - First, clone the OpenPose repository from GitHub to your local machine. Use the following command:
     ```
     git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git
     ```
   - This will create an OpenPose directory with all the necessary files, including the `models` directory.

2. **Base Models:**
   - After cloning, navigate to the `models` directory within the OpenPose folder.
   - Double-click on `getBaseModels.bat`. This script will download the required body, face, and hand models.

3. **Optional Models:**
   - For additional models like COCO and MPII, double-click on `models/getCOCO_and_MPII_optional.bat`. Note: These models are slower and less accurate. Download them only if necessary.

## Installation Steps

- Ensure that you have cloned or downloaded the OpenPose repository from GitHub. For detailed instructions, refer to the following resources:
    - OpenPose v1.7.0: [OpenPose GitHub - v1.7.0](https://github.com/CMU-Perceptual-Computing-Lab/openpose/tree/v1.7.0)
    - Documentation: [OpenPose Documentation - v1.7.0](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/v1.7.0/doc/)

## Quick Start Guides

1. **C++ Quick Start Guide:**
   - For getting started with C++, follow the instructions in the [C++ Quick Start Guide](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/v1.7.0/doc/quick_start.md).

2. **Python Quick Start:**
   - For Python usage, refer to both the C++ quick start guide (for the same flags) and the Python testing documentation:
       - [C++ Quick Start Guide](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/v1.7.0/doc/quick_start.md)
       - [Python Testing Documentation](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/v1.7.0/doc/modules/python_module.md#testing) - Note: Replace "cd build/examples/tutorial_api_python" with "cd python/".
       - The rest of the instructions in `python_module.md` are for the GitHub source code library and can be ignored.

3. **Python Code Example:**
   ```bash
   cd {OpenPose_root_path}
   cd python/
   python openpose_python.py
   ```

## Additional Notes

- Ensure to follow the instructions as per your operating system and hardware capabilities.
- Replace `{OpenPose_root_path}` with the actual path where OpenPose is installed on your machine.
- For troubleshooting, refer to the OpenPose GitHub Issues page or the detailed documentation provided in the links above.
