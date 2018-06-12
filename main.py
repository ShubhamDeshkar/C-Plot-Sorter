import os
import glob
import shutil
import datetime
from datetime import datetime


# It is assumed that this code file resides just outside the test-data
# folder.
test_data_path = os.path.join(os.getcwd(), 'test-data')
os.chdir(test_data_path)
gif_plots = glob.glob('*.gif')

for plot in gif_plots:
      filename = plot
      plot = plot.split('-')
      date_name = plot[0]
      print(date_name)
