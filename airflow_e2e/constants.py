CONVENIENT_MAKE_COMMANDS = (
    "For your convenience, you can copy the following make commands into your\n"
    "Makefile (or create one if it does not yet exist):\n"
    "\n"
    "clean:\n"
    "\tsource ./docker/.envrc && \\\n"
    "\tdocker-compose \\\n"
    "\t-f ./docker/docker-compose.yml \\\n"
    "\t-f ./docker/docker-compose-dev.yml \\\n"
    "\t-f ./docker/docker-compose-tests.yml \\\n"
    "\tdown --remove-orphans --volumes\n"
    "\n"
    "dev: clean\n"
    "\tsource ./docker/.envrc && \\\n"
    "\tdocker-compose \\\n"
    "\t-f ./docker/docker-compose.yml \\\n"
    "\t-f ./docker/docker-compose-dev.yml \\\n"
    "\tup -d\n"
    "\n"
    "wait_for_airflow_web_to_be_healthy:\n"
    "\tuntil [ $$(docker inspect -f '{{.State.Health.Status}}' airflow-web) = 'healthy' ] ; do \\\n"
    "\t\tsleep 1 ; \\\n"
    "\tdone\n"
    "\n"
    "seeded_dev: dev wait_for_airflow_web_to_be_healthy\n"
    "\tdocker exec airflow-scheduler sh -c \\\n"
    "\t'airflow connections import /tmp/seed/connections.yaml && airflow variables import /tmp/seed/variables.json'\n"
    "\n"
    "e2e:\n"
    "\tsource ./docker/.envrc && \\\n"
    "\tdocker-compose \\\n"
    "\t-f ./docker/docker-compose.yml \\\n"
    "\t-f ./docker/docker-compose-tests.yml \\\n"
    "\tup --exit-code-from test-runner\n"
)

BASIC_USAGE_INSTRUCTIONS = (
    "An `.envrc` file is generated in the `docker/` folder as well. Replace the values\n"
    "of the fields with the placeholder `<SECRET_STRING_TO_BE_FILLED_IN>` with actual\n"
    "values of your choice. Please remember to add the following to your source code\n"
    "versioning tool ignore file\n"
    "\n"
    "To run the Airflow E2E test scripts, run:\n"
    "\n"
    "\tmake e2e\n"
)
