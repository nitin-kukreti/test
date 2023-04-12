FROM python:3
WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./solve.py" ]

# ENTRYPOINT ["python","program/temp.py"]