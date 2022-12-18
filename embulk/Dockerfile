FROM openjdk:8-slim as builder
SHELL ["/bin/bash", "-c"]
WORKDIR /app

RUN apt-get update && apt-get install -y curl

# Install Embulk
RUN curl --create-dirs -o /bin/embulk -L "https://dl.embulk.org/embulk-latest.jar" && \
  chmod +x /bin/embulk

# Install plugins
RUN curl --create-dirs -o /tmp/postgresql-42.4.2.jar "https://jdbc.postgresql.org/download/postgresql-42.4.2.jar"
RUN embulk gem install embulk-output-postgresql embulk-filter-column

# Install Python and Poetry
RUN apt-get install -y python3.9 python3-pip python3-venv
RUN pip install pipx
RUN pipx install poetry

# Setup server
COPY . .
RUN /root/.local/bin/poetry install

CMD ["/root/.local/bin/poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
