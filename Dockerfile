FROM python:3
WORKDIR /server
RUN pip install Flask
COPY server.py $PWD
EXPOSE 5000
ENV FLASK_APP=server.py
CMD [ "flask", "run", "--host=0.0.0.0" ]