FROM python:3.10.6-buster
COPY backend/api /api
COPY model /model
COPY requirements.txt /requirements.txt
COPY model/yolov7/requirements.txt /model_requirements.txt
COPY temp_file_from_user.jpg /temp_file_from_user.jpg
RUN apt update
RUN apt install -y zip htop screen libgl1-mesa-glx
RUN pip install --upgrade pip
RUN pip install thop
RUN pip install -r /requirements.txt
RUN pip install -r /model_requirements.txt
RUN mkdir public
CMD uvicorn predict:app --host 0.0.0.0 --app-dir /api --port $PORT
