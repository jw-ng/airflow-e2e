from airflow_e2e.composer.seeder_file.variables_json_file import VariablesJsonFile


class TestVariablesJsonFile:
    def test_should_return_correct_examples(self):
        json_file = VariablesJsonFile()

        assert json_file.data == {
            "example_string_variable": "example_string_value",
            "example_json_variable": {"foo": "bar", "baz": 42},
            "example_array_variable": ["lorem", "ipsum"],
        }
