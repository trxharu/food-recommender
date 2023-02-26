FROM node:lts-alpine as build
WORKDIR /frontend
COPY . .
RUN yarn install
RUN yarn build

FROM nginx:alpine
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /frontend/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]