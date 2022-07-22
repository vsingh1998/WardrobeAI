#for modeling
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator 
from tensorflow.keras.preprocessing import image

#for read and show images
import matplotlib.pyplot as plt
import cv2                                                          
import matplotlib.image as mpimg


#for save and load models
import tensorflow as tf
from tensorflow import keras                                        

import numpy as np

#for color classification
import colorsys                                                     
import PIL.Image as Image

from scipy.spatial import KDTree
from webcolors import (
   CSS3_HEX_TO_NAMES,
    hex_to_rgb
)
   
    
# load saved models
sub_model = tf.keras.models.load_model('models/models/model_category/')
top_model = tf.keras.models.load_model('models/models/model_topwear/')
bottom_model = tf.keras.models.load_model('models/models/model_bottomwear/')
foot_model = tf.keras.models.load_model('models/models/model_footwear/')


# List of all possible topwear, bottomwear, footwear the model would show. Used by cloth_classification()
sub_list = ["bottom","foot","top"]
top_list = [['Belts', 'Blazers', 'Dresses', 'Dupatta', 'Jackets', 'Kurtas',
       'Kurtis', 'Lehenga Choli', 'Nehru Jackets', 'Rain Jacket',
       'Rompers', 'Shirts', 'Shrug', 'Suspenders', 'Sweaters',
       'Sweatshirts', 'Tops', 'Tshirts', 'Tunics', 'Waistcoat'],
           ['Boys', 'Girls', 'Men', 'Unisex', 'Women'],
           ['Black', 'Blue', 'Dark Blue', 'Dark Green', 'Dark Yellow', 'Green',
       'Grey', 'Light Blue', 'Multi', 'Orange', 'Pink', 'Purple', 'Red',
       'White', 'Yellow'],
           ['Fall', 'Spring', 'Summer', 'Winter'],
           ['Casual', 'Ethnic', 'Formal', 'Party', 'Smart Casual', 'Sports',
       'Travel']]
bottom_list = [['Capris', 'Churidar', 'Jeans', 'Jeggings', 'Leggings', 'Patiala',
       'Salwar', 'Salwar and Dupatta', 'Shorts', 'Skirts', 'Stockings',
       'Swimwear', 'Tights', 'Track Pants', 'Tracksuits', 'Trousers'],
              ['Boys', 'Girls', 'Men', 'Unisex', 'Women'],
              ['Black', 'Blue', 'Dark Blue', 'Dark Green', 'Dark Yellow', 'Grey',
       'Light Blue', 'Multi', 'Orange', 'Pink', 'Purple', 'Red', 'White',
       'Yellow'],
              ['Fall', 'Spring', 'Summer', 'Winter'],
              ['Casual', 'Ethnic', 'Formal', 'Smart Casual', 'Sports']]
foot_list = [['Casual Shoes', 'Flats', 'Flip Flops', 'Formal Shoes', 'Heels',
       'Sandals', 'Sports Sandals', 'Sports Shoes'],
            ['Boys', 'Girls', 'Men', 'Unisex', 'Women'],
            ['Black', 'Blue', 'Dark Blue', 'Dark Green', 'Dark Orange',
       'Dark Yellow', 'Grey', 'Light Blue', 'Multi', 'Orange', 'Pink',
       'Purple', 'Red', 'White', 'Yellow'],
            ['Fall', 'Spring', 'Summer', 'Winter'],
            ['Casual', 'Ethnic', 'Formal', 'Party', 'Smart Casual', 'Sports']]


def rgb_to_css3(rgb_tuple):
    """
    This function converts the rgb names to their corresponding name
    in css3 format.
    
    Input: rgb tuple
    Output: css3 name

    Refered from: https://medium.com/codex/rgb-to-color-names-in-python-the-robust-way-ec4a9d97a01f
    """
    # a dictionary of all the hex and their respective names in css3
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return names[index]

def recognize_color(image):
    """
    This function recognizes the dominant color of the input image.
    Refered from : https://gist.github.com/nathforge/658336
    
 
    """

    max_score = 0.0001
    dominant_color = None
    for count,(r,g,b) in image.getcolors(image.size[0]*image.size[1]):
       
        saturation = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)[1]
        y = min(abs(r*2104+g*4130+b*802+4096+131072)>>13,235)
        y = (y-16.0)/(235-16)
        if y > 0.9:
            continue
        score = (saturation+0.1)*count
        if score > max_score:
            max_score = score
            dominant_color = (r,g,b)
            
    return rgb_to_css3(dominant_color)
 
    
def classify_color(single_path):
    """
    This function classifies the color for the defined path of a photo.
    Input: path of an image
    Output: color
    """
    image = Image.open(single_path)
    image = image.convert('RGB')
    return recognize_color(image)
    
    
    
