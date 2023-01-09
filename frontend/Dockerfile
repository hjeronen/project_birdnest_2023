# Build React static files
FROM node:18.12.1-bullseye-slim as build

WORKDIR /app

COPY . .

RUN npm ci
RUN npm run build

# Copy React static files and start nginx
FROM nginxinc/nginx-unprivileged
COPY --from=build /app/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d

EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]