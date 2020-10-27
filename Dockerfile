FROM python:3
WORKDIR /server
RUN pip install Flask
COPY *.py ${PWD}
EXPOSE 5000
ENV FLASK_APP=hello.py
CMD [ "flask", "run" ]