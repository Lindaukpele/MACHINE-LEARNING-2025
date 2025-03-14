import nltk    #It is natural langaguage toolkit. It has a lot of functions 
nltk.download()
import csv
from nltk.tokenize import word_tokenize #it returns list of words example 'I'am going to school' will return them as 4 words 1'am,  'going', 'to' and 'school.
from nltk.stem import WordNetLemmatizer #it reverts everything to the original form e.g swimming is reversed to swim
import numpy as np
import random
from collections import Counter
import os

#import numpy as py

#import pandas as pd
df = pd.read_csv("mushrooms.csv")

