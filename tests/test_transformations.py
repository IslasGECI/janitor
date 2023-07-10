from janitor import janitor

from typer.testing import CliRunner

runner = CliRunner()


def test_app():
    result = runner.invoke(
        janitor,
        ["transform-cat-data", "--help"],
    )
    assert result.exit_code == 0
