from geci_janitor import janitor
from typer.testing import CliRunner

runner = CliRunner()


def test_app():
    result = runner.invoke(
        janitor,
        ["transform-cat-data", "--help"],
    )
    assert result.exit_code == 0
    assert "--positions-path" in result.stdout
    assert "--morphometry-path" in result.stdout

    result = runner.invoke(
        janitor,
        ["clean-socorro-position", "--help"],
    )
    assert result.exit_code == 0

    result = runner.invoke(
        janitor,
        ["socorro-morphometry", "--help"],
    )
    assert result.exit_code == 0

    result = runner.invoke(
        janitor,
        ["extract-weeks-from-xlsx", "--help"],
    )
    assert result.exit_code == 0

    result = runner.invoke(
        janitor,
        ["change-date-format-to-iso", "--help"],
    )
    assert result.exit_code == 0

    result = runner.invoke(
        janitor,
        ["--help"],
    )
    assert "XX" not in result.stdout


def test_version():
    result = runner.invoke(
        janitor,
        ["version"],
    )
    expected_version = "0.13.0"
    assert expected_version in result.stdout
