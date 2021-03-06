
import os
from typing import Callable

# TODO write data from template in file
# TODO add try/except
def create_file(fname, mode = 'w'):
  '''Create new files 
  Args:
      fname (str): Name of the file
      mode (str): Mode to open the file. Default is `w` (write mode)
        More info in [Python's official documentation](https://docs.python.org/3/library/functions.html#open)
  '''
  with open(fname, mode):
    pass

def create_directory(dirname, path = '.', permits = 0o777):
  '''Create a leaf directory and all intermediate ones
  This is a wrapper to os.makedirs()
  Args:
      dirname (str): Name of the directory
      path (str): Path to the directory to be created
      permits (oct): Directory permits
  '''
# TODO improve try/except with a good code error and message
  try:
    os.makedirs(os.path.join(path, dirname), mode = permits, exist_ok = False)
  except OSError as err:
    print(str(err))

def traverse(x, f: Callable) -> None:
  '''Traverse dictionary and apply a function to keys and values
  Args:
      x (dict): Dictionary with a valid project structure
      f (function): function to apply to keys and values in `obj`
  '''
  if isinstance(x, dict) and len(x):
    f(x)
  elif isinstance(x, list) and len(x):
    for item in x:
      if isinstance(item,dict): 
        traverse(item, f)
      else:
        raise Exception('Not a dictionary node')
  else:
    raise Exception('Not a list or dictionary object')


# TODO transfer this code to tests
# if __name__ == '__main__':

#   x = {
#        'type':'directory',
#        'name':'dir-a',
#        'contents':[
#              {'type':'file','name':'f-1.txt'},
#              {'type':'file','name':'f-2.txt'},
#              {'type':'directory',
#               'name':'dir-b',
#               'contents':[]
#              },
#              {'type':'directory',
#               'name':'dir-c',
#               'contents':[
#                 {'type':'file','name':'f-3.txt'},
#               ]
#              },
#            ]
#       }

#   traverse(x, transform)

# TODO Create another function to calculate the sha256 of files and directories for testing
# TODO Use the traverse function to calculate all the sha256.
# Do I need to add those sha in another structure or in the YAML file?