# - There are 20 folders. Use them to make a training set and a testing set.
# - The testing set should include:
# * All the documents from the folder "comp.windows.x". Their label should be "comp".
# * All the documents from the folder "rec.sport.baseball". Their label should be "sports".
# * All the documents from the folder "talk.politics.misc". Their label should be "politics".
# * All the documents from "rec.autos". Their label should be "rec".

# - You can use any of the other folders to build the training set. You can use as many documents and folders as you
# want. You cannot use documents from the 4 folders of the testing set. You cannot use external documents that are not
# from the 20 newsgroups dataset.
# - Write a classification script that reads the 20 newsgroups dataset, creates the training and testing sets and gets
# the maximum possible accuracy on the testing set.
# - IMPORTANT: MAKE SURE THAT YOUR SCRIPT ALWAYS DELETES AND IGNORES ALL THE LINES THAT APPEAR BEFORE THE FIRST EMPTY
# LINE OF EACH DOCUMENT. THIS APPLIES TO BOTH TESTING AND  TRAINING DOCUMENTS. This has to happen before you train and
# apply the model.
# - Submit the script.
# - This is a team assignment.
# - You get 10 points if you submit a script that works, even if the accuracy is low.
# - You get +2 points for every team that get a lower accuracy than yours.

import os
import os.path
import sklearn as skl
import pandas as pd


def load_data(fname):
    with open(fname, encoding="utf8", errors='ignore') as f:
        found_break = False
        article_text = ""
        for line in f:
            if found_break:
                article_text = article_text + " " + line
            if line == '\n' and len(line) <= 3:
                found_break = True
        f.close()
    article_text = article_text.replace('\n', ' ')
    return article_text


# function to read in data files and return training and testing data frames
def read_data():
    rev_train = []
    labels_train = []
    rev_test = []
    labels_test = []
    test_file_names = ['20_newsgroups/comp.windows.x', '20_newsgroups/rec.sport.baseball',
                       '20_newsgroups/talk.politics.misc', '20_newsgroups/rec.autos']
    folder_path = "20_newsgroups"
    newsgroups = [x[0] for x in os.walk(folder_path)]
    newsgroups = newsgroups[1:]
    for subfolder in newsgroups:
        label = subfolder[14:]
        file_names = os.listdir(subfolder)
        for file in file_names:
            rev = load_data(subfolder + "/" + file)
            if subfolder in test_file_names:
                for _ in range(1, len(rev)): labels_train.append(label)
                rev_test.append(rev)
            else:
                for _ in range(1, len(rev)): labels_test.append(label)
                rev_train.append(rev)
    print(rev_train[0:1])
    print(labels_train[0:1])
    print(rev_test[0:1])
    print(labels_test[0:1])
    return rev_train, labels_train, rev_test, labels_test


def main():
    rev_train, labels_train, rev_test, labels_test = read_data()
    train_df = pd.DataFrame(list(zip(labels_train, rev_train)), columns=['Label', 'Text'])
    test_df = pd.DataFrame(list(zip(labels_test, rev_test)), columns=['Label', 'Text'])
    train_df.to_csv("Train.csv")
    test_df.to_csv("Test.csv")
    clf = ""


main()
