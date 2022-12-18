# connpass-analytics

## Requirements

- Docker
- docker-compose

## Setup

```bash
# Create keywords.conf from sample
cp digdag/project/keywords.conf{.sample,}

# Build and start docker contianers
docker-compose build
docker-compose up -d

# Create digdag project
docker-compose exec digdag bash
digdag push connpass-analytics --project project/  # in docker container
```
