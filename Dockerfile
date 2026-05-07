FROM node:20-alpine AS builder

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json* frontend/yarn.lock* ./

RUN npm install --legacy-peer-deps || yarn install --frozen-lockfile

COPY frontend/ ./

RUN npx expo export --platform web --output-dir dist

FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]