from pathlib import Path

from flit.common import VCSError
from . import hg
from . import git
from . import fsl

def identify_vcs(directory: Path):
    directory = directory.resolve()
    for p in [directory] + list(directory.parents):
        if (p / '.git').is_dir():
            return git
        if (p / '.hg').is_dir():
            return hg
        if ((p / '.fslckout').is_file()
            or (p / '_FOSSIL_').is_file()):
            return fsl

    raise VCSError("Directory does not appear to be in a VCS", directory)
