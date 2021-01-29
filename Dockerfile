FROM python:3-alpine

# Copy app files
COPY app /usr/src/app/

# Copy requirements file for pip3 to use
COPY ./requirements.txt /usr/src/app/

# Install app dependencies using pip3
RUN pip3 install -r /usr/src/app/requirements.txt

# Run script to insert data into mysql database
CMD ["python", "/usr/src/app/insert.py"] 