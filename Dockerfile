FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt
# root-user-action=ignore may be dangerous if the root image is changed from one of the official python images

COPY . .

CMD [ "python3", "./main.py" ]