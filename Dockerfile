FROM python:3.6
ADD . /iqvizyon_proje
WORKDIR /iqvizyon_proje
RUN pip install -r requirements.txt
