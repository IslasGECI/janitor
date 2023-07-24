import os
import typer
import geci_janitor as jn

janitor = typer.Typer(help="Tools to clean k9 data for the eradication Guadalupe Island project")


@janitor.command()
def transform_xlsx(options: str):
    """
    Transform data `IG_ESFUERZO_K9_{date}.xls[x]` \n
    """
    command = f"docker run --entrypoint clean_k9_data --volume $PWD:/workdir islasgeci/clean_k9_data {options}"
    os.system(command)


@janitor.command(help="Clean and check IG_POSICION_TRAMPAS and IG_MORFOMETRIA")
def transform_cat_data():
    command = "docker run --rm --volume $PWD:/data islasgeci/diferencias_morfometria_posicion_trampas:latest ./src/verify_data.sh /data"
    os.system(command)


@janitor.command(help="Generate tidy and weekly effort tables for socorro monthly cat data")
def clean_socorro_week_data(week: int, data_file: str):
    command = f"docker run -v $PWD/results:/workdir/results -v $PWD:/workdir/data islasgeci/datatools python src/get_weekly_summary_socorro_from_excell.py {week} data/{data_file}"
    os.system(command)
    command = f"docker run -v $PWD/results:/workdir/results -v $PWD:/workdir/data islasgeci/diferencias_morfometria_posicion_trampas src/make_table_tidy.R --data results/socorro_cleaned_format.csv --salida results/tidy_{week}.csv"
    os.system(command)


@janitor.command()
def version():
    version = jn.__version__
    print(version)
