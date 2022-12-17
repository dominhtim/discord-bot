FROM python:3

# Setup app foler
WORKDIR /usr/src/app

# Setup venv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install ffmpeg
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire folder and run the application:
COPY . .
CMD ["python3", "bot.py"]
