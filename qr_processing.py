#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:13:44 2024

@author: Bodhi Global Analysis
"""

import os
import cv2
from PIL import Image
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
from collections import defaultdict

class QR_reader:
    
    def __init__(self, input_folder, output_folder, pdf_folder):
        """
        - Initialise the QR reader class

        input_folder: str, Directory containing the raw images (scanned papers)
        output_folder: str, Directory to save the processed images
        pdf_folder: str, Directory to save the merged PDF file
        """
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.pdf_folder = pdf_folder
        
    def process_images(self):
        """
        - Conducting the QR reader
        """
        input_folder = self.input_folder
        output_folder = self.output_folder
        output_folder_original = f"{self.output_folder}/original"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"Output folder created: {output_folder}")
    
        for filename in os.listdir(input_folder):
            if filename.lower().endswith((".jp2",".jpeg",".png",".jpg")):  # Check for image file types
                img_path = os.path.join(input_folder, filename)
                print("")
                print(f"Processing file: {img_path}")
                img = cv2.imread(img_path)
                img_original = img
                height, width = img.shape[:2]
                img = cv2.resize(img, (width * 1, height * 1), interpolation=cv2.INTER_LANCZOS4)
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                h, s, v = cv2.split(hsv)
    
                lim = 255 - 120
                v[v > lim] = 255
                v[v <= lim] += 90
    
                final_hsv = cv2.merge((h, s, v))
                img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
                if img is None:
                    print(f"Error loading image: {img_path}")
                    continue
                
                decoded_objects = decode(img, symbols=[ZBarSymbol.QRCODE])
                print(f"Decoded {len(decoded_objects)} QR codes in {filename}.")
                
                new_values = []                
                
                for obj in decoded_objects:
                    data = obj.data.decode('utf-8')
                    
                    if not any(t in data for t in ['TL', 'TR', 'BL']):
                        try:
                            id_value, page_num = data.split(':')
                            new_value = f"{id_value}-{page_num}"
                            new_values.append(new_value)
                            print(f"Extracted value: {new_value}")
                            new_image_name = f"{id_value}_{page_num}.jpg"
                            new_image_path = os.path.join(output_folder, new_image_name)
                            new_image_path2 = os.path.join(output_folder_original, new_image_name)
                        except ValueError as e:
                            print(f"Error processing data '{data}': {e}")
    
    
                qr_data = {obj.data.decode('utf-8'): obj.rect for obj in decoded_objects}
                
                if 'TL' in qr_data and 'TR' in qr_data:
                    x_start = qr_data['TL'][0]
                    x_end = qr_data['TR'][0] + qr_data['TR'][1]
                
                    cropped_image = img[:,x_start:x_end]
                
                    cv2.imwrite(new_image_path, cropped_image)
                    cv2.imwrite(new_image_path2, img_original)
                    print("The image has been saved:", new_image_path)
                else:
                    print("Couldn't find the QR codes (TL or TR)")
    
    def group_participants(self):
        """
        - Group the images if they have the same participant ID
        """
        images_folder = self.output_folder
        images_info = defaultdict(list)

        for file_name in os.listdir(images_folder):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                try:
                    n1, n2 = file_name.split('_')
                    n2 = int(n2.split('.')[0])

                    image_path = os.path.join(images_folder, file_name)
                    images_info[n1].append((n2, image_path))
                except ValueError:
                    print(f"The format of the file is incorrect: {file_name}")
        
        for participant in images_info:
            images_info[participant].sort(key=lambda x: x[0])
        
        return images_info
    
    def create_pdf(self):
        """
        - Create a PDF by merging grouped images
        """
        images_info = self.group_participants()
        output_folder = self.pdf_folder
        self.lack_pdf = []
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"Output folder created: {output_folder}")
        
        for participant_id, images in images_info.items():

            first_image_path = images[0][1]
            image_list = [Image.open(path[1]).convert('RGB') for path in images]
    
            pdf_path = os.path.join(output_folder, f"{participant_id}_survey.pdf")
            
            if len(image_list) < 15:
                self.lack_pdf.append(pdf_path)
                print(f"{pdf_path} file contains fewer than 15 pages. ((Page number): {len(image_list)})")

            image_list[0].save(pdf_path, save_all=True, append_images=image_list[1:])
            print(f"New PDF has been saved: {pdf_path}")
