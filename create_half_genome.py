
import random

def generate_large_dna_file(filename,
                            total_size=3_000_000_000,
                            chunk_size=10_000_000):
    with open(filename, 'w') as f:
        for _ in range(total_size // chunk_size):
            chunk = ''.join(random.choices('agct', k=chunk_size))
            f.write(chunk)
        remainder = total_size % chunk_size
        if remainder:
            chunk = ''.join(random.choices('agct', k=remainder))
            f.write(chunk)

if __name__ == '__main__':
    generate_large_dna_file("half_genomes/gen3.txt")
    print("File generation complete")
