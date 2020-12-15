FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install ptvsd==4.3.2
COPY . .

EXPOSE 5000 4444

CMD [ "python", "./app.py" ]