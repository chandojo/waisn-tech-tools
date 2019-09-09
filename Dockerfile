FROM continuumio/miniconda:4.6.14 AS waisntechtools-base
LABEL waisntechtools-image-type=base

ENV SERVER_PORT 8000
ENV SRC_DIR /opt/waisn-tech-tools/

# copy source code
RUN mkdir -p $SRC_DIR
COPY ./environment-docker.yml $SRC_DIR
COPY ./waisntechtools/waisntechtools/ $SRC_DIR/waisntechtools/waisntechtools/
COPY ./waisntechtools/alerts/ $SRC_DIR/waisntechtools/alerts
COPY ./waisntechtools/manage.py $SRC_DIR/waisntechtools/manage.py

# set up conda env
WORKDIR $SRC_DIR
RUN conda env create -f environment-docker.yml

# run tests to sanity check image build
WORKDIR $SRC_DIR/waisntechtools
RUN . /opt/conda/etc/profile.d/conda.sh && \
    conda activate waisn-tech-tools && \
    python manage.py test

# expose runtime port - exposing debug port for now until creating production configuration
EXPOSE $SERVER_PORT

# set up some environment variables
ENV AUTH0_DOMAIN AUTH0_DOMAIN
ENV AUTH0_KEY AUTH0_KEY
ENV AUTH0_SECRET AUTH0_SECRET

# run migrations
RUN . /opt/conda/etc/profile.d/conda.sh && \
    conda activate waisn-tech-tools && \
    python manage.py migrate

# build development image
FROM waisntechtools-base as waisntechtools-dev
LABEL waisntechtools-image-type=dev
ENV WAISN_AUTH_DISABLED TRUE
ENTRYPOINT . /opt/conda/etc/profile.d/conda.sh && \
    conda activate waisn-tech-tools && \
    python manage.py runserver 0.0.0.0:$SERVER_PORT

# build production image
FROM waisntechtools-base as waisntechtools-prod
LABEL waisntechtools-image-type=prod
ENV WAISN_AUTH_DISABLED FALSE

ENV DJANGO_SECRET_KEY DJANGO_SECRET_KEY
ENV DB_HOSTNAME DB_HOSTNAME
ENV DB_PORT DB_PORT
ENV DB_NAME DB_NAME
ENV DB_USERNAME DB_USERNAME
ENV DB_PASSWORD DB_PASSWORD

# set up the static files to be served by web server
RUN . /opt/conda/etc/profile.d/conda.sh && \
    conda activate waisn-tech-tools && \
    python manage.py collectstatic --settings waisntechtools.settings.production

ENTRYPOINT . /opt/conda/etc/profile.d/conda.sh && \
    conda activate waisn-tech-tools && \
    python manage.py runserver --settings waisntechtools.settings.production 0.0.0.0:$SERVER_PORT
