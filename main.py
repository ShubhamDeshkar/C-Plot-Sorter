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
      test_data_path = os.path.join(os.getcwd(), 'test-data')
      os.chdir(test_data_path)
      gif_plots = os.listdir(test_data_path)

      for plot in gif_plots:
            filename = plot
            file_path = os.path.join(os.getcwd(), filename)
            if(os.path.isfile(file_path)):
                  if(ismatch(filename)):
                        plot = plot.split('-')
                        date_name = plot[0]

                        # Convert date_name into datetime objects.
                        date_time_object = datetime.datetime.strptime(date_name,
                                                                      '%Y%m%d').date()
                        year_month_day = str(date_time_object).split('-')

                        day_folder_path   = os.path.join(os.getcwd(), year_month_day[0],
                                                   year_month_day[1], year_month_day[2])

                        if(not os.path.exists(day_folder_path)):
                              os.makedirs(day_folder_path)

                        # Moves the file into its proper directory
                        shutil.move(file_path, day_folder_path)
