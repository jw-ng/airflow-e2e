import typing
from pathlib import Path
from string import Template


def copy_from_template(
    template_file_path: Path,
    output_file_path: Path,
    substitutions: typing.Dict[str, str] = None,
):
    with template_file_path.open(mode="r") as template_file:
        template = Template(template_file.read())

    substitutions = substitutions or {}
    with output_file_path.open("w") as docker_compose_yml_file:
        content = template.substitute(**substitutions)
        docker_compose_yml_file.write(content)
