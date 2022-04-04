#!/usr/bin/python3

"""
DNA molecules are made of two twisting, paired strands. Each strand is made of four chemical units,
called nucleotide bases. The bases are adenine (A), thymine (T), guanine (G) and cytosine (C).
The human genome contains approximately 3 billion of these base pairs, which reside in the 23 pairs of chromosomes
within the nucleus of all our cells.
There are many parts of the genome with contiguous repetitions of the same nucleotide, so they are good candidates
for compression.

Write a function that takes the DNA Strand  with the read of the Sequencer and encodes it replacing repeated
nucleotides with the number of repetitions followed by the repeated nucleotide. For example, given an input of
"TTTAGGTC" the program should output "3TA2GTC".
As another example, an input of ACTTTTTAGCCCCCCCGGGGTTTTTA should output AC5TAG7C4G5TA
"""


def compress(strand: str) -> str:
    """
    This function takes the DNA Strand  with the read of the sequencer and encodes it replacing repeated
    nucleotides with the number of repetitions followed by the repeated nucleotide. For example, given an input of
    "TTTAGGTC" the program should output "3TA2GTC".

    Args:
        strand (str): Full DNA sequence.

    Returns:
        str: Compressed DNA sequence.
    """
    result = []
    counter = 1
    current = strand[0]

    for i in range(1, len(strand) + 1):
        if i < len(strand):
            if strand[i] == current:
                counter += 1
                continue

        if counter == 1:
            result.append(current)
        else:
            result.append(str(counter))
            result.append(current)
            counter = 1

        if i < len(strand):
            current = strand[i]

    return ''.join(result)


def compress_prima(strand: str) -> str:
    """
    This function takes the DNA Strand  with the read of the sequencer and encodes it replacing repeated
    nucleotides with the number of repetitions followed by the repeated nucleotide. For example, given an input of
    "TTTAGGTC" the program should output "3TA2GTC".

    Args:
        strand (str): Full DNA sequence.

    Returns:
        str: Compressed DNA sequence.
    """

    result = []
    counter = 1

    for i in range(0, len(strand)):
        current = strand[i]
        if i < len(strand) - 1:
            j = i + 1

            if current == strand[j]:
                counter += 1
                continue

        if counter == 1:
            result.append(current)
        else:
            result.append(str(counter))
            result.append(current)
            counter = 1

    return ''.join(result)


def compress_generator(strand: str):
    """
    This function takes the DNA Strand  with the read of the sequencer and encodes it replacing repeated
    nucleotides with the number of repetitions followed by the repeated nucleotide. For example, given an input of
    "TTTAGGTC" the program should output "3TA2GTC".

    Args:
        strand (str): Full DNA sequence.

    Returns:
        Generator[str]: Compressed DNA sequence.
    """

    counter = 1

    for i in range(0, len(strand)):
        current = strand[i]
        if i < len(strand) - 1:
            j = i + 1

            if current == strand[j]:
                counter += 1
                continue

        if counter == 1:
            yield current
        else:
            yield str(counter) + current
            counter = 1


def main():
    strand = 'AAACTTTTTAGCCCCCCCGGGGTTTTTAAA'

    assert compress(strand) == '3AC5TAG7C4G5T3A'
    assert compress_prima(strand) == '3AC5TAG7C4G5T3A'
    assert ''.join(compress_generator(strand)) == '3AC5TAG7C4G5T3A'


if __name__ == '__main__':
    exit(main())
