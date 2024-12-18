

def load_input(f_p):
    with open(f_p, 'r') as file:
        file_content = file.read()
    print(f"Genome Length: {len(list(file_content))}")
    return file_content
    

def preprocess(raw_string):
    raw_string = raw_string.replace("\n", "")
    txtL = list(raw_string)
    return txtL


def complement(seqL):
    if type(seqL) != list:
        try:
            seqL = list(seqL)
        except:
            raise ValueError("Sequence must be a list.")
    compL = seqL[:]
    i=0
    for base in compL:
        if base == 'a':
            compL[i] = 't'
        elif base == 't':
            compL[i] = 'a'
        elif base == 'g':
            compL[i] = 'c'
        elif base == 'c':
            compL[i] = 'g'
        else:
            raise ValueError("Non-nucleotide detected in sequence.")
        i+=1
    compL = ''.join(compL)
    
    for x,y in zip(seqL[0:5], compL[0:5]):
        print(x,'----',y)

    return compL



from pyspark import SparkContext
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("DNA").getOrCreate()
sc = spark.sparkContext

def complement_parallel(seqL):
    
    def complement(base):
        if base == 'a':
            return 't'
        elif base == 't':
            return 'a'
        elif base == 'g':
            return 'c'
        elif base == 'c':
            return 'g'
        else:
            raise ValueError("Non-nucleotide detected in sequence.")

    try:
        rdd = sc.parallelize(seqL, numSlices=8)
        complemented_rdd = rdd.map(complement)
        result = ''.join(complemented_rdd.collect())
        return result
    finally:
        sc.stop()


def send_output(f_p, output):
    f = open(f_p, "w")
    f.write(output)
    f.close()



if __name__ == '__main__':

    input_path = 'half_genomes/gen3.txt'
    output_path = 'half_genomes/gen3c.txt'
    
    file_content = load_input(input_path)
    sequence3 = preprocess(file_content)
    
    result = complement(sequence3)
    #result = complement_parallel(sequence3)

    send_output(output_path, result)
    
    print("Process complete")

