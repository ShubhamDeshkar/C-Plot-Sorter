import os
import glob
import datetime
import shutil


# It is assumed that this code file resides just outside the test-data
# folder.
test_data_path = os.path.join(os.getcwd(), 'test-data')
os.chdir(test_data_path)
print(glob.glob('*.gif'))


