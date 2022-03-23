import typing

from airflow_e2e.composer.docker_compose_file.services.base_service import BaseService


class ManualE2eTestRunnerService(BaseService):
    @property
    def data(self) -> typing.Dict:
        return {
            "command": 'bash -c "bash /src/scripts/wait_for_airflow_web.sh '
            '&& tail -f /dev/null"'
        }
