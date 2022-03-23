from airflow_e2e.composer.airflow_core_services_composer import (
    AirflowCoreServicesComposer,
)
from airflow_e2e.composer.e2e_test_runner_service_composer import E2eTestRunnerServiceComposer


def build_airflow_core_services_composer(
    dags: str, with_custom_airflow_packages: bool
) -> AirflowCoreServicesComposer:
    airflow_core_services_composer = AirflowCoreServicesComposer(dags=dags)

    return (
        airflow_core_services_composer.with_custom_airflow_installation()
        if with_custom_airflow_packages
        else airflow_core_services_composer
    )


def build_e2e_test_runner_service_composer(
    dags: str, tests: str,  with_custom_test_packages: bool
):
    e2e_test_runner_service_composer = E2eTestRunnerServiceComposer(
        dags=dags, tests=tests
    )

    return (
        e2e_test_runner_service_composer.with_custom_test_packages()
        if with_custom_test_packages
        else e2e_test_runner_service_composer
    )
