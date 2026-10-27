# EverQuint Max Profit Problem

## Overview
This project implements a Python solution to the Max Profit interview assignment. It determines the maximum earnings achievable by constructing theatres, pubs, and commercial parks sequentially within a given time budget.

## Building Details

| Building | Construction Time | Earnings per Operating Time Unit |
|---|---:|---:|
| Theatre (T) | 5 | $1,500 |
| Pub (P) | 4 | $1,000 |
| Commercial Park (C) | 10 | $2,000 |

## Approach
The solution uses dynamic programming with memoization to compare feasible construction sequences and select the sequence with maximum earnings.

## Files
- `max_profit.py` — Python implementation.
- `Max_Profit_Problem.ipynb` — Google Colab notebook containing the code and tests.

## Run Instructions
Install Python 3, then execute:

```bash
python max_profit.py
```

Alternatively, open the notebook in Google Colab and run its cells.

## Assignment Test Cases
- Time budget: 7 units — expected earnings: $3,000.
- Time budget: 8 units — expected earnings: $4,500.
- Time budget: 13 units — expected earnings: $16,500.

## Testing
The implementation includes assertions for the three assignment examples and additional edge cases.

## Assumptions
Buildings are constructed sequentially. A building starts earning after construction is completed. A building completed exactly at the end of the available time earns zero.
