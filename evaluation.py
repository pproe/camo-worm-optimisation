import cv2 
import numpy as np
from util import prep_image
from matplotlib import pyplot as plt

IMG_MASK = [320, 560, 160, 880]

def detect_edges(image):
    # Performs simple canny edge detection on image and returns binary
    upper_threshold = 200
    lower_threshold = 100
    
    edges_detected = cv2.Canny(image, lower_threshold, upper_threshold)
    
    return edges_detected

def compare_edge_overlap(image1, image2):
    # Performs bitwise AND of image binarys

    overlap = cv2.bitwise_and(image1, image2)
    
    return overlap

def display_images(image1, image2, overlap):
    plt.subplot(131),plt.imshow(image1, cmap = 'gray')
    plt.title('Image 1'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(overlap, cmap = 'gray')
    plt.title('Overlap Of Images'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(image2, cmap = 'gray')
    plt.title('Image 2'), plt.xticks([]), plt.yticks([])
    
    plt.show()
    
def evaluate_images(image1_path, image2_path, display=False):
    
    # Read images
    img1 = cv2.imread(image1_path, 0)
    img2 = cv2.imread(image2_path, 0)

    # Resize image so they have matching dimensions
    dsize = img1.shape
    img2 = cv2.resize(img2, (dsize[1], dsize[0]))
    
    # Detect edges on both images
    img1_edges = detect_edges(img1)
    img2_edges = detect_edges(img2)
    
    # Compare overlapping edges and sum total
    overlap = compare_edge_overlap(img1_edges, img2_edges)
    
    # Higher score indicates more matching edges of the images
    edge_score = np.sum(overlap)
    
    # Optional: Display edges of images
    if(display):
        display_images(img1_edges, img2_edges, overlap)
    
    return edge_score


# ADJUST FOLLOWING PATHS TO IMAGES

IMG1_PATH = './images/blank_drawing.png'
IMG2_PATH = './gbest_imgs/gbest_24.png'

print("Score for iter 1: " + str(evaluate_images(IMG1_PATH, IMG2_PATH, True)))

IMG1_PATH = './images/blank_drawing.png'
IMG2_PATH = './images/blank_drawing.png'

#print("Score for Iter 24: " + str(evaluate_images(IMG1_PATH, IMG2_PATH, False)))