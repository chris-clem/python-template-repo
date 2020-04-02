from click.testing import CliRunner

from {{cookiecutter.package_name}}.{{cookiecutter.script_name}} import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
