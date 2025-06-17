# Top K Frequent Elements Analysis

**Group 6 - Divide and Conquer**  
George Lin, Minda Xie, Andrew Li, Xiaoti Hu

## Quick Start

Run the analysis script to compare three algorithms for finding the top K most frequent elements:
- Sort-based (O(n log n))
- Bucket Sort (O(n)) 
- Heap-based (O(n log k))

## Usage

```bash
python(3) TopKAnalysisEnhanced.py [uniqueness_level] [sizes] [k]
```

### Parameters
- `uniqueness_level`: 1 (10%), 2 (50%), or 3 (90%)
- `sizes`: comma-separated input sizes or "default" 
- `k`: number of top elements to find (default: 100)

## Examples

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


## Files

- `TopKAnalysisEnhanced.py` - Main analysis script
- `TopKSolutions.py` - Algorithm implementations
- Results displayed as interactive matplotlib graphs