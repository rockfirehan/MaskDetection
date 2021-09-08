import os,random
####create data.txt samples train:val=8:2
def createSampletxt():
    image_dir = "./mask_dataset"
    f_val = open("data_test.txt", 'w')
    f_train = open("data_train.txt", 'w')

    path, dirs, files = next(os.walk(image_dir))
    data_size = len(files)

    ind = 0
    data_test_size = int(0.2 * data_size)
    test_array = random.sample(range(data_size), k=data_test_size)

    for f in os.listdir(image_dir):
        if(f.split(".")[-1] == "jpg"):
            ind += 1

            if ind in test_array:
                f_val.write(image_dir+'/'+f+'\n')
            else:
                f_train.write(image_dir+'/'+f+'\n')

    f_train.close()
    f_val.close()