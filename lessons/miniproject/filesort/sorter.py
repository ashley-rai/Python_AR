import os
from pathlib import Path

folderToSort = Path("C:/Users/User/Downloads")

filesInFolder = os.listdir(folderToSort)

# We sort based on these suffixes
suffixesToSort: list[str] = [".sb3", ".mp3", ".htm", ".exe", ".msix"]


def createFolderAndMoveFile(fileSuffix: str):
    destination_folder = folderToSort / fileSuffix.removeprefix(".")
    destination_folder.mkdir(exist_ok=True)

    source = folderToSort / file
    destination = destination_folder / file

    source.rename(destination)
    print(f"Moved: {file} -> {destination_folder}")


for file in filesInFolder:
    fileSuffix = Path(file).suffix

    if fileSuffix in suffixesToSort:
        createFolderAndMoveFile(fileSuffix)
    # print(suffix)
