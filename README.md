The ‘qr_processing.py’ script performs the following functions.

① Idenfity QR codes within the image
-> To do this, this script adjusts the brightness of the image

② Rename the image
-> Based on the fourth QR code, the script renames the image in the format n1_n2.jpg (where n1 is the respondent ID, and n2 is the page number)

③ Crops the image for image processing
-> Using the top-left (TL) and top-right (TR) QR codes as reference points, the script crops the image so these two QR codes define its edges

④ Merge images into a single PDF (15 pages == 1 PDF)
-> This script merges images into PDFs (both original and resized images)
-> It also notifies us if a PDF has fewer than 15 pages, allowing us to manually add data from the physical copies as needed

The ‘image_processing.py’ script implements the following functions.

① Create a question class that includes the coordinates of each checkbox and the corresponding answers

② Check if more than 70% of a check box is filled with non-white pixels
-> If yes, it generates the corresponding answer
-> If no checkboxes are filled, it generates a "missing value"
-> This process does not support open-ended questions

③ Aggregate all data into a data frame and save it
