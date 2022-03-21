# airflow-e2e

This packages aims to set up the scripts to run Airflow DAGs E2E tests.

## Installation

```shell
pip install airflow-e2e
```

## Usage

### Pre-requisites

Before generating and running the E2E test scripts, the following files are required to
be present in your repository:

1. A `requirements.txt` file at the root of your repository, which contains all
   Python packages required by your Airflow scheduler and workers to perform the
   tasks under tests
2. A `requirements-dev.txt` file at the root of your repository, which contains
   all the Python pacakges required by the test runner to run you E2E test 
   suite(s)
3. A folder that contains the Airflow DAGs under test
4. A folder that contains the E2E test suite(s)

### Generating the test scripts

To generate the Airflow E2E test scripts, run the following command at the root
of your repository:

```shell
airflow-e2e --dags dags/ --tests tests/e2e
```

This will generate a `docker` folder at the root of your repository, and it will
contain the following files:

```
<root_of_repository>
 |- docker/
     |- airflow_connections_and_variables_seeder/
     |   |- connections.yml
     |   |- variables.json
     |- .envrc
     |- docker-compose.yml
     |- docker-compose-dev.yml
     |- docker-compose-manual-testing.yml
     |- docker-compose-tests.yml
```

In addition, for your convenience, the following `make` commands are printed on
the console, should you be interested to use them:

```makefile
clean:
	source ./docker/.envrc && \
	docker-compose \
	-f ./docker/docker-compose.yml \
	-f ./docker/docker-compose-dev.yml \
	-f ./docker/docker-compose-tests.yml \
	down --remove-orphans --volumes

dev: clean
	source ./docker/.envrc && \
	docker-compose \
	-f ./docker/docker-compose.yml \
	-f ./docker/docker-compose-dev.yml \
	up -d

wait_for_airflow_web_to_be_healthy:
	until [ $$(docker inspect -f '{{.State.Health.Status}}' airflow-web) = "healthy" ] ; do \
		sleep 1 ; \
	done

seeded_dev: dev wait_for_airflow_web_to_be_healthy
	docker exec airflow-scheduler sh -c \
	"airflow connections import /tmp/seed/connections.yaml && airflow variables import /tmp/seed/variables.json"

e2e:
	source ./docker/.envrc && \
	docker-compose \
	-f ./docker/docker-compose.yml \
	-f ./docker/docker-compose-tests.yml \
	up --exit-code-from test-runner
```

### Setting up the E2E tests

A `.envrc` file is generated in the `docker/` folder as well. Replace the values of
the fields with the placeholder `<SECRET_STRING_TO_BE_FILLED_IN>` with actual values
of your choice. Please remember to add the following to your source code versioning
tool ignore file (`.gitignore` for Git, for example):

```
.envrc*
```

Even though we may be using dummy credentials for our tests, we should still be
vigilant when it comes to committing secrets.

### Running the E2E tests

To run the E2E tests, you can run the following command:

```shell
source ./docker/.envrc && \
  docker-compose \
  -f ./docker/docker-compose.yml \
  -f ./docker/docker-compose-tests.yml \
  up --exit-code-from test-runner
```

Or, if you have copied the convenient `make` command from before, you can run:

```shell
make e2e
```

## License

GNU GENERAL PUBLIC LICENSE v3

## Testing

To run the tests, run the following command at the root of the repository:

```shell
make test
```

## Changelog

Refer to [CHANGELOG.md](https://github.com/jw-ng/airflow-e2e/blob/main/CHANGELOG.md)
