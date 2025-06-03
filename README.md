# Stock_Data: List of Stock Symbols with CUSIP ID Numbers

A comprehensive collection of stock symbols paired with their corresponding CUSIP (Committee on Uniform Securities Identification Procedures) identification numbers.

## Overview

This repository contains a dataset that maps publicly traded company stock symbols to their unique CUSIP identifiers. CUSIP numbers are 9-character alphanumeric identifiers assigned to North American financial securities for the purposes of facilitating clearing and settlement of trades.

## Contents

- `CUSIP.csv`: Main dataset containing stock symbols and their CUSIP IDs
- `EOD/`: Archive of previous versions of the dataset

## Data Format

The primary dataset is provided in CSV format with the following columns:

| Column | Description |cusip,symbol,description
|--------|-------------|
| CUSIP | The 9-character CUSIP identifier |
| Symbol | The stock ticker symbol as used on major exchanges |
| Description | Full registered name of the company / Mutual Fund |

## Usage

### Retrieving CUSIP for a Stock Symbol

```python
import pandas as pd

# Load the dataset
stock_data = pd.read_csv('stock_cusip_mapping.csv')

# Get CUSIP for a specific stock symbol
symbol = 'AAPL'  # Apple Inc.
cusip = stock_data[stock_data['Symbol'] == symbol]['CUSIP'].values[0]
print(f"The CUSIP for {symbol} is {cusip}")
```


## Data Sources

This dataset is compiled from multiple sources including:

- SEC EDGAR database
- Public filings
- Exchange listings
- Financial data providers

Data is periodically validated for accuracy, but users should perform their own verification for critical applications.

## Limitations

- This dataset may not include all possible stock symbols
- Some securities might have changed their CUSIP numbers due to corporate actions
- The dataset is updated periodically but may not reflect the most recent changes

## Contributing

Contributions to improve or expand this dataset are welcome. Please submit pull requests with:

1. Clear description of the changes
2. Source of the new/updated information
3. Date when the information was obtained

## License

This dataset is provided under [choose appropriate license] license. See the LICENSE file for details.

## Citation

If you use this dataset in your research or project, please cite it as:

```
Yoshishima. (2025). Stock_Data: List of Stock Symbols with CUSIP ID number. GitHub Repository. https://github.com/yoshishima/Stock_Data
```

## Website

For additional resources and tools related to this dataset, visit our website: [https://thax.io](https://thax.io)

## Contact

For questions, corrections, or additional information, please [open an issue](https://github.com/yoshishima/Stock_Data/issues) on this repository.
