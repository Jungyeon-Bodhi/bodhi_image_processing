# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:35:48 2024

@author: Bodhi Global Analysis
"""

import os
import pandas as pd
from PIL import Image

class Question:
    
    def __init__(self, number, page_number, type_q, question_set):
        """
        - Initialise the question class

        number: int, Number of the question
        page_number: int, Number of the pdf page
        type_q: str, Type of the question ('single','multi','open-ended')
        question_set: dic, Dictionary that contains the coordinates of each checkbox and the corresponding answers
        """
        self.number = number
        self.page_number = page_number
        self.type_q = type_q
        self.question_set = question_set
    

class Image_processing:

    def __init__(self, name, image_path, sample_size):
        """
        - Initialise the image processing class

        name: int, Name of the project
        image_path: str, Directory of processed image files
        sample_size: int, Total number of samples
        """
        self.name = name
        self.image_path = image_path
        self.questions = []
        self.sample_size = sample_size
        
    def add_question(self, question):
        """
        - Add question classes into the image processing class

        question: question, Question class object
        """
        self.questions.append(question)

    def set_df(self):
        """
        - Initialise an empty dataset
        """
        self.df = pd.DataFrame(columns=[question.number for question in self.questions])
        
    def save(self, path):
        """
        - Extract the final dataset
        
        path: str, Directory for saving the final dataset
        """        
        self.df.to_excel(path, index=False)

    def processing(self, threshold=0.7):
        """
        - Implement the image processing
        
        threshold: float, Threshold settings for the checkbox
        """ 
        image_path = self.image_path
        df = self.df

        for question in self.questions:
            if question.type_q == 'single':
                for i in range(1, self.sample_size+1):
                    image_name = f'{i}_{question.page_number}.jpg'
                    image = os.path.join(image_path, image_name)
                    img = Image.open(image).convert('RGB')          
                    width, height = img.size
                    results = {}
                    white_rgb = (255, 255, 255)
                    question_dict = question.question_set
                    for key, coordinates in question_dict.items():
                        for coord, value in coordinates.items():
                            x1, y1, w, h = coord
                            x2, y2 = x1 + w, y1 + h
                        
                            if x2 > width or y2 > height:
                                results[value] = 'missing value'
                                continue
            
                            crop = img.crop((x1, y1, x2, y2))
                            total_pixels = crop.size[0] * crop.size[1]
                            
                            non_white_count = sum(1 for pixel in crop.getdata() if pixel != white_rgb)
                
                            if non_white_count / total_pixels >= threshold:
                                results[value] = value
                                break
                            else:
                                results[value] = 'missing value'
                                break
                    a = [key for key, value in results.items() if value != 'missing value']
                    a = ''.join(a)
                    df.loc[i, question.number] = a
                    self.df = df
                    
            elif question.type_q == 'open-ended':
                for i in range(1, self.sample_size+1):
                    df.loc[i, question.number] = 'open-ended'
                    self.df = df
                    
            elif question.type_q == 'multi':
                
                df.drop(columns=[str(question.number)], inplace=True, errors='ignore')
                
                for i in range(1, len(question.question_set) + 1):
                    df[f"{question.number}_{i}"] = 0 
                    
                for i in range(1, self.sample_size+1):
                    image_name = f'{i}_{question.page_number}.jpg'
                    image = os.path.join(image_path, image_name)
                    img = Image.open(image).convert('RGB')          
                    width, height = img.size
                    results = {}
                    white_rgb = (255, 255, 255)
                    question_dict = question.question_set
                    for key, coordinates in question_dict.items():
                        for coord, value in coordinates.items():
                            x1, y1, w, h = coord
                            x2, y2 = x1 + w, y1 + h
                        
                            if x2 > width or y2 > height:
                                results[value] = 'missing value'
                                continue
            
                            crop = img.crop((x1, y1, x2, y2))
                            total_pixels = crop.size[0] * crop.size[1]
                            
                            non_white_count = sum(1 for pixel in crop.getdata() if pixel != white_rgb)
                
                            if non_white_count / total_pixels >= threshold:
                                results[value] = value
                                break
                            else:
                                results[value] = 'missing value'
                                break
                    a = [key for key, value in results.items() if value != 'missing value']

                    for number, coords in question.question_set.items():
                        for coord, value in coords.items():
                            if value in a:
                                df.loc[i, f"{question.number}_{number}"] = 1
                    self.df = df                