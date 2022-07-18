import pandas as pd


def group_color(styles):
  styles["colorgroup"] = -1
  styles.loc[(styles.baseColour=='Red')|
          (styles.baseColour=='Brown')|
          (styles.baseColour=='Coffee Brown')|
          (styles.baseColour=='Maroon')|
          (styles.baseColour=='Rust')|
          (styles.baseColour=='Burgundy')|
          (styles.baseColour=='Mushroom Brown'),"colorgroup"] = 0
  styles.loc[(styles.baseColour=='Copper'),"colorgroup"] = 1
  styles.loc[(styles.baseColour=='Orange')|
              (styles.baseColour=='Bronze')|
              (styles.baseColour=='Skin')|
              (styles.baseColour=='Nude'),"colorgroup"] = 2
  styles.loc[(styles.baseColour=='Gold')|
              (styles.baseColour=='Khaki')|
              (styles.baseColour=='Beige')|
              (styles.baseColour=='Mustard')|
              (styles.baseColour=='Tan')|
              (styles.baseColour=='Metallic'),"colorgroup"]= 3
  styles.loc[(styles.baseColour=='Yellow'),"colorgroup"] = 4
  styles.loc[(styles.baseColour=='Lime Green'),"colorgroup"]= 5
  styles.loc[(styles.baseColour=='Green')|
          (styles.baseColour=='Sea Green')|
          (styles.baseColour=='Fluorescent Green')|
          (styles.baseColour=='Olive'),"colorgroup"] = 6
  styles.loc[(styles.baseColour=='Teal')|
          (styles.baseColour=='Turquoise Blue'),"colorgroup"] = 7
  styles.loc[(styles.baseColour=='Blue'),"colorgroup"]= 8
  styles.loc[(styles.baseColour=='Navy Blue'),"colorgroup"] = 9
  styles.loc[(styles.baseColour=='Purple')|
          (styles.baseColour=='Lavender'),"colorgroup"] = 10
  styles.loc[(styles.baseColour=='Pink')|
          (styles.baseColour=='Magenta')|
          (styles.baseColour=='Peach')|
          (styles.baseColour=='Rose')|
          (styles.baseColour=='Mauve'),"colorgroup"] = 11
  styles.loc[(styles.baseColour=='Black')|
          (styles.baseColour=='Charcoal'),"colorgroup"] = 12
  styles.loc[(styles.baseColour=='White')|
          (styles.baseColour=='Off White')|
          (styles.baseColour=='Cream'),"colorgroup"] = 13
  styles.loc[(styles.baseColour=='Grey')|
          (styles.baseColour=='Silver')|
          (styles.baseColour=='Taupe')|
          (styles.baseColour=='Grey Melange'),"colorgroup"] = 14
  styles.loc[(styles.baseColour=='Multi'),"colorgroup"] = 15  
    

def remove_items(styles, col, item):
  """
  function to drop certain columns

  input : styles: dataframe
          col: column to drop items from
          item: items to drop
  return: dataframe
  """

  for i in item:
    styles = styles.drop(styles[styles[col]==i].index)
  
  return styles


def split_data(x, batch_size):
  """
  function to make train, test, validation splits

  input : x, input dataset
  return: x_train, training dataset
          x_val, validation dataset
          x_test, testing dataset
  """

  input = x
  input = input.shuffle(buffer_size=len(input))

  train_size = int(0.6*len(input))
  val_size   = int(0.2*len(input))

  x_train = input.take(train_size).batch(batch_size, drop_remainder=True)
  x_val   = input.skip(train_size).take(val_size).batch(batch_size, drop_remainder=True)
  x_test  = input.skip(train_size + val_size).batch(batch_size, drop_remainder=True)

  return x_train, x_val, x_test
  
