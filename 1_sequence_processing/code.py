from typing import List, Union
import numpy.typing as npt
import numpy as np

def base_count(fastafile: str) -> List[int]:
    # 課題 1-1
    base_counts = [0, 0, 0, 0]
    with open(fastafile, 'r') as file:
        for line in file:
            if line.startswith('>'):
                continue
            base_counts[0] += line.count('A')
            base_counts[1] += line.count('T')
            base_counts[2] += line.count('G')
            base_counts[3] += line.count('C')

    return base_counts # A, T, G, C

def gen_rev_comp_seq(fastafile: str) -> str:
    # 課題 1-2
    rev_comp = []
    with open(fastafile, 'r') as file:
        for line in file:
            if line.startswith('>'):
                continue
            for base in line:
                if base == 'A':
                    rev_comp.insert(0, 'T')
                if base == 'T':
                    rev_comp.insert(0, 'A')
                if base == 'G':
                    rev_comp.insert(0, 'C')
                if base == 'C':
                    rev_comp.insert(0, 'G')

    return "".join(rev_comp)

def calc_gc_content(fastafile: str, window: int=1000, step: int=300) -> Union[npt.NDArray[np.float_], List[float]]:
    # 課題 1-3
    # 値を出力するところまで。matplotlibを使う部分は別途実装してください。
    sequence = ""
    with open(fastafile, 'r') as file:
        for line in file:
            if line.startswith('>'):
                continue
            sequence += line.strip().upper()

    gc_contents = []
    for i in range(0, len(sequence) - window + 1, step):
        window_seq = sequence[i:i + window]
        gc_count = window_seq.count('G') + window_seq.count('C')
        gc_content = (gc_count / window) * 100
        gc_contents.append(gc_content)

    return np.array(gc_contents)

def search_motif(fastafile: str, motif: str) -> List[str]:
    # 課題 1-4
    return []

def translate(fastafile: str) -> List[str]:
    # 課題 1-5
    return []

if __name__ == "__main__":
    filepath = "data/NT_113952.1.fasta"
    # 課題 1-1
    print(base_count(filepath))
    # 課題 1-2
    print(gen_rev_comp_seq(filepath))
    # 課題 1-3
    print(calc_gc_content(filepath))
    # 課題 1-4
    print(search_motif(filepath, "ATG"))
    # 課題 1-5
    print(translate(filepath))
