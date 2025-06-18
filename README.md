# Coding Files Usage Guide

**Group 6 - Divide and Conquer**  
George Lin, Minda Xie, Andrew Li, Xiaoti Hu

This document contains instructions on how to run the analysis on the following algorithms: **Top K Frequent Elements** and **Wiggle Sort II**. Both analyses compare multiple algorithmic approaches and generate performance visualizations.

## Table of Contents
- [Top K Frequent Elements Analysis](#top-k-frequent-elements-analysis)
  - [Quick Start](#top-k-quick-start)
  - [Usage](#top-k-usage)
  - [Examples](#top-k-examples)
  - [Files](#top-k-files)
- [Wiggle Sort II Analysis](#wiggle-sort-ii-analysis)
  - [Quick Start](#wiggle-quick-start)
  - [Usage](#wiggle-usage)
  - [Examples](#wiggle-examples)
  - [Files](#wiggle-files)

---

## Top K Frequent Elements Analysis

Compares three algorithms for finding the top K most frequent elements in an array:
- **Sort-based**: O(n log n) time complexity
- **Bucket Sort**: O(n) time complexity
- **Heap-based**: O(n log k) time complexity

### Top K Quick Start

```bash
python(3) AnalysisTopK.py
```

This runs the analysis with default settings and displays interactive matplotlib graphs comparing all three algorithms.

### Top K Usage

```bash
python(3) AnalysisTopK.py [uniqueness_level] [sizes] [k]
```

#### Parameters
- `uniqueness_level`: Data uniqueness level
  - `1` = 10% unique values
  - `2` = 50% unique values  
  - `3` = 90% unique values
- `sizes`: Input array sizes (comma-separated) or "default"
- `k`: Number of top elements to find (default: 100)

### Example Command-line calls

```bash
# Show all scenarios with default settings
python TopKAnalysisEnhanced.py

# Test 50% uniqueness with default sizes and k=100
python TopKAnalysisEnhanced.py 2

# Test 10% uniqueness with custom sizes and k=100  
python TopKAnalysisEnhanced.py 1 1000,5000,10000

# Test 90% uniqueness with default sizes and k=50
python TopKAnalysisEnhanced.py 3 default 50

# Full custom: 50% uniqueness, custom sizes, k=25
python TopKAnalysisEnhanced.py 2 500,2000,8000 25

# Help
python TopKAnalysisEnhanced.py --help
```

### Top K Files

- `AnalysisTopK.py` - Main analysis script
- `TopKSolutions.py` - Algorithm implementations
- Results displayed as interactive matplotlib graphs

---

## Wiggle Sort II Analysis

Compares three algorithms for wiggle sorting (arranging array so that `nums[0] < nums[1] > nums[2] < nums[3]...`):
- **Brute-force**: Simple sorting approach
- **Divide & Conquer**: O(n)-time median partitioning implementation
- **Greedy**: Interleaving-based approach

### Wiggle Quick Start

```bash
python(3) WiggleSortII_Analysis.py
```

This generates runtime plots for all three algorithms and saves the output as `wiggleSort_Result_RealTime.png`.

### Wiggle Usage

```bash
python(3) WiggleSortII_Analysis.py --ratios [uniqueness_level] --sizes [sizes]
```

#### Parameters
- `uniqueness_level`: Uniqueness level of array values
  - Float values between 0 and 1 (e.g., 0.1 for 10%, 0.5 for 50%, 0.9 for 90%)
  - Can specify multiple values
- `sizes`: Comma-separated list of input sizes or "default"
  - Default sizes: [1000, 5000, 10000]

### Wiggle Examples

```bash
# Run with default settings
python(3) WiggleSortII_Analysis.py

# Run with custom uniqueness levels
python(3) WiggleSortII_Analysis.py --ratios 0.2 0.8

# Run with custom input sizes
python(3) WiggleSortII_Analysis.py --sizes 2000 6000 10000

# Customize both parameters
python(3) WiggleSortII_Analysis.py --ratios 0.1 0.5 0.9 --sizes 500 1000 2000
```

### Wiggle Files

- `WiggleSortII_Analysis.py` - Main analysis script
- `Brute_Force.py` - Brute-force wiggle sort implementation
- `Divide_and_Conquer.py` - O(n)-time median partitioning implementation
- `Greedy.py` - Greedy interleaving-based approach
- `wiggleSort_Result_RealTime.png` - Runtime analysis results
- `WiggleSortII_TimeAnalysis.png` - Generated output for report

---

## Libraries & Set up

1. Ensure you have Python3 and matplotlib installed
2. Clone this repository or download associated code files
3. Run either analysis script with your desired parameters
4. View the generated performance graphs to compare algorithmic approaches

For questions or issues, please refer to the individual script help documentation using the `--help` flag.