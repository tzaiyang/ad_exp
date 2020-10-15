import os
import random
import fnmatch

train_bags = ["{}{:03d}".format("Train",x) for x in range(1,17)]
test_bags = ["{}{:03d}".format("Test",x) for x in range(1,13)]

positive_bags = []
negative_bags = []
# Randomly choose 6 anomaly videos from Test directory
while(len(positive_bags)<6):
   x = random.randint(1,12)
   temp_s = "{}{:03d}".format("Test",x)
   if temp_s not in positive_bags:
     positive_bags.append(temp_s)

# Randomly choose 4 normaly videos from Train directory
while(len(negative_bags)<4):
   x = random.randint(1,16)
   temp_s = "{}{:03d}".format("Train",x)
   if temp_s not in negative_bags:
     negative_bags.append(temp_s)


dataset_dir = "/AnomalyDetection_data/UCSD_Anomaly_Dataset_v1p2/UCSDped2"
# re_train_bags=positive_bags+negative_bags

def count_files(directory, postfix_list):
    lst = os.listdir(directory)
    cnt_list = len(fnmatch.filter(lst, '*'+postfix_list))
    return cnt_list

with open("train_split_list.txt","w") as f:
  for vid_name in positive_bags:
    vipath="{}/Test/{}".format(dataset_dir,vid_name)
    vinumber=count_files(vipath,'.tif')
    f.write("{} {} 1\n".format(vipath,vinumber))
  for vid_name in negative_bags:
    vipath="{}/Train/{}".format(dataset_dir,vid_name)
    vinumber=count_files(vipath,'.tif')
    f.write("{} {} 0\n".format(vipath,vinumber))

# re_test_bags=list(set(train_bags)-set(negative_bags))+list(set(test_bags)-set(positive_bags))
with open("test_split_list.txt","w") as f:
  for vid_name in list(set(test_bags)-set(positive_bags)):
    vipath="{}/Test/{}".format(dataset_dir,vid_name)
    vinumber=count_files(vipath,'.tif')
    f.write("{} {} 1\n".format(vipath,vinumber))
  for vid_name in list(set(train_bags)-set(negative_bags)):
    vipath="{}/Train/{}".format(dataset_dir,vid_name)
    vinumber=count_files(vipath,'.tif')
    f.write("{} {} 0\n".format(vipath,vinumber))

