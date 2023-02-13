from os.path \
    import \
    realpath, \
    dirname

source_path = None


def get_source_path() -> str:
    global source_path
    return source_path


def set_source_path( value: str ):
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

    print(
        "source directory: ",
        get_source_path()
    )
