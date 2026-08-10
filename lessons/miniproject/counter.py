import os
from pathlib import Path
from collections import Counter

folderPath = "C:/Users/User/Downloads"

files = os.listdir(folderPath)

suffixes_sorted: list[str] = []

# print(files)

for file in files:
    suffix = Path(file).suffix
    suffixes_sorted.append(suffix)
    # print(suffix)
suffixes_sorted.sort()

# unique_suffixes = set(suffixes_sorted)
# for suffix in unique_suffixes:
#     print(suffix)
# print(unique_suffixes)

suffix_counts = Counter(suffixes_sorted)
print(suffix_counts)

for s,c in sorted(suffix_counts.items()):
    print(s,c)

