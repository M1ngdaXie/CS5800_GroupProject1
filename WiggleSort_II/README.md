# Wiggle Sort II Analysis

**Group 6 - Divide and Conquer**  
George Lin, Minda Xie, Andrew Li, Xiaoti Hu

## Quick Start

To run the benchmark with default settings:

```bash
python(3) WiggleSortII_Analysis
```

This will generate runtime plots for all three algorithms—Brute-force, Divide & Conquer, and Greedy—and save the output as wiggleSort_Result_RealTime.png.



## Usage

```bash
python(3) WiggleSortII_Analysis.py --ratios [uniqueness_level] --sizes [sizes]
```

### Parameters
- `uniqueness_level`: Uniqueness level of the array values
Accepts one or more float values between 0 and 1
(e.g., 0.1 for 10% unique values, 0.5 for 50%, 0.9 for 90%)
- `sizes`: Comma-separated list of input sizes
(e.g., 1000 5000 10000)
Use "default" to use the built-in sizes [1000, 5000, 10000]


## Examples
Run with default settings:

```bash
python(3) WiggleSortII_Analysis
```

Run with custom uniqueness levels:

```bash
python(3) WiggleSortII_Analysis --ratios 0.2 0.8
```
Run with custom input sizes:


```bash
python(3) WiggleSortII_Analysis --sizes 2000 6000 10000
```
Customize both:

```bash
python(3) WiggleSortII_Analysis --ratios 0.1 0.5 0.9 --sizes 500 1000 2000
```


## Files

- `WiggleSortII_Analysis.py` - Main analysis script
- `Brute_Force.py` – Brute-force wiggle sort implementation
- `Divide_and_Conquer.py` – O(n)-time median partitioning implementation
- `Greedy.py` – Greedy interleaving-based approach
- `wiggleSort_Result_RealTime.png` - Results displayed as interactive matplotlib graphs
- `WiggleSortII_TimeAnalysis.png` - Output We generated for report.