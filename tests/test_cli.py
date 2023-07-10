from janitor import janitor
from typer.testing import CliRunner

runner = CliRunner()


def test_app():
    result = runner.invoke(
        janitor,
        ["transform-cat-data", "--help"],
    )
    assert result.exit_code == 0

    result = runner.invoke(
        janitor,
        ["--help"],
    )
    assert "XX" not in result.stdout
