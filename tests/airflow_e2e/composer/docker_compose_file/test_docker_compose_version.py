from airflow_e2e.composer.docker_compose_file.docker_compose_version import DOCKER_COMPOSE_VERSION


def test_should_return_correct_version():
    assert DOCKER_COMPOSE_VERSION == {"version": "3.7"}
