FROM apache/superset:latest

USER root

RUN chmod +x /app/docker/docker-bootstrap.sh

# Start Superset
USER superset
CMD ["bash", "docker-bootstrap.sh", "app"]
