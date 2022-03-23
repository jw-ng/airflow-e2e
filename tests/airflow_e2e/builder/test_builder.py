from pathlib import Path

from airflow_e2e.builder.builder import build_airflow_core_services_composer
from airflow_e2e.composer.constants import TEMPLATES_DIR_PATH


def test_build_airflow_core_services_composer_should_return_airflow_core_services_composer_without_custom_mount_when_with_custom_airflow_installation_is_false():
    composer = build_airflow_core_services_composer(
        dags="some/dags/folder", with_custom_airflow_installation=False
    )

    assert (
        composer.template_file_path
        == Path(TEMPLATES_DIR_PATH) / "docker-compose.yml.template"
    )


def test_build_airflow_core_services_composer_should_return_airflow_core_services_composer_with_custom_airflow_installation_when_with_custom_mount_is_true():
    composer = build_airflow_core_services_composer(
        dags="some/dags/folder", with_custom_airflow_installation=True
    )

    assert (
        composer.template_file_path
        == Path(TEMPLATES_DIR_PATH) / "docker-compose.yml_without_requirements.template"
    )
