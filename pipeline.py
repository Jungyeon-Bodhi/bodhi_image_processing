#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:02:48 2024

@author: Bodhi Global Analysis
"""

from qr_processing import QR_reader as qr
from image_processing import Question, Image_processing

# QR Reader Setting
input_folder = 'data/test' # Directory containing the raw images (scanned papers)
output_folder = 'data/result_image' # Directory to save the processed images
pdf_folder = 'data/result_pdf' # Directory to save the merged PDF file

# Create QR Reader and Implementing
bodhi_qr = qr(input_folder, output_folder, pdf_folder)
bodhi_qr.process_images()
bodhi_qr.create_pdf()

# Settings for creating a PDF with original images
output_folder2 = 'data/result_image/original'
pdf_folder2 = 'data/result_pdf/original'

original_save = qr(input_folder, output_folder2, pdf_folder2)
original_save.create_pdf()

# Image Processing Setting (Project name, Directory containing the processed images, Total number of samples)
carob = Image_processing('Carob', output_folder, 4)
carob.set_df()

# Details of the questions (checkbox coordinates and corresponding answers)
def questions_generate():
    question_1 = {
        1:{(424, 460, 15, 15): '18-24'},  # q1_1
        2:{(424, 500, 15, 15): '25-34'},  # q1_2
        3:{(424, 520, 15, 15): '35-44'},  # q1_3
        4:{(424, 550, 15, 15): '45-54'},  # q1_4
        5:{(424, 580, 15, 15): '55-64'},  # q1_5
        6:{(424, 610, 15, 15): '65 and over'},  # q1_6
    }
    
    question1 = Question(1, 1, 'single', question_1)
    carob.add_question(question1)
    
    question_2 = {
        1:{(424, 660, 15, 15): 'Upper Nile'}, 
        2:{(424, 690, 15, 15): 'Jonglei'},
        3:{(424, 720, 15, 15): 'Unity States'},
        4:{(424, 750, 15, 15): 'GPAA'},
    }
    
    question2 = Question(2, 1, 'single', question_2)
    carob.add_question(question2)
    
    question_3 = {
        1:{(424, 820, 15, 15): 'Male'}, 
        2:{(424, 850, 15, 15): 'Female'},
        3:{(424, 880, 15, 15): 'Non-binary'},
        4:{(424, 910, 15, 15): 'Other'},
        5:{(424, 940, 15, 15): 'Prefer not to say'},
    }
    
    question3 = Question(3, 1, 'single', question_3)
    carob.add_question(question3)
    
    question_4 = {
        1:{(424, 980, 15, 15): 'Yes'}, 
        2:{(424, 1010, 15, 15): 'No'},
        3:{(424, 1040, 15, 15): 'Prefer not to say'},
    }
    
    question4 = Question(4, 1, 'single', question_4)
    carob.add_question(question4)
    
    question_5 = {
        1:{(424, 1080, 15, 15): 'Yes'}, 
        2:{(424, 1110, 15, 15): 'No'},
    }
    
    question5 = Question(5, 1, 'single', question_5)
    carob.add_question(question5)
    
    question_6 = {
        1:{(424, 1160, 15, 15): 'NA'}, 
    }
    
    question6 = Question(6, 1, 'open-ended', question_6)
    carob.add_question(question6)
    
    question_7 = {
        1:{(424, 1210, 15, 15): 'Yes, own phone'}, 
        2:{(424, 1240, 15, 15): 'Yes, borrowed/family phone'},
        3:{(424, 1270, 15, 15): 'No'},
    }
    
    question7 = Question(7, 1, 'single', question_7)
    carob.add_question(question7)
    
    question_8 = {
        1:{(424, 1316, 15, 15): 'NA'}, 
    }
    
    question8 = Question(8, 1, 'open-ended', question_8)
    carob.add_question(question8)
    
    question_9 = {
        1:{(424, 1365, 15, 15): 'Yes'}, 
        2:{(424, 1395, 15, 15): 'No'},
    }
    
    question9 = Question(9, 1, 'single', question_9)
    carob.add_question(question9)
    
    question_10 = {
        1:{(424, 1440, 15, 15): 'NA'}, 
    }
    
    question10 = Question(10, 1, 'open-ended', question_10)
    carob.add_question(question10)
    
    question_11 = {
        1:{(424, 1548, 15, 15): 'Spouse'}, 
        2:{(424, 1578, 15, 15): 'Biological parent'},
        3:{(424, 1608, 15, 15): 'Biological parent'},
        4:{(424, 1636, 15, 15): 'Mother/Father-in-law'},
        5:{(424, 1664, 15, 15): 'Brother/Sister'},
        6:{(424, 1694, 15, 15): 'Relative'},
        7:{(424, 1722, 15, 15): 'Neighbour'}, 
        8:{(424, 1748, 15, 15): 'Friend'},
        9:{(424, 1778, 15, 15): 'Myself'},
    }
    
    question11 = Question(11, 1, 'single', question_11)
    carob.add_question(question11)
    
    question_12 = {
        1:{(424, 1826, 15, 15): 'Yes'}, 
        2:{(424, 1854, 15, 15): 'No'},
    }
    
    question12 = Question(12, 1, 'single', question_12)
    carob.add_question(question12)
    
    question_13 = {
        1:{(424, 1902, 15, 15): 'Yes'}, 
        2:{(424, 1932, 15, 15): 'No'},
    }
    
    question13 = Question(13, 1, 'single', question_13)
    carob.add_question(question13)
    
    question_14 = {
        1:{(424, 1980, 15, 15): 'Started but did not complete primary school'}, 
        2:{(424, 2034, 15, 15): 'Finished primary school'},
        3:{(424, 2067, 15, 15): 'Started but did not complete secondary school'},
        4:{(424, 2126, 15, 15): 'Finished secondary school'},
        5:{(424, 2154, 15, 15): 'University'},
    }
    
    question14 = Question(14, 1, 'single', question_14)
    carob.add_question(question14)
    
    question_33 = {
        1:{(1450, 2262, 60, 60): 'Rape'},
        2:{(1450, 2352, 60, 60): 'Sexual assault'},
        3:{(1450, 2442, 60, 60): 'Physical assualt'},
        4:{(1450, 2532, 60, 60): 'CEFMU'},
        5:{(1450, 2652, 60, 60): 'Denial of resources'},
        6:{(1450, 2800, 60, 60): 'Psychological emotional abuse'},
        7:{(1450, 2880, 60, 60): 'Female Genital Mutilation'},
        8:{(1450, 2960, 60, 60): 'Technology-related GBV'},
        9:{(1450, 3040, 60, 60): 'None'},
    }
    
    question33 = Question(33, 4, 'multi', question_33)
    #carob.add_question(question33)

# Create and save the questions to the image processing pipeline
questions_generate()

# Conduct the image processing pipeline
carob.processing()
carob.save("raw_data.xlsx")
