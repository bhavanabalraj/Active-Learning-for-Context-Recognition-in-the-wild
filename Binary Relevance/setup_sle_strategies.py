import os

for i in range(51):
    os.chdir("label_" + str(i))
    os.system("python copy_model_sl.py " + str(i))
    os.chdir("../")
