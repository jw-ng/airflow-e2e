import tempfile
from pathlib import Path
from unittest.mock import MagicMock, call

from airflow_e2e.composer import composer


def test_should_create_docker_base_folder():
    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        expected_docker_folder_path = Path(temp_dir) / "docker"

        assert expected_docker_folder_path.exists()


def test_setup_should_setup_airflow_core_services(mocker):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.composer.composer.AirflowCoreServicesComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        assert spy_composer.call_count == 1
        assert spy_composer.call_args == call(dags="some/dags/folder")

        assert mock_composer_instance.setup.call_count == 1
        assert mock_composer_instance.setup.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )


def test_setup_without_requirements_should_setup_airflow_core_services_without_mounting_requirements_txt(
    mocker,
):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.composer.composer.AirflowCoreServicesComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup_without_requirements(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        assert spy_composer.call_count == 1
        assert spy_composer.call_args == call(dags="some/dags/folder")

        assert mock_composer_instance.setup_without_mount.call_count == 1
        assert mock_composer_instance.setup_without_mount.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )


def test_setup_should_setup_e2e_test_runner_service(mocker):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.composer.composer.E2eTestRunnerServiceComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        assert spy_composer.call_count == 1
        assert spy_composer.call_args == call(
            dags="some/dags/folder",
            tests="some/tests/folder",
        )

        assert mock_composer_instance.setup.call_count == 1
        assert mock_composer_instance.setup.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )


def test_setup_without_requirements_should_setup_e2e_test_runner_service(mocker):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.composer.composer.E2eTestRunnerServiceComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup_without_requirements(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        assert spy_composer.call_count == 1
        assert spy_composer.call_args == call(
            dags="some/dags/folder",
            tests="some/tests/folder",
        )

        assert mock_composer_instance.setup.call_count == 1
        assert mock_composer_instance.setup.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )


def test_setup_should_setup_airflow_seeder_service_composer(mocker):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.composer.composer.AirflowSeederServiceComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        assert spy_composer.call_count == 1
        assert spy_composer.call_args == call()

        assert mock_composer_instance.setup.call_count == 1
        assert mock_composer_instance.setup.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )


def test_setup_without_requirements_should_setup_airflow_seeder_service_composer(
    mocker,
):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.composer.composer.AirflowSeederServiceComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup_without_requirements(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        assert spy_composer.call_count == 1
        assert spy_composer.call_args == call()

        assert mock_composer_instance.setup.call_count == 1
        assert mock_composer_instance.setup.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )


def test_setup_should_setup_manual_e2e_test_runner_service_composer(mocker):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.composer.composer.ManualE2eTestRunnerServiceComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        assert spy_composer.call_count == 1
        assert spy_composer.call_args == call()

        assert mock_composer_instance.setup.call_count == 1
        assert mock_composer_instance.setup.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )


def test_setup_without_requirements_should_setup_manual_e2e_test_runner_service_composer(
    mocker,
):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.composer.composer.ManualE2eTestRunnerServiceComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup_without_requirements(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        assert spy_composer.call_count == 1
        assert spy_composer.call_args == call()

        assert mock_composer_instance.setup.call_count == 1
        assert mock_composer_instance.setup.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )


def test_setup_should_setup_envrc_file_writer(mocker):
    mocker_writer_instance = MagicMock()
    spy_writer = mocker.patch(
        "airflow_e2e.composer.composer.EnvrcFileWriter",
        return_value=mocker_writer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        assert spy_writer.call_count == 1
        assert spy_writer.call_args == call()

        assert mocker_writer_instance.setup.call_count == 1
        assert mocker_writer_instance.setup.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )


def test_setup_without_requirements_should_setup_envrc_file_writer(mocker):
    mocker_writer_instance = MagicMock()
    spy_writer = mocker.patch(
        "airflow_e2e.composer.composer.EnvrcFileWriter",
        return_value=mocker_writer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup_without_requirements(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        assert spy_writer.call_count == 1
        assert spy_writer.call_args == call()

        assert mocker_writer_instance.setup.call_count == 1
        assert mocker_writer_instance.setup.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )
