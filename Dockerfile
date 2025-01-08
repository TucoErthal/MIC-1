FROM python:3.11
ADD main.py .
RUN pip install nicegui
CMD ["python", "./main.py"]