# setup.py is a python file, which usually tells you that the module/package 
# you are about to install has been packaged and distributed with Distutils,
# which is the standard for distributing Python Modules.

# This allows you to easily install Python packages. Often it's enough to write:

# > python setup.py install

# and the module will install itself.

# Read second answer:
# https://stackoverflow.com/questions/1471994/what-is-setup-py


# If you downloaded package that has "setup.py" in root folder, you can install it by
# running python setup.py install

# If you are developing a project and are wondering what this file is useful for,
# check Python documentation on writing the Setup Script
# https://docs.python.org/3/distutils/introduction.html#distutils-simple-example
# https://docs.python.org/3/distutils/setupscript.html


# most information that you supply to the Distutils is supplied as keyword arguments
# to the setup() function

# those keyword arguments fall into two categories: package metadata 
# (name, version number) and information about what’s in the package (a list of
# pure Python modules, in this case)

# modules are specified by module name, not filename (the same will hold true
# for packages and extensions)

# it’s recommended that you supply a little more metadata, in particular your name,
# email address and a URL for the project

# sdist = Source distribution

# To create a source distribution for this module, you would create a setup script,
# setup.py, containing the above code, and run this command from a terminal:

# setup.py sdist

# sdist will create an archive file (e.g., tarball on Unix, ZIP file on Windows)
# containing your setup script setup.py, and your module foo.py. The archive file
# will be named foo-1.0.tar.gz (or .zip), and will unpack into a directory foo-1.0.

# If an end-user wishes to install your foo module, all they have to do is download
# foo-1.0.tar.gz (or .zip), unpack it, and—from the foo-1.0 directory—run

# python setup.py install

# which will ultimately copy foo.py to the appropriate directory for third-party 
# modules in their Python installation.


# sdist will create an archive file (e.g., tarball on Unix, ZIP file on Windows) 
# containing your setup script setup.py, and your module foo.py. The archive file
# will be named foo-1.0.tar.gz (or .zip), and will unpack into a directory foo-1.0.

# https://en.wikipedia.org/wiki/Archive_file

# If an end-user wishes to install your foo module, all they have to do is download
# foo-1.0.tar.gz (or .zip), unpack it, and—from the foo-1.0 directory—run

# python setup.py install

# which will ultimately copy foo.py to the appropriate directory for third-party
# modules in their Python installation.



# This simple example demonstrates some fundamental concepts of the Distutils.
# First, both developers and installers have the same basic user interface,
# i.e. the setup script. The difference is which Distutils commands they use:
# the sdist command is almost exclusively for module developers, while install is
# more often for installers (although most developers will want to install 
# their own code occasionally).

# **** READ TERMINOLOGY AT BOTTOM OF FIRT PYTHON.ORG LINK ABOVE ****

# **** SO GOOD ****
# https://realpython.com/python-application-layouts/


# *** LPTHW VID ***

# hello(**args) will take the arguments from a dictionary called args to populate the
# two parameters of args.

# __pycache__ <-- compiled code that it runs after the first time you run it
# to be faster

# cp -r skeleton ex46
# that's a way to copy the skeleton in command line (he is in lpthw virtualenv)

# to rename in powershell just do 'mv NAME ex46'

# python setup.py install
# pip uninstall ex46


https://realpython.com/python-virtual-environments-a-primer/

# our virtual environment’s bin directory is now at the beginning of the path.
# That means it’s the first directory searched when running an executable on the 
# command line. Thus, the shell uses our virtual environment’s instance of
# Python instead of the system-wide version.


### That's the badger ###

https://packaging.python.org/guides/installing-using-pip-and-virtualenv/

# As long as your virtualenv is activated pip will install packages into that 
# specific environment and you’ll be able to import and use packages 
# in your Python application.

# If you want to switch projects or otherwise leave your virtualenv, simply run:

# deactivate





# pip install virtualenv
# mkdir .venvs
# virtualenv --system-site-packages .venvs/lpthw
# .\.venvs\lpthw\Scripts\activate    <--This has to be from home directory (cd ~)
# type deactivate to get out of virtual environment

# (lpthw) > pip install nose

# cp -r c:\Users\Sean\projects\skeleton ex47


