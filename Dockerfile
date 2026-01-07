# -------- Stage 1 : Build Angular App --------
FROM node:18-alpine AS build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .
RUN npm run build --configuration production

# -------- Stage 2 : Serve using Nginx --------
FROM nginx:alpine

COPY --from=build /app/dist/ecs-angular-app /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
