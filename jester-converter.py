import csv
import cv2 as cv
import os, os.path
import numpy as np
import math
from multiprocessing import Pool

#settings:
jester_dataset_dir = '/mnt/storage/20bn-datasets/20bn-jester-v1/'
number_of_images_to_merge = 10
outout_directory = '/mnt/storage/out/'

# function to create an image of the swipe action.
def create_image(id):
    global jester_dataset_dir
    data_dir = jester_dataset_dir + id
    files = os.listdir(data_dir)
    files_count = len(files)
    if files_count < 10:
        return merge_images(1)
    else:
        mod = int(math.floor(files_count/number_of_images_to_merge))
        images = []
        for name in os.listdir(data_dir):
            file = data_dir + '/' + name
            if os.path.isfile(file) == False:
                continue
            stripped = name.strip('0').replace('.jpg', '')
            if (stripped.isdigit() == False):
                continue

            int_in_name = int(float(stripped))

            if (int_in_name == 1 or int_in_name % mod == 0) and len(images) < number_of_images_to_merge:
                images.append(cv.imread(file))
        return merge_images(images)


def merge_images(images):
    if len(images) != number_of_images_to_merge:
        raise Exception('Number if image in input is not equal to settings. got '+ str(len(images)) +  ' instead of ' + str(number_of_images_to_merge))
    first_image = images[0]
    images.pop(0)
    for image in images:
        first_image = np.concatenate((first_image, image), axis=1)

    return first_image

def write_image(image, filename, type):
    target = outout_directory + type + '/' + filename
    cv.imwrite(target, image)

def process_row(row):
    if (row[1] == 'Swiping Left' or row[1] == 'Swiping Right'):
        # row[0] = id
        # row[1] = action
        merged_image = create_image(row[0])
        write_image(merged_image, row[0] + '.jpg', 'swipe')
    elif (row[1] == 'No gesture' or row[1] == 'Doing other things'):
        merged_image = create_image(row[0])
        write_image(merged_image, row[0] + '.jpg', 'unknown')

p = Pool(75)
with open('jester.csv', newline='') as csvfile:
    count = 0;
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        p.map(process_row, [row])





