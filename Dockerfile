FROM python:3.10.4-slim

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

COPY model.py model.bin dv.bin /app/

EXPOSE 8081

# Command to run the Flask app with Gunicorn
CMD ["pipenv", "run", "waitress-serve", "--port=8081", "model:app"]