####################################
def prediction_helper(train_images, my_model, lelist):
    """
    Helper function to store prediction from the models
    Input: image, one of three sub-model, a encoder list
    Output: list
    """
    # Convert the predicted result encoded as a number back to the original string
    # and then make them a list contains all the informations
    my_predictions = my_model.predict(train_images)
    result = []
    type_predicted_label = np.argmax(my_predictions[0][0])
    result.append(lelist[0][type_predicted_label])
    type_predicted_label = np.argmax(my_predictions[1][0])
    result.append(lelist[1][type_predicted_label])
    type_predicted_label = np.argmax(my_predictions[2][0])
    result.append(lelist[2][type_predicted_label])
    type_predicted_label = np.argmax(my_predictions[3][0])
    result.append(lelist[3][type_predicted_label])
    type_predicted_label = np.argmax(my_predictions[4][0])
    result.append(lelist[4][type_predicted_label])
    return result


def cloth_classification(single_path):
    
    """
    This function takes the path of an input image, reshape it, and then perform classification.
    
    Input: path of an image
    Output:tuple of (subtype : (prediction from model_category), 
                                     res(a string having all predictions for the given image), 
                                     res_str(the information to be displayed onto the UI))
    """
    
    # Our model only applies to dataframes. 
    # Therefore, in order to enable the model to predict a single picture, 
    # we turn this picture into a dataframe with only one row.
    train_images = np.zeros((1,80,60,3))
  
    path = single_path#/content/images   
    img = cv2.imread(path)
    
    #reshape img to apply the model
    if img.shape != (80,60,3):
        img = image.load_img(path, target_size=(80,60,3))

    train_images[0] = img

    
    result2 = sub_list[np.argmax(sub_model.predict(train_images))]
    
    # According to the results of the first model, branch to three other models
    if result2=="top":
        res = prediction_helper(train_images,top_model,top_list)
    elif result2=="bottom":
        res = prediction_helper(train_images,bottom_model,bottom_list)
    elif result2=="foot":
        res = prediction_helper(train_images,foot_model,foot_list)
    res.append(single_path)
    res_str = f"{res[0]}, {res[1]}, {classify_color(single_path)}, {res[3]}, {res[4]}, {single_path}" 
    
    return (result2,res_str,res)




def recommend_color_top(top_color_group, combotype):
    """
    This function sets rules for recommedning rest of the outfit given colour of the topwear.
    The recommendation is done by seeding random colours and comparing them versus the basecolour identified by our network.

    
    Input: color and a angle: moderate_combo == 90
                              similar_combo == 60
                              close_combo == 30
                              same_combo == 0
    Output: list of recommended colours for bottomwear and footwear
    """
    
    co = int(combotype/30)
    
    
    #colour groups : Black = 12, White = 13, Grey = 14, Multicoloured = 15

    #if top color is multi
    if top_color_group == 15: #if top color is multi
        bottom_color_group = random.choice([12,13,14]) #black, white,grey go well with multicoloured tops
         
        # Setting rules for bottomwear-footwear compatibility from daily life combinations
        if bottom_color_group==12: #black bottom
            shoes_color_group = 13 #white footwear
            
        elif bottom_color_group==13:                      #bottom = white
            shoes_color_group = random.choice([12,13,14]) #footwear = Black/White/Grey 

        else:                     
            shoes_color_group = random.choice([12,13])    #footwear =  black / white (Conventional choice!)
    
    
    # monochromatic top_colour
    elif top_color_group == 12 or top_color_group == 13 or top_color_group == 14:
        if top_color_group == 12:
            bottom_color_group = random.choice([12,13]) # Black and white bottoms both go well with black topwear
            if bottom_color_group==12:
                shoes_color_group = 13
            else:
                shoes_color_group=random.choice([12,13])

        elif top_color_group == 13:
            bottom_color_group = random.choice([12,13])
            if bottom_color_group==12:
                shoes_color_group = 13
            else:
                shoes_color_group=12
        else:
            bottom_color_group=random.choice([12,13])
            shoes_color_group=random.choice([12,13])  
    
    # If topwear not monochromatic/multi, then choose within a defined window from the colourwheel. Window range defined by combotype
    else: 
        bottom_color_group = random.choice([top_color_group-co, top_color_group+co])
        
        if bottom_color_group==top_color_group-co:
            shoes_color_group = top_color_group+co
        else:
            shoes_color_group = top_color_group-co
            
        if bottom_color_group <0:
            bottom_color_group = 12 - bottom_color_group

            
        if shoes_color_group <0:
            shoes_color_group = 12 - shoes_color_group

        bottom_color_group = bottom_color_group % 12
        shoes_color_group = shoes_color_group % 12

            
    return (bottom_color_group , shoes_color_group)
