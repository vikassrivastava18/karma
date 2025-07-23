# frontend.Dockerfile

FROM node:20-alpine

WORKDIR /app

# These will work IF we mount frontend/karma into /app
COPY frontend/karma/package.json . 
RUN npm install


COPY ./frontend/karma /app

EXPOSE 8080

CMD ["npm", "run", "serve", "--", "--host", "0.0.0.0"]
