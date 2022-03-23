from airflow_e2e.builder.builder import (
    build_airflow_core_services_composer,
    build_e2e_test_runner_service_composer,
    build_extra_services_composer,
)
from airflow_e2e.composer.docker_compose_file.docker_compose_tests_yaml_file import (
    DockerComposeTestsYamlFile,
)
from airflow_e2e.composer.docker_compose_file.docker_compose_yaml_file import (
    DockerComposeYamlFile,
)


def test_build_airflow_core_services_composer_should_return_airflow_core_services_composer_without_custom_installation_when_with_custom_airflow_packages_is_false():
    composer = build_airflow_core_services_composer(
        dags="some/dags/folder", with_custom_airflow_packages=False
    )

    assert (
        composer.yaml_file.data
        == DockerComposeYamlFile(dags_folder="some/dags/folder").data
    )


def test_build_airflow_core_services_composer_should_return_airflow_core_services_composer_with_custom_installation_when_with_custom_airflow_packages_is_true():
    composer = build_airflow_core_services_composer(
        dags="some/dags/folder", with_custom_airflow_packages=True
    )

    assert (
        composer.yaml_file.data
        == DockerComposeYamlFile(dags_folder="some/dags/folder")
        .with_custom_airflow_packages()
        .data
    )


def test_build_e2e_test_runner_service_composer_should_return_e2e_test_runner_service_composer_without_custom_installation_when_with_custom_test_packages_is_false():
    composer = build_e2e_test_runner_service_composer(
        dags="some/dags/folder",
        tests="some/tests/folder",
        with_custom_test_packages=False,
    )

    assert (
        composer.yaml_file.data
        == DockerComposeTestsYamlFile(
            dags_folder="some/dags/folder",
            tests_folder="some/tests/folder",
        ).data
    )


def test_build_e2e_test_runner_service_composer_should_return_e2e_test_runner_service_composer_with_custom_installation_when_with_custom_test_packages_is_true():
    composer = build_e2e_test_runner_service_composer(
        dags="some/dags/folder",
        tests="some/tests/folder",
        with_custom_test_packages=True,
    )

    assert (
        composer.yaml_file.data
        == DockerComposeTestsYamlFile(
            dags_folder="some/dags/folder",
            tests_folder="some/tests/folder",
        )
        .with_custom_test_packages()
        .data
    )


def test_build_extra_services_composer_should_return_extra_services_composer_without_mongo_when_with_mongo_is_false():
    composer = build_extra_services_composer(with_mongo=False)

    assert composer.yaml_file.data.get("services") is None


def test_build_extra_services_composer_should_return_extra_services_composer_with_mongo_when_with_mongo_is_true():
    composer = build_extra_services_composer(with_mongo=True)

    assert composer.yaml_file.data.get("services").get("mongodb") is not None
