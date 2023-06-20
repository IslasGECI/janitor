import docker
import typer

janitor = typer.Typer(
    help="Tools to clean k9 data for the eradication Guadalupe Island project")


@janitor.command()
def transform_xlsx(command: str):
    """
    Transform data `IG_ESFUERZO_K9_{date}.xls[x]` \n
    """
    client = docker.from_env()
    image = client.images.pull("islasgeci/clean_k9_data")
    client.containers.run(
        "islasgeci/clean_k9_data",
        volumes={"$PWD": {"bind": "/workdir", "mode": "rw"}},
        command=f"clean_k9_data {command}",
        remove=True,
    )


@janitor.command()
def version():
    print("0.1.0")
