# Fraud Risk Analysis

## Project Overview

This project involves analyzing a dataset of financial transactions to identify patterns and potential fraud. The dataset is a subset of the [PaySim dataset](https://www.kaggle.com/ealaxi/paysim1/version/2), which was originally generated as part of the following research:

E. A. Lopez-Rojas, A. Elmir, and S. Axelsson. *"PaySim: A financial mobile money simulator for fraud detection"*. In: The 28th European Modeling and Simulation Symposium-EMSS, Larnaca, Cyprus. 2016.

The main objectives are to perform exploratory data analysis (EDA), visualize important metrics, and compute statistical insights to understand the nature of fraud in financial services. The script uses `pandas` for data manipulation and `matplotlib` for plotting.

## Features

- **Data Loading**: Loads a CSV file containing transaction data into a Pandas DataFrame.
- **Data Overview**: Displays basic information about the dataset, including column names, the first few rows, and a random sample.
- **Transaction Analysis**:
  - Lists unique transaction types.
  - Identifies the top 10 transaction destinations.
  - Counts fraudulent transactions.
  - Summarizes the number of distinct destinations each source has interacted with.
  - Calculates the correlation between transaction amount and fraud occurrence.
- **Visualizations**:
  - Bar chart of the top 10 transaction destinations.
  - Line chart of transactions over time.
  - Histogram of transaction amounts.

## Installation

To run this project, you need to have Python installed along with the required libraries. You can install the required libraries using `pip`:

```bash
pip install pandas matplotlib
```

## Dataset

The dataset should be a CSV file named `transactions.csv`. The expected directory structure is:

```
.
├── main.py
└── transactions.csv
```

Ensure that your CSV file contains the following columns: `step`, `type`, `amount`, `nameOrig`, `oldbalanceOrg`, `newbalanceOrig`, `nameDest`, `oldbalanceDest`, `newbalanceDest`, `isFraud`, `isFlaggedFraud`.

## Usage

1. **Prepare Your Data**:
   - Place your `transactions.csv` file in the same directory as the script.

2. **Run the Script**:
   ```bash
   python main.py
   ```

3. **View Results**:
   - The script prints various outputs to the console:
     - **Column Names**: Lists all column names in the dataset.
     - **First 5 Rows**: Displays the first 5 rows of the dataset.
     - **Random Sample**: Shows a random sample of 5 rows.
     - **Unique Transaction Types**: Lists unique transaction types.
     - **Top 10 Transaction Destinations**: Displays the top 10 transaction destinations by frequency.
     - **Fraudulent Transactions Count**: Shows the number of fraudulent transactions.
     - **Interactions by Source**: Summarizes interactions by source.
     - **Fraud Correlation**: Calculates and prints the correlation between transaction amount and fraud occurrence.

   - The script also generates the following visualizations:
     - **Top Transaction Destinations**: A bar chart of the top 10 transaction destinations.
     - **Transactions Over Time**: A line chart showing the number of transactions over time.
     - **Transaction Amount Distribution**: A histogram of transaction amounts.

## Code Overview

- **`load_data(file_path)`**:
  - Loads the dataset from the specified CSV file into a DataFrame.

- **`display_data_overview(df)`**:
  - Prints an overview of the dataset, including column names, the first few rows, and a random sample.

- **`analyze_transactions(df)`**:
  - Performs various analyses on the transaction data and prints the results.

- **`plot_visualizations(df)`**:
  - Generates and displays plots for top destinations, transactions over time, and transaction amount distribution.

- **`main()`**:
  - Main function to execute the data loading, analysis, and visualization.

## Contribution

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

