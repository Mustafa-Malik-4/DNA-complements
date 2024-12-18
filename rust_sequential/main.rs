use std::fs;
use std::fs::OpenOptions;
use std::io::Write;
use std::error::Error;

const INPUT_FILE: &str = "/Users/mustafam/Desktop/Files/genomics/half_genomes/gen3.txt";
const OUTPUT_FILE: &str = "/Users/mustafam/Desktop/Files/genomics/half_genomes/gen3c.txt";


fn complement(base: char) -> char {
    match base {
        'a' => 't',
        't' => 'a',
        'g' => 'c',
        'c' => 'g',
        _ => base,
    }
}

fn main() -> Result<(), Box<dyn Error>> {

    let sequence = fs::read_to_string(INPUT_FILE)?;
    println!("Read sequence");

    let complement_sequence: String = sequence.chars().map(complement).collect();
    println!("Complemented sequence");

    let mut file = OpenOptions::new()
        .write(true)    
        .create(true)   
        .truncate(true) 
        .open(OUTPUT_FILE)?;

    file.write_all(complement_sequence.as_bytes())?;
    println!("Operation complete");

    Ok(())
}
