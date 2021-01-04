from math import *
from numpy import *
from argparse import ArgumentParser

def comparesamples(samples1, samples2, weights, summary = 'd', analysis = 'x'):
    
    # Function reading the .csv files (samples and weights data) and prepare data for the analyses
    def data_read (file):
        with open (file) as file:
            lines = file.readlines()
            data_storage_name =[]
            for line in lines:
                row = []
                for string in line.split(','):
                    row.append(float(string.strip()))
                data_storage_name.append(row)
        return data_storage_name

    data1 = data_read(samples1)
    data2 = data_read(samples2)
    w = data_read(weights)
    
    
    results = []
# Replace loop with iterator - TODO
    for value in range(len(data1)):
        s = 0
    
    # Algorithm X - Sample difference
    # Replace loop with iterator - TODO
        if analysis == 'x':
            for element in range(len(data1)):
            # Ignore missing values
                if isnan(data1[value][element]) or isnan(data2[value][element]):
                    d = 0
                else:
                    d = data1[value][element] - data2[value][element]
                s += w[0][element] * abs(d)
            results.append(s)
        
    # Algorithm Y - Discrepancies
        if analysis == 'y':
            for element in range(len(data1)):
            # Ignore missing values
                if isnan(data1[value][element]) or isnan(data2[value][element]):
                    d = 0
                else:
                    d = (data1[value][element] - data2[value][element])**2
                
                s += w[0][element] * d
                discr = sqrt(s)
    
            results.append(round(discr,2))
    
    # Possible adding of other algorithms
    

    # Criticality - number of elements in the sample difference vector exceeding a threshold value 
    # Replace loop with iterator
    # Delete lines in excess
    critical = 0
    for result in results:
        if result > threshold:
            critical += 1
    
    # d-index - average of sample difference vector across sample pairs
    d_index = np.mean(results)
    
    if summary == 'criticality':
        return("criticality:", critical, "results above", threshold)
    if summary == 'd':
        return("d-index:", round(d_index,2))

if __name__ == "__main__":
    parser = ArgumentParser(description="Compute criticality and d-index")
    parser.add_argument('--summary', '-s')
    parser.add_argument('--analysis','-a')
    parser.add_argument('samplesl')
    parser.add_argument('samples2')
    parser.add_argument('weights')
    arguments= parser.parse_args()
    
    comparesamples(arguments.summary, arguments.analysis,arguments.samples1, arguments.samples2, arguments.weights)