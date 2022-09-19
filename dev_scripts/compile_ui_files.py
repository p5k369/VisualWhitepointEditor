"""Convert every ui-file in src/ui to a py-file in src/gen."""
import os
from pathlib import Path

from dev.dev_functions import compile_ui_files

if __name__ == "__main__":
    os.chdir(Path(__file__).parent.parent)
    compile_ui_files([Path("src") / "ui"])
