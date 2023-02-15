from os.path \
    import \
    realpath, \
    dirname

import pathlib

source_path = None
repository_path = None

def get_repository_path() -> str:
    global repository_path
    return repository_path


def set_repository_path(
        value: str
):
    global repository_path
    repository_path = value


def get_source_path() -> str:
    global source_path
    return source_path


def set_source_path(
        value: str
):
    global source_path
    source_path = value


def get_script_location(
        script: str
) -> str:
    script_path = dirname(
        realpath(
            script
        )
    )

    return script_path


def setup(
        workspace: str
):
    set_source_path(
        get_script_location(
            workspace
        )
    )

    find_repository = pathlib.Path(
        get_source_path()
    ).parent.absolute()

    set_repository_path(
        str(find_repository)
    )

    debug()


def debug():
    print(
        "source directory: ",
        get_source_path()
    )

    print(
        "repository directory:",
        get_repository_path()
    )
