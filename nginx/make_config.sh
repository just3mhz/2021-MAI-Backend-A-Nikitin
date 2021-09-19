set -eu

envsubst '${NGINX_USER} ${NGINX_PUBLIC}' < nginx.conf.template > nginx.conf
