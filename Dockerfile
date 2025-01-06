FROM python:3.6
COPY . /add
WORKDIR /add
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python","add.py"]
