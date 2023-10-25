FROM python:3.8
WORKDIR /app
COPY /src /app/src
RUN pip3 install Flask
EXPOSE 8080
CMD ["python3", "src/fortune_teller.py"]