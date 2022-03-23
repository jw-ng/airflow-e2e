from airflow_e2e.composer.airflow_core_services_composer import (
    AirflowCoreServicesComposer,
)


def build_airflow_core_services_composer(
    dags: str, with_custom_airflow_packages: bool
) -> AirflowCoreServicesComposer:
    airflow_core_services_composer = AirflowCoreServicesComposer(dags=dags)

    return (
        airflow_core_services_composer.with_custom_airflow_installation()
        if with_custom_airflow_packages
        else airflow_core_services_composer
    )
