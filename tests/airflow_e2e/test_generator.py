import tempfile
from pathlib import Path

from airflow_e2e.generator import generate


def test_should_create_docker_base_folder():
    with tempfile.TemporaryDirectory() as temp_dir:
        generate(
            dags="some/dags/folder",
            working_dir=temp_dir,
        )

        expected_docker_folder_path = Path(temp_dir) / "docker"

        assert expected_docker_folder_path.exists()


def test_should_create_docker_compose_yml_file_in_docker_base_folder():
    with tempfile.TemporaryDirectory() as temp_dir:
        generate(
            dags="some/dags/folder",
            working_dir=temp_dir,
        )

        docker_compose_yml_file_path = Path(temp_dir) / "docker" / "docker-compose.yml"

        assert docker_compose_yml_file_path.exists()


def test_should_setup_correct_dags_folder_in_docker_compose_yml_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        generate(
            dags="some/dags/folder",
            working_dir=temp_dir,
        )

        docker_compose_yml_file_path = Path(temp_dir) / "docker" / "docker-compose.yml"

        with docker_compose_yml_file_path.open() as f:
            actual = f.read()

        expected_docker_compose_yml_file_path = Path(__file__).resolve().parent / "resources" / "expected_docker_compose.yml"
        with expected_docker_compose_yml_file_path.open() as f:
            expected = f.read()

        assert actual == expected
