from generators.generators import Generator
from algorithms.quickSort import quickSort
from visualization.visualize import Visualizer
import time


def runQuickSort(arr):
    '''
    function that runs and times quick sort
    arr -> list of integers
    return -> time in seconds^(-5), num of operations
    '''
    startTime = time.perf_counter_ns()
    steps = quickSort(arr, 0, len(arr) - 1)
    endTime = time.perf_counter_ns()
    return (endTime - startTime) / 10000000.0, steps

def runSortedArrays(inputs):
    '''
    function that performs a run on quick
    sort using sorted arrays as input
    inputs -> array of input sizes
    return -> info about the algorithm run (time and steps)
    '''
    quickTimes = []         # cpu time for quick sort
    quickSteps = []         # num of operations for quick sort

    for inputSize in inputs:
        generator = Generator(inputSize)
        newArray = generator.generateSortedArray()
        quickTime, quickStep = runQuickSort(newArray)
        
        quickTimes.append(quickTime)
        quickSteps.append(quickStep)

    return quickTimes, quickSteps


def runReversedSortedArrays(inputs):
    '''
    function that performs a run on quick sort
    using reversed sorted arrays as input
    inputs -> array of input sizes
    return -> info about the algorithm run (time and steps)
    '''
    quickTimes = []         # cpu time for quick sort
    quickSteps = []         # num of operations for quick sort

    for inputSize in inputs:
        generator = Generator(inputSize)
        newArray = generator.generateReversedSortedArray()
        quickTime, quickStep = runQuickSort(newArray)
        
        quickTimes.append(quickTime)
        quickSteps.append(quickStep)

    return quickTimes, quickSteps


def runRandomPermutationArrays(inputs):
    '''
    function that performs a run on quick sort
    using random permutations as input
    inputs -> array of input sizes
    return -> info about the algorithm run (time and steps)
    '''
    quickTimes = []         # cpu time for quick sort
    quickSteps = []         # num of operations for quick sort

    for inputSize in inputs:
        generator = Generator(inputSize)
        newArray = generator.generateRandomPermutation()
        quickTime, quickStep = runQuickSort(newArray)
        
        quickTimes.append(quickTime)
        quickSteps.append(quickStep)

    return quickTimes, quickSteps


def run50RandomInRangeArrays(inputs):
    '''
    function that generates n arrays of n random numbers (n is each entry in inputs)
    and returns info about the run in the form of average of the n runs
    inputs -> list of array sizes
    return -> average info about the algorithm run (time and steps)
    '''
    finalquickTimes = []     # cpu time for quick sort
    finalquickSteps = []     # num of operations for quick sort
    for inputSize in inputs:
        quickTimes = []
        quickSteps = []
        generator = Generator(inputSize)
        arrays = generator.generate50RandomInRange()
        for array in arrays:
            quickTime, quickStep = runQuickSort(array)
            quickTimes.append(quickTime)
            quickSteps.append(quickStep)
        
        # appending the average of the n runs in the final result array
        finalquickTimes.append(sum(quickTimes)/len(quickTimes))
        finalquickSteps.append(sum(quickSteps)/len(quickSteps))
    
    return finalquickTimes, finalquickSteps


if __name__ == '__main__':

    # input sizes given in the instructions
    inputs = [100, 200, 300, 400, 500, 600]
    print()

    visualizer = Visualizer(inputs)

    # running algorithms for the sorted array inputs
    quickTimes, quickSteps = runSortedArrays(inputs)
    print('- SORTED ARRAYS -')
    print()
    visualizer.printSingleRunValues(quickTimes, quickSteps)
    visualizer.plotCurves(inputs, quickTimes, 'SORTED ARRAYS')

    print('[STILL RUNNING] wait for the new output...')
    print()

    # running algorithms for the reversed sorted array inputs
    quickTimes, quickSteps = runReversedSortedArrays(inputs)
    print('- REVERSED SORTED ARRAYS -')
    print()
    visualizer.printSingleRunValues(quickTimes, quickSteps)
    visualizer.plotCurves(inputs, quickTimes, 'REVERSED SORTED ARRAYS')

    print('[STILL RUNNING] wait for the new output...')
    print()

    # running algorithms for the random permutation array inputs
    quickTimes, quickSteps = runReversedSortedArrays(inputs)
    print('- RANDOM PERMUTATION ARRAYS -')
    print()
    visualizer.printSingleRunValues(quickTimes, quickSteps)
    visualizer.plotCurves(inputs, quickTimes, 'RANDOM PERMUTATION ARRAYS')

    print('[STILL RUNNING] wait for the new output...')
    print()

    # running algorithms for the random permutation array inputs
    quickTimes, quickSteps = run50RandomInRangeArrays(inputs)
    print('- 50 RANDOM ARRAYS EACH RUN -')
    print()
    visualizer.printSingleRunValues(quickTimes, quickSteps)
    visualizer.plotCurves(inputs, quickTimes, '50 RANDOM ARRAYS EACH RUN')