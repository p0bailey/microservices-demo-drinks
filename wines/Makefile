#Authored by Phillip Bailey
.PHONY: all build
.SILENT:

APP = wine

PORT = 5000

all:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build:  ## build Docker image
	docker rm -f $(APP)-app | true && \
	docker build --tag $(APP)-app . && \
	docker run --name $(APP)-app -p $(PORT):$(PORT) $(APP)-app
