from janitor import janitor
import os
from typer.testing import CliRunner

runner = CliRunner()


def test_app():
    result = runner.invoke(
        janitor,
        ["transform-cat-data", "--help"],
    )
    assert result.exit_code == 0
    expected_file_path = "tests/data/IG_POSICION_TRAMPAS_02JUL2023_clean.csv"
    if os.path.exists(expected_file_path):
        os.remove(expected_file_path)

    folder_with_data_path = "tests/data"
    os.chdir(folder_with_data_path)
    result = runner.invoke(
        janitor,
        ["transform-cat-data"],
    )
    os.chdir("/workdir")
    assert os.path.exists(expected_file_path)
