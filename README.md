
# OpenPose for 2D Gait Analysis: Knee Flexion Landmark Detection 

Gait analysis is the scientific study of walking patterns in the field of biomechanics. It involves analyzing body mechanics, such as joint angles and muscle activity, during the different phases of walking. This analysis helps in diagnosing mobility issues, optimizing athletic performance, and guiding rehabilitation therapies.
It is crucial in various medical fields, especially orthopedics and rehabilitation.  Traditional approaches are not accessible and require costly and obtrusive equipment. 

I designed a markerless, low monetary cost, accessible approach to human gait analysis using an OpenPose-based 2D estimation system for knee flexion landmarks. Next, I plot Clinical gait angles, points of contact, and errors in estimation via approximations in displacement and flexion angles by taking a weighted average tuned to a specific demographic. 
Our approach could aid in the early detection and management of Gait anomalies often linked to people with musculoskeletal disability, providing an accessible diagnosis.

## OpenPose Installation and Usage Guide 

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

1. **Python Quick Start:**
   - For Python usage, refer to both the C++ quick start guide (for the same flags) and the Python testing documentation:
       - [C++ Quick Start Guide](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/v1.7.0/doc/quick_start.md)
       - [Python Testing Documentation](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/v1.7.0/doc/modules/python_module.md#testing) - Note: Replace "cd build/examples/tutorial_api_python" with "cd python/".
       - The rest of the instructions in `python_module.md` are for the GitHub source code library and can be ignored.

2. **Running openpose with Pyton:**
   ```bash
   cd {OpenPose_root_path}
   cd python/
   python openpose_python.py {video_name}
   ```

## Additional Notes

- Ensure to follow the instructions as per your operating system and hardware capabilities.
- Replace `{OpenPose_root_path}` with the actual path where OpenPose is installed on your machine.
- For troubleshooting, refer to the OpenPose GitHub Issues page or the detailed documentation provided in the links above.


## Open Pose for Gait Analysis


<p align="center">
  <img src="images/anatomical_plane_2.png" alt="Anatomical planes" title="Anatomical planes used in Biomechanics"/>
</p>

Anatomical planes of the human body: the sagittal plane divides the body into right and left halves, the frontal (or coronal) plane divides it into anterior (front) and posterior (back) halves, and the transverse plane divides the body into superior (upper) and inferior (lower) halves. These planes are used as points of reference in anatomical and medical contexts to describe locations or movements of various parts of the body.


The work computes gait angles in 2D plane as suggested in Whittle M. W. Gait Analysis: An introduction. Oxford, UK: Butterworth-Heinemann; 1991. [Google Scholar].

## Computed Angles for Gait Analysis

I calculate the following three angles for comprehensive gait analysis:

- **Knee Angle**: Defined as the angle between the femur and the tibia, typically unambiguous. [Sagittal Plane]
- **Ankle Angle**: Commonly defined as the angle between the tibia and an arbitrary line in the foot. While this angle is usually around 90°, it is conventionally set as 0°, with dorsiflexion and plantarflexion being movements in the positive and negative directions, respectively.
- **Hip Angle**: Measured in two distinct ways:
  - The angle between the vertical and the femur. [Sagittal Plane]
  - The angle between the pelvis and the femur, which is the 'true' hip angle, usually defined such that 0° approximates the hip angle in the standing position. [Frontal Plane]

<p align="center">

<!-- <img src="images/right_foot_resized.png" alt="Right Foot" title="Right Foot" style="display: block; margin-bottom: 10px;"/> -->
<img src="images/medial_foot.png" alt="Medial Foot" title="Medial Foot" style="display: block; margin-bottom: 5px;"/>
<img src="images/limbs_2.png" alt="Lower Limbs" title="Lower Limbs" style="display: block; margin-bottom: 5px;"/>

<!-- ![Lower Limbs](images/lower_limbs_resized.png "Lower Limbs")
<!-- ![Right Foot](images/right_foot_resized.png "Right Foot") -->
<!-- ![Medial Foot](images/medial_foot.png "Medial Foot") --> 
</p>

## Single Gait Cycle

The figures illustrates the various positions of the legs during a single gait cycle by the right leg (shown in gray). It depicts stages such as initial contact, loading response, mid-stance, terminal stance, pre-swing, initial swing, mid-swing, and terminal swing, along with heel rise, opposite toe off, and opposite initial contact, demonstrating the sequential movements involved in a complete step.

<!-- 
![Gait cycle circle](images/gait_cycle_circle.png "Gait cycle circle")
![Gait cycle square](images/single_gait_square.png "Gait cycle square") -->

<p align="center">
  <img src="images/gait_cycle_circle.png" alt="Gait cycle circle" title="Gait cycle circle"/>
</p>
<p align="center">
  <img src="images/single_gait_square.png" alt="Gait cycle square" title="Gait cycle square"/>
</p>

## Ongoing work 

The project involved setting up a camera-based system to gather standardized gait cycle data from Indian users, aiming to develop a synchronized and calibrated multi-view video and motion capture dataset. This normative dataset is crucial for understanding the typical gait characteristics in the Indian population, aiding in various applications like biomechanical research and clinical assessments.

## Future work: 3D Gait Analysis  

Additionally, 3D gait analysis offers precise and comprehensive insights into an individual's walking pattern, allowing for a detailed assessment of movement inefficiencies and joint mechanics.By visualizing three-dimensional motion, clinicians and therapists can make more informed decisions, leading to improved patient outcomes and more effective treatment interventions.
Given below are references to further our work to 3D gait analysis:


<p align="center">
  <img src="images/3d_innovations.png" alt="3d_innovations" title="3d_innovations"/>
</p>

link: [Experimental Gait Analysis to Study Stress Distribution of the Human Foot - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5694576/)

<p align="center">
  <img src="images/rose_gamble.png"  alt="rose_gamble"  title="rose_gamble"/>
</p>

<p align="center">
  <img src="images/other_refs.png"  alt="other_refs"  title="other_refs"/>
</p>


### Potential integration of OpenPose 3D Points and Depth Sensor 

OpenPose offers the capability to track 3D points, although this feature is currently limited to facial features, and left and right hand keypoints. This limitation arises from the complexity involved in accurately capturing and interpreting 3D data.

For those interested in extending the 3D capabilities of OpenPose to full-body tracking, integrating depth sensors presents a viable solution. Depth sensors can provide the additional data necessary for constructing a complete 3D skeleton model.

There are ongoing discussions and developments in the community around this topic. Notable references include:

- [3D skeleton from keypoints - Issue #428 on CMU-Perceptual-Computing-Lab/openpose (GitHub)](https://github.com/CMU-Perceptual-Computing-Lab/openpose/issues/428)
- [3D Reconstruction Demo - jrkwon/openpose (GitHub)](https://github.com/jrkwon/openpose/blob/master/doc/3d_reconstruction_demo.md)

These resources provide insights into current efforts and potential methodologies for integrating depth sensors with OpenPose, paving the way for more comprehensive 3D motion tracking and analysis.



## Acknowledgments

The work presented herein was conducted under the  supervision of Prof. Tathagata Ray from the Birla Institute of Science and Technology, Pilani.

