import pandas as pd
import kagglehub

def extract():
    path = kagglehub.dataset_download("walekhwatlphilip/intro-to-data-cleaning-eda-and-machine-learning")
    data = pd.read_csv(path+'/bi.csv', encoding='latin1')
    return data