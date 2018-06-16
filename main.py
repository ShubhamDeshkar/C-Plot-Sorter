import os
import glob
import shutil
import datetime
import re



# It is assumed that this code file resides just outside the test-data
# folder.

def ismatch(filename):
      # match the pattern for 8 digit followed by a '-' followed by 6 digits
      regex = re.compile('\d\d\d\d\d\d\d\d-\d\d\d\d\d\d')

      # if filename matches the pattern return True
      if(regex.search(filename)):
            return 'True'
      else:
            return 'False'


if __name__ == '__main__':
      # get the test-data folder path
      test_data_path = os.path.join(os.getcwd(), 'test-data')
      os.chdir(test_data_path)

      # list all the files and folders inside test-data path
      gif_plots = os.listdir(test_data_path)

      for plot in gif_plots:
            filename = plot
            # create a path for the filename
            file_path = os.path.join(os.getcwd(), filename)
            # if file path is a file, proceed
            if(os.path.isfile(file_path)):
                  # check if the filename matches the pattern
                  if(ismatch(filename) == 'True'):
                        # split about '-'
                        plot = plot.split('-')
                        # save the first element (index=0)
                        date_name = plot[0]

                        # Convert date_name into datetime objects.
                        date_time_object = datetime.datetime.strptime(date_name,
                                                                      '%Y%m%d').date()
                        # split about '-' ['yyyy', 'mm', 'dd']
                        year_month_day = str(date_time_object).split('-')

                        # create a folder path using above list elements
                        day_folder_path   = os.path.join(os.getcwd(), year_month_day[0],
                                                   year_month_day[1], year_month_day[2])

                        # create the folder if not present already
                        if(not os.path.exists(day_folder_path)):
                              os.makedirs(day_folder_path)

                        # Move the file into its proper directory
                        shutil.move(file_path, day_folder_path)
