FROM node:lts-slim

RUN npm install pm2 -g --registry http://registry.npm.taobao.org

COPY ./src /src
WORKDIR /src

RUN npm install --registry http://registry.npm.taobao.org

EXPOSE 3000

CMD [ "pm2-runtime", "index.js" ]