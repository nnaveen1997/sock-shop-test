#Base Image
FROM python:3

#Directory for application
WORKDIR /test

#Install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

#Copy source code
COPY integration_test.py .

#Run the code
CMD [ "python", "integration_test.py" ]