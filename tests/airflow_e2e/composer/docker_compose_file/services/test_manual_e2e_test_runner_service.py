from airflow_e2e.composer.docker_compose_file.services.manual_e2e_test_runner_service import (
    ManualE2eTestRunnerService,
)


class TestManualE2eTestRunnerService:
    def test_should_return_correct_e2e_test_runner_service_settings(self):
        assert ManualE2eTestRunnerService().data == {
            "command": 'bash -c "bash /src/scripts/wait_for_airflow_web.sh '
            '&& tail -f /dev/null"'
        }
