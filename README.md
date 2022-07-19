# Contents

[1. Intro](#1)

[2. Start the app](#2)

[3. Repo structure](#3)


<h2 id="1">1. Intro</h2> Dread. Dilemma. Distraction. Picking out a daily outfit from your wardrobe often involves these emotions. Given the abundance of clothes in our wardrobes, picking an outfit should be simpler and quicker. 

Could this be a task our mobiles can do as well? We set out exploring this. Our idea is to apply computer vision based deep learning techniques to recommend outfits. We develop a local app that can be accessed on our systems which identifies outfits as a combination of 3 subcategories - Topwear, Bottomwear and Footwear. Furthermore, we give you the outfits based on the season of the year. You may choose to look ahead for a specific time in the future to plan your outfit in advance.


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
