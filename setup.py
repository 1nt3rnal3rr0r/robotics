import shutil
import os
from subprocess import call
from distutils.dir_util import copy_tree

this_file_dir = os.path.dirname(os.path.realpath(__file__))

# build interface
os.chdir(os.path.join(this_file_dir, './interface'))
call(['yarn', 'build'], shell=True)

# copy new interface
dest = os.path.join(this_file_dir, './controller/react_build')
copy_tree(os.path.join(this_file_dir, './interface/build'), dest)
