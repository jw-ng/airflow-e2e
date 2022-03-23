import typing

from airflow_e2e.composer.docker_compose_file.services.base_service import BaseService


class E2eTestRunnerService(BaseService):
    def __init__(self, dags_folder: str, tests_folder: str):
        self._volumes = [
            f"../{dags_folder}:/src/dags",
            f"../{tests_folder}:/src/tests",
            "./scripts:/src/scripts",
        ]

    @property
    def data(self) -> typing.Dict:
        return {
            **{
                "container_name": "test-runner",
                "image": "bitnami/airflow-scheduler:latest",
                "depends_on": ["aiflow-web"],
                "working_dir": "/src",
                "environment": [
                    "PYTHONPATH=/src",
                    "AIRFLOW_ADMIN_USERNAME=${AIRFLOW_USERNAME}",
                    "AIRFLOW_ADMIN_PASSWORD=${AIRFLOW_PASSWORD}",
                    "AIRFLOW_DATABASE_HOST=airflow-postgresql",
                    "AIRFLOW_DATABASE_NAME=${AIRFLOW_DATABASE_NAME}",
                    "AIRFLOW_DATABASE_USERNAME=${AIRFLOW_DATABASE_USERNAME}",
                    "AIRFLOW_DATABASE_PASSWORD=${AIRFLOW_DATABASE_PASSWORD}",
                    "AIRFLOW_FERNET_KEY=${AIRFLOW_FERNET_KEY}",
                    "AIRFLOW_LOAD_EXAMPLES=no",
                    "AIRFLOW_SECRET_KEY=${AIRFLOW_SECRET_KEY}",
                    "AIRFLOW_WEBSERVER_HOST=airflow-web",
                    "AIRFLOW__CORE__LOAD_DEFAULT_CONNECTIONS=False",
                ],
                "command": 'bash -c "bash /src/scripts/wait_for_airflow_web.sh '
                '&& pytest -vvv -s --log-cli-level=DEBUG /src/tests/integration"',
            },
            **{"volumes": self._volumes},
        }

    def with_custom_test_packages(self) -> "E2eTestRunnerService":
        self._volumes += ["../requirements-dev.txt:/bitnami/python/requirements.txt"]

        return self
