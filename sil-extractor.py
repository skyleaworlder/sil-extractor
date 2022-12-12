import sys
from typing import List

sil_types = []
exclude_chars = ["(", "%", "#", "{", "}", "@", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def main(argv: List[str]):
    sil_file_path = argv[0]
    output_path = argv[1]
    with open(sil_file_path, "r") as f:
        lines = f.readlines()
        lines = [line.strip().strip("\n") for line in lines if len(line) != 0]
        process_sil_lines(lines)
    with open(output_path, "w") as f:
        tmp = [f"{idx} {sil_type}\n" for idx, sil_type in enumerate(sil_types)]
        f.writelines(tmp)


def process_sil_lines(lines: List[str]):
    for line in lines:
        process_sil_line(line)


def process_sil_line(line: str):
    sil_fragments = line.split(" ")
    head = sil_fragments[0]
    if len(head) == 0:
        return
    if check_head(head):
        if head not in sil_types:
            sil_types.append(head)
        return
    if head.startswith("%"):
        sil_type = sil_fragments[2]
        if sil_type not in sil_types:
            sil_types.append(sil_type)
        return


def check_head(head: str) -> bool:
    for char in exclude_chars:
        if char in head:
            return False
    else:
        return True


if __name__ == "__main__":
    main(sys.argv[1:])

