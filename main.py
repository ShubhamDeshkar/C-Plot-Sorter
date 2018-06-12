import os
import glob
import shutil
import datetime


# It is assumed that this code file resides just outside the test-data
# folder.

test_data_path = os.path.join(os.getcwd(), 'test-data')
os.chdir(test_data_path)
gif_plots = glob.glob('*.gif')

for plot in gif_plots:
      filename = plot
      plot_path = os.path.join(os.getcwd(), filename)
      plot = plot.split('-')
      date_name = plot[0]

      # Convert date_name into datetime objects.
      date_time_object = datetime.datetime.strptime(date_name, '%Y%m%d').date()
      year_month_day = str(date_time_object).split('-')

      #year_folder_path  = os.path.join(os.getcwd(), year_month_day[0])
      #month_folder_path = os.path.join(os.getcwd(), year_month_day[0], year_month_day[1])
      day_folder_path   = os.path.join(os.getcwd(), year_month_day[0], year_month_day[1], year_month_day[2])
      #shutil.move()
      print(plot_path)

      
