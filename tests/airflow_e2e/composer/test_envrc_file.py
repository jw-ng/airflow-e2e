from airflow_e2e.composer.envrc_file import EnvrcFile


class TestEnvrcFile:
    def test_data_should_return_correctly(self):
        assert EnvrcFile().content == (
            "export AIRFLOW_EMAIL=user@example.com\n"
            "export AIRFLOW_USERNAME=user\n"
            "export AIRFLOW_PASSWORD=<SECRET_STRING_TO_BE_FILLED_IN>\n"
            "export AIRFLOW_DATABASE_NAME=bitnami_airflow\n"
            "export AIRFLOW_DATABASE_USERNAME=bn_airflow\n"
            "export AIRFLOW_DATABASE_PASSWORD=<SECRET_STRING_TO_BE_FILLED_IN>\n"
            "export AIRFLOW_FERNET_KEY=<SECRET_STRING_TO_BE_FILLED_IN>\n"
            "export AIRFLOW_SECRET_KEY=<SECRET_STRING_TO_BE_FILLED_IN>\n"
        )
