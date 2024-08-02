import os
import warnings
from itertools import chain
from pathlib import Path
from auxiliary.turbopath import turbopath


def search_path(basepath: str | Path, query: str, verbose: bool = False, suppress: bool = False) -> list[Path]:
    """Searches from basepath with query
    Args:
        basepath: ground path to look into
        query: search query, can contain wildcards like *.npz or **/*.npz
        verbose:
        suppress: if true, will not throwing warnings if nothing is found

    Returns:
        All found paths
    """
    basepath = str(basepath)
    assert os.path.exists(basepath), f"basepath for search_path() doesnt exist, got {basepath}"
    if not basepath.endswith("/"):
        basepath += "/"
    print(f"search_path: in {basepath}{query}") if verbose else None
    paths = sorted(list(chain(list(Path(f"{basepath}").glob(f"{query}")))))
    if len(paths) == 0 and not suppress:
        warnings.warn(f"did not find any paths in {basepath}{query}", UserWarning)
    return paths


# Find config path
def config_by_name(name: str) -> Path:
    directory = turbopath(__file__).parent.parent
    if not name.endswith(".yaml"):
        name += ".yaml"
    p = search_path(directory, query=f"**/{name}", suppress=True)
    assert len(p) == 1, f"Did not find exactly one config yaml with name {name} in directory {directory}, got {p}"
    return p[0]
