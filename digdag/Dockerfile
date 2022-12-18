FROM openjdk:8-slim
SHELL ["/bin/bash", "-c"]
WORKDIR /app

RUN apt-get update && apt-get install -y curl

# Install Digdag
RUN curl --create-dirs -o /bin/digdag -L "https://dl.digdag.io/digdag-latest" && \
  chmod +x /bin/digdag

COPY . .

# CMD digdag scheduler --project project -o ./db -O ./logs -b 0.0.0.0
# CMD digdag scheduler --project project -c scheduler.conf -b 0.0.0.0
CMD digdag server -c postgresql.conf -b 0.0.0.0
