.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make help: Show this help message"
	@echo "  make docker-up: Start the application in a docker container"

.PHONY: docker-up
docker-up:
	docker compose -f docker-compose.dev.yaml up --build