import os
from pathlib import Path

folderPath = Path("C:/Users/User/Downloads")

files = os.listdir(folderPath)

our_suffixes: list[str] = [".sb3", ".mp3", ".htm", ".exe", ".msix"]

# print(files)

for file in files:
    suffix = Path(file).suffix
    if suffix in our_suffixes:
        destination_folder = folderPath / suffix.removeprefix(".")
        destination_folder.mkdir(exist_ok=True)
        
        source = folderPath / file
        destination = destination_folder / file
        
        source.rename(destination)
        print(f"Moved: {file} -> {destination_folder}")
    # print(suffix)
