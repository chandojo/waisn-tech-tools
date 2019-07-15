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

# Running the Server

There are a few environment settings that need to be enabled to run the server. The reason for this is because the
website is protected using Auth0. Hence the following environment variables need to be declared. Note that the Auth0
application should be configured to be a **Regular Web Application**.

* `AUTH0_DOMAIN`: The Auth0 application's domain
* `AUTH0_KEY`: The Auth0 application's client id
* `AUTH0_SECRET`: The Auth0 application's client secret.

## Disabling Auth0

Runnning the service locally without access to the internet requires authentication to be disabled. This can be done by
setting the environment variable:

```
# disable Auth0 login requirement
export WAISN_AUTH_DISABLED='TRUE'
```

# Docker

You can build the web application using the provided Docker file. Currently, only an image that can be used for testing
has been created:

```
# build the Docker image
docker build -f Dockerfile.test .
# run the docker file
docker run -p 8000:8000 --rm [environment variables to enable Auth0] ${IMAGE_ID}
```
