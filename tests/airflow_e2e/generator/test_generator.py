import tempfile
from pathlib import Path
from unittest.mock import MagicMock, call

from airflow_e2e.generator import generator


def test_should_create_docker_base_folder():
    with tempfile.TemporaryDirectory() as temp_dir:
        generator.generate(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        expected_docker_folder_path = Path(temp_dir) / "docker"

        assert expected_docker_folder_path.exists()


def test_should_create_docker_compose_manual_testing_yml_file_in_docker_base_folder():
    with tempfile.TemporaryDirectory() as temp_dir:
        generator.generate(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        docker_compose_manual_testing_yml_file_path = (
            Path(temp_dir) / "docker" / "docker-compose-manual-testing.yml"
        )

        assert docker_compose_manual_testing_yml_file_path.exists()


def test_should_create_envrc_file_in_docker_base_folder():
    with tempfile.TemporaryDirectory() as temp_dir:
        generator.generate(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        envrc_file_path = Path(temp_dir) / "docker" / ".envrc"

        assert envrc_file_path.exists()


def test_should_setup_correct_template_in_envrc_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        generator.generate(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
        )

        envrc_file_path = Path(temp_dir) / "docker" / ".envrc"

        with envrc_file_path.open() as f:
            actual = f.read()

        expected_envrc_file_path = (
            Path(__file__).resolve().parent.parent / "resources" / "expected_envrc"
        )
        with expected_envrc_file_path.open() as f:
            expected = f.read()

        assert actual == expected


def test_should_set_current_working_directory_as_default_working_directory_when_not_specified(
    mocker,
):
    with tempfile.TemporaryDirectory() as temp_dir:
        mocker.patch("airflow_e2e.generator.generator.os.getcwd", return_value=temp_dir)

        generator.generate(
            dags="some/dags/folder",
            tests="some/tests/folder",
        )

        docker_folder_path = Path(temp_dir) / "docker"

        assert docker_folder_path.exists()
        assert docker_folder_path.is_dir()


def test_generate_should_setup_airflow_core_services(mocker):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.generator.generator.AirflowCoreServicesComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        generator.generate(
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


def test_generate_without_requirements_should_setup_airflow_core_services_without_mounting_requirements_txt(
    mocker,
):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.generator.generator.AirflowCoreServicesComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        generator.generate_without_requirements(
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


def test_generate_should_setup_e2e_test_runner_service(mocker):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.generator.generator.E2eTestRunnerServiceComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        generator.generate(
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


def test_generate_without_requirements_should_setup_e2e_test_runner_service(mocker):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.generator.generator.E2eTestRunnerServiceComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        generator.generate_without_requirements(
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


def test_generate_should_setup_airflow_seeder_service_composer(mocker):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.generator.generator.AirflowSeederServiceComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        generator.generate(
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


def test_generate_without_requirements_should_setup_airflow_seeder_service_composer(
    mocker,
):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.generator.generator.AirflowSeederServiceComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        generator.generate_without_requirements(
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
