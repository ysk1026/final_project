import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from util.file_helper import FileReader
basedir = os.path.dirname(os.path.abspath(__file__))
import pandas as pd
import numpy as np

class ReviewModel:
    
    def __init__(self):
        print(f'basedir ####{basedir}')
        self.reader = FileReader()
        
    def hook_process(self):
        review = self.get_review()
        print(f'{review}')
    
    def get_review(self):
        reader = self.reader
        reader.context = os.path.join(basedir, 'data')
        reader.fname = 'ratings.train.txt'
        reader.new_file()
        review = reader.csv_to_dframe()
        # review = pd.read_csv(reader.new_file(), encoding='UTF-8', delimiter =',')
        # review = reader.csv_to_dframe()
        print(f'{review.head()}')
        return review
    
if __name__ == '__main__':
    model = ReviewModel()
    model.hook_process()
    # model.get_review()