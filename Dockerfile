FROM node:25.6.1 AS build

WORKDIR /work

COPY ui /work

RUN npm install -D vite
RUN npx vite build

FROM python:3.11 AS run

WORKDIR /server

COPY server .
RUN pip install -r requirements.txt

COPY --from=build /work/dist ./server/src/flaskr/static

CMD ["flask", "--app=src/flaskr", "run", "--host=0.0.0.0", "--port=1234"]
