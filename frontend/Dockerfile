FROM python:3.9

COPY ./req.txt .
RUN pip install -r req.txt

WORKDIR /app
COPY . .

EXPOSE 80

ENTRYPOINT [ "streamlit", "run", "frontend.py", "--server.address=0.0.0.0", "--server.port=80"]