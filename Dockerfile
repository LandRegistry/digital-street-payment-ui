# Set the base image to the base image

FROM hmlandregistry/dev_base_python_flask:4

RUN yum install -y -q libffi-devel openssl

# HTTPS cert
RUN mkdir -p /supporting-files && \
  cd /supporting-files && \
  openssl req \
    -new \
    -newkey rsa:4096 \
    -days 365 \
    -nodes \
    -x509 \
    -subj "/C=GB/L=London/O=HM Land Registry/CN=localhost" \
    -keyout ssl.key \
    -out ssl.cert

RUN cd /supporting-files && curl -SLO "https://nodejs.org/dist/v8.11.3/node-v8.11.3-linux-x64.tar.xz" && \
tar -xJf "node-v8.11.3-linux-x64.tar.xz" -C /usr/local --strip-components=1 && \
ln -s /usr/local/bin/node /usr/local/bin/nodejs && \
rm "node-v8.11.3-linux-x64.tar.xz"


# Install node modules
# These are installed outside of the mounted volume and nodejs is instructed to look for them by setting NODE_PATH / PATH
# This is to avoid the fact that the volume will wipe out anything that gets added when the container is being built
ENV NODE_PATH='/supporting-files/node_modules' \
  PATH="/supporting-files/node_modules/.bin:${PATH}" \
  NODE_ENV='production' \
  NPM_CONFIG_PRODUCTION='false'
ADD package*.json /supporting-files/
RUN cd /supporting-files \
  && npm install


# Get the python environment ready.
ADD requirements_test.txt requirements_test.txt
ADD requirements.txt requirements.txt
RUN pip3 install -q -r requirements.txt && \
  pip3 install -q -r requirements_test.txt


# Put your app-specific stuff here (extra yum installs etc).
# Any unique environment variables your config.py needs should also be added as ENV entries here
ENV APP_NAME=payment-ui \
  MAX_HEALTH_CASCADE=6 \
  LOG_LEVEL=DEBUG \
  SECRET_KEY='ABC' \
  FLASK_DEBUG=1 \
  CONTENT_SECURITY_POLICY_MODE='full' \
  STATIC_ASSETS_MODE='development'

CMD ["./run.sh"]

