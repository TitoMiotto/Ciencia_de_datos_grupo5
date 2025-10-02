import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np

boston = pd.read_csv('datosCrudos.csv')
boston.head()

boston.describe()