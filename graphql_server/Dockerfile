FROM node:14-stretch-slim

WORKDIR /usr/src/app

COPY package.json ./

RUN yarn install --verbose

COPY . .

CMD [ "sleep", "infinity" ]
