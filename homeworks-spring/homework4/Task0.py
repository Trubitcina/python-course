from scipy.ndimage import imread
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, \
    AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics.classification import accuracy_score


# my dataset http://pics.psych.stir.ac.uk/Other_face_databases.html
# function to get images from directory as matrix

# with shape of (n, 10000)
def get_images(dir_name):
    images = []
    for file_name in os.listdir(dir_name):
        x = imread(dir_name + "/" + file_name, flatten=True)
        x.shape = (10000, )
        images.append(x)
    images = np.array(images)
    return images

# lets get images from smile and non-smile directories
# and then shuffle them so our train/validation split is fair
smile = get_images("smile")
non_smile = get_images("non_smile")
np.random.shuffle(smile)
np.random.shuffle(non_smile)

print(smile.shape)
print(non_smile.shape)


# lets get 320 (160 smile and 160 non-smile) of images as training data
train_smile = smile[:160, ]
train_non_smile = non_smile[:160, ]

# other images are validation data
validate_smile = smile[160:, ]
validate_non_smile = non_smile[160:, ]

train = np.concatenate((train_smile, train_non_smile))
validate = np.concatenate((validate_smile, validate_non_smile))

# true classes 1 for smile image and 0 for non-smile image
train_y = np.concatenate((np.ones(160), np.zeros(160)))

forests = (RandomForestClassifier, ExtraTreesClassifier,
           AdaBoostClassifier, GradientBoostingClassifier)
estimators = (10, 20, 40, 80, 100, 150, 200, 300, 400, 500, 1000)

forest = []
for f in forests:
    for i in estimators:
        random_forest = f(n_estimators=i)
        random_forest = random_forest.fit(train, train_y)

        validate_y = np.concatenate((np.ones(40), np.zeros(40)))
        predicted_y = random_forest.predict(validate)
        print(accuracy_score(validate_y, predicted_y))
        forest.append(accuracy_score(validate_y, predicted_y))

result = open("forests.txt", "w")
result.write("n_estimators\t10\t20\t40\t80\t100\t150\t200\t300\t400\t500\t1000\n")
result.write("RandomForestClassifier" + "\t" + str(forest[0:11]) + "\n")
result.write("ExtraTreesClassifier" + "\t" + str(forest[11:22]) + "\n")
result.write("AdaBoostClassifier" + "\t" + str(forest[22:33]) + "\n")
result.write("GradientBoostingClassifier" + "\t" + str(forest[33:44]) + "\n")
