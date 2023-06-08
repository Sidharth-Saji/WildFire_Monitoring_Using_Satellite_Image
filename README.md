# WildFire Detection Using Satellite Image

BTech Sem 2 FINAL PROJECT 

<br />Course : ID1110 
<br />Introduction to Programming

<br />**Instructor**<sub>
              <br />Albert Sunny 
              <br />Assistant Professor
              <br />Computer Science and Engineering
              <br />Indian Institute of Technology Palakkad
              <br />[Albert Sunny](https://albert-sunny.github.io/)
              <sub/>
## TEAM MEMBERS 

TEAM ID : F02

| Name of Team member  | Roll Number   |
| -------------------- | ------------- |
| SIDHARTH SAJI        | 122201026     |
| NISHANTH TAKUR       | 112201027     |
| MORI YASHWANTH       | 132201039     |

## Project Overview

The objective of this project is to develop a wildfire detection model that can analyze satellite images and identify areas prone to wildfire using CNN. We aim to detect and predict wildfires at a certain place.

## Dependencies

The following dependencies are required to run the project:

+ Python 3.6+
+ Numpy
+ Pandas
+ Os.path
+ TensorFlow
+ Pathlib
+ Keras
+ Matplotlib
+ Jupyter Notebook

## Installation

To install the project dependencies, follow these steps:

1. Clone this repository to your local machine.
2. Install __Python 3.6__ or a higher version if not already installed.
3. install the required Python libraries by running the following command:

```bash
  pip install -r requirements.txt
```

## Usage

To use the wildlife detection system,
follow the steps below:

1. Acquire satellite images or use the provided sample dataset.
2. Preprocess the satellite images, including resizing, normalization, albumentations etc.
3. Create Model using libraries imported (Refer Jupyter Notebook "Model_Training_2.ipynb".
4. Train the Model using preprocessed Satellite Images
5. Deploy the model using flask (Folder Flask_HTML)
6. We can upload images to the deployment and it will predict if wildfire occurs or not and provides a prediction percentage

<br />For detailed instructions and code examples, refer to the __Jupyter Notebook__ Model_Training_2.ipynb provided in the repository

## Data

The project requires satellite imagery datasets. You can use publicly available datasets or acquire them from reliable sources. The dataset should include images labeled with wildfire and non-wildfire regions for training and testing purposes.

<br />Some Sites from which Data Taken is given Below:
<br />[NASA](https://visibleearth.nasa.gov/search?q=Forest+Fire)
<br />[KAGGLE](https://www.kaggle.com/datasets/abdelghaniaaba/wildfire-prediction-dataset)
<br />[Worlview](https://worldview.earthdata.nasa.gov/)
<br />[NRSC ISRO](https://www.nrsc.gov.in/)

