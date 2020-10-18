FROM node:14-stretch-slim

WORKDIR /usr/src/app

COPY package.json yarn.lock ./

ENV NODE_ENV=production

RUN yarn install --verbose

COPY . .

CMD [ "sleep", "infinity" ]
