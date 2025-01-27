FROM python:3.12.6

ADD assets /assets
ADD programs /programs
ADD src /src

RUN pip install nicegui
CMD ["python", "src/gui.py"]