import multiprocessing
"""
def process_data(data):
    # Perform some computation on the data
    result = data * 2
    return result
"""
def pro_data(daata):
    result1=daata*5+7
    return result1

if __name__ == '__main__':
    
    input_data = [1, 2, 3, 4, 5]

    # Create a pool of worker processes
    pool = multiprocessing.Pool()

    # Apply the process_data function to each element in input_data using parallel processing
   # results = pool.map(process_data, input_data)

    #different process
    results1=pool.map(pro_data,input_data)

    # Close the pool 
    pool.close()
    pool.join()

   #print(results)
    print(results1)
