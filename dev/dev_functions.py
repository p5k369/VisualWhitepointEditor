"""Development functions."""
from __future__ import annotations

from pathlib import Path
from typing import List

from PyQt6 import uic


def compile_ui_files(src_folders: List[Path]) -> None:
    """
    Compile the ui files.

    Compile the ui files in src_folders and copy the created
    files to gen folder.
    """
    for folder in src_folders:
        for file in folder.iterdir():
            print(f"Converting file {file}")
            with file.open("r", encoding="utf-8") as source:
                new_file = file.parent.parent / "gen" / f"ui_{file.stem}.py"
                with new_file.open(
                    "w",
                    encoding="utf-8",
                ) as target:
                    uic.compileUi(source, target)
    print("Conversion finished")


