# waisn-tech-tools

Tech tools for the WAISN.

# Setting up Environment

[Anaconda][] is used to manage the python environment that the project runs in. After installing, you can set up the
anaconda environment:

```
# create the conda env
conda env create -f ./environment.yml
# 'waisn-tech-tools' conda env should be listed
conda env list
# activate the environment
source activate waisn-tech-tools
# do a bunch of work
# ...
# ...
# deactivate the env
source deactivate
```

[Anaconda]: https://www.anaconda.com/

# Updating the Environment

If you are installing new packages, you will want to update the environment file as well.

```
# install new package
conda install new-package-name
# update environment file
conda env export > ./environment.yml
# please remove the "prefix" key from the file
```

# Project Commands

To see commands specific to the project, e.g. seeding, run:

```
python manage.py
```
