FROM python:3.9.0-slim

RUN apt-get update && apt-get install -y \
      python-dev python3-dev \
      build-essential libssl-dev libffi-dev \
      libxml2-dev libxslt1-dev zlib1g-dev

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sleep", "infinity"]
# CMD [ "python3", "./run_spider.py"]


