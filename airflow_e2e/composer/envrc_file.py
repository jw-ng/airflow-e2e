import textwrap


class EnvrcFile:
    @property
    def content(self) -> str:
        return textwrap.dedent("""\
            export AIRFLOW_EMAIL=user@example.com
            export AIRFLOW_USERNAME=user
            export AIRFLOW_PASSWORD=<SECRET_STRING_TO_BE_FILLED_IN>
            export AIRFLOW_DATABASE_NAME=bitnami_airflow
            export AIRFLOW_DATABASE_USERNAME=bn_airflow
            export AIRFLOW_DATABASE_PASSWORD=<SECRET_STRING_TO_BE_FILLED_IN>
            export AIRFLOW_FERNET_KEY=<SECRET_STRING_TO_BE_FILLED_IN>
            export AIRFLOW_SECRET_KEY=<SECRET_STRING_TO_BE_FILLED_IN>
        """)
