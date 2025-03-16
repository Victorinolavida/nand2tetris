ifndef VERBOSE
	MAKEFLAGS += --no-print-directory
endif

## help: print this help message
.PHONY: help
help:
	@echo "Usage:"
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'

## test: run tests for the project
.PHONY: test
test:
	@echo "Running tests..."
	@go clean -testcache
	@go test -v ./...
