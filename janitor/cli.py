import os
import typer
import janitor as jn

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


@janitor.command()
def version():
    version = jn.__version__
    print(version)
