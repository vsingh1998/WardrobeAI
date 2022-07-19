# Contents

[1. Intro](#1)

[2. Start the app](#2)

[3. Repo structure](#3)


<h2 id="1">1. Intro</h2> Do you sometimes (definitely not during the final exams week) stand in front of your closet and think deeply about "what should I wear today?!", "how do I pair up clothes today to make me more fashionable?!". Everyone defines fashion personally, but there are always some methods and ways that are fashionable for most people. What a person wears can also clearly show how that person's character and taste are. People who don't have time to think about this may need to use an app to improve their sense of fashion, such as an outfit recommendation app. In general, we have implemented such a local app which can store photo of clothes owned by users and recommend what to wear (top, bottom, and shoes) today.

<br>
<h2 id="2">2. Start the app</h2>

To start the app: 

a) First download trained models from here to the models folder. 

b) Install all the packages:
```
   pip install -r requirements.txt
```

c) Next, type the following code in any Python environment:
```
   python3 ui_module.py   
```   



<h2 id="3">3. Repository structure</h2>

```
.
├── data
│   ├── images # A directory containing the dataset images
│   └── styles.csv # A csv file containing the annotations for the images
├── models # A directory containing trained models and images of the model architectures
│   ├── models # A google drive folder which contains our trained models
│   │   ├── model_category # A model that distinguishes tops, bottoms, and shoes
│   │   ├── model_bottomwear # A model that recognizes the type, color, gender, season, and usage of bottoms
│   │   ├── model_footwear # A model that recognizes the type, color, gender, season, and usage of shoes
│   │   └── model_topwear # A model that recognizes the type, color, gender, season, and usage of tops
│   ├── model_bottomwear.png # Architecture of the model_bottomwear
│   ├── model_category.png # Architecture of the model_category
│   ├── model_footwear.png # Architecture of the model_footwear
│   └── model_topwear.png # Architecture of the model_topwear
├── ui_images # A directory containing images used for the ui_module
├── exploratory_data_analysis.ipynb # A notebook containing the analysis of our dataset and corresponding inferences
├── model_category.ipynb # A notebook containing the training of the model_category
├── models_subcategory.ipynb # A notebook containing the training of the model_bottomwear, model_footwear, and model_topwear
├── recognition_module.py # A module that contains functions and classes to generate the GUI#
├── ui_module.py # A module to run the application
├── utils.py # A module containing helping functions for model training
├── README.md # The Readme file
└── requirements.txt # The packages used

```
