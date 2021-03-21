import cv2

# image
img = 'images.jpeg'

# pretrained classifier
classifier = 'cars.xml'

# create open cv image
img = cv2.imread(img)

# create car classifier
car_tracker = cv2.CascadeClassifier(classifier)


print('code ran')
