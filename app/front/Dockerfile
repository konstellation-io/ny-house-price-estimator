
FROM node:14.15.4-alpine3.10 as front-builder

LABEL maintainer="Intelygenz - Konstellation Team"
ARG VERSION
WORKDIR /app

COPY . .

RUN yarn install --network-timeout 1000000
RUN yarn run build

FROM nginx:alpine

COPY --from=front-builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
