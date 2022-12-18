FROM python:3.10.9

WORKDIR /app

RUN pip install --upgrade pip && pip install pipx && pipx ensurepath
RUN pipx install poetry

# Setup server
COPY . .
RUN /root/.local/bin/poetry install

CMD ["/root/.local/bin/poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
