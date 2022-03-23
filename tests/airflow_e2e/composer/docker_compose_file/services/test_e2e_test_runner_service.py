from airflow_e2e.composer.docker_compose_file.services.e2e_test_runner_service import E2eTestRunnerService


class TestE2eTestRunnerService:
    def test_should_return_correct_e2e_test_runner_service_settings(self):
        assert E2eTestRunnerService(
            dags_folder="some/dags/folder",
            tests_folder="some/tests/folder",
        ).data == {
            "container_name": "test-runner",
            "image": "bitnami/airflow-scheduler:latest",
            "depends_on": ["aiflow-web"],
            "working_dir": "/src",
            "volumes": [
                "../some/dags/folder:/src/dags",
                "../some/tests/folder:/src/tests",
                "./scripts:/src/scripts",
            ],
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
                       '&& pytest -vvv -s --log-cli-level=DEBUG /src/tests/integration"'
        }

    def test_should_return_e2e_test_runner_service_with_requirements_dev_txt_mount_when_with_custom_airflow_packages(
            self,
    ):
        service = E2eTestRunnerService(
            dags_folder="some/dags/folder",
            tests_folder="some/tests/folder",
        ).with_custom_test_packages()

        assert service.data == {
                   "container_name": "test-runner",
                   "image": "bitnami/airflow-scheduler:latest",
                   "depends_on": ["aiflow-web"],
                   "working_dir": "/src",
                   "volumes": [
                       "../some/dags/folder:/src/dags",
                       "../some/tests/folder:/src/tests",
                       "./scripts:/src/scripts",
                       "../requirements-dev.txt:/bitnami/python/requirements.txt",
                   ],
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
                              '&& pytest -vvv -s --log-cli-level=DEBUG /src/tests/integration"'
               }
