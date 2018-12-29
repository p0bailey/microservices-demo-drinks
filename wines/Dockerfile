# our base image
FROM python:2

# install Python modules needed by the Python app
COPY web_app/requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY web_app/ /usr/src/app/

# tell the port number the container should expose
#EXPOSE 5000

# run the application
CMD ["python", "/usr/src/app/app.py"]
