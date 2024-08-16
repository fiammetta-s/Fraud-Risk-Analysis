import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    # Load the dataset from a CSV file into a Pandas DataFrame.
    return pd.read_csv(file_path)

def display_data_overview(df):
    # Prints an overview of the dataset, including column names and a sample of the data.
    print("Column Names:", df.columns.tolist())
    print("First 5 Rows:\n", df.head())
    print("Random Sample:\n", df.sample(5))

def analyze_transactions(df):
    # Perform various analyses on the transaction data.
    print("Unique Transaction Types:", df['type'].unique().tolist())
    print("Top 10 Transaction Destinations:\n", df['nameDest'].value_counts().head(10))
    print("Fraudulent Transactions Count:", len(df[df['isFraud'] == 1]))
    print("Interactions by Source:\n", df.groupby('nameOrig')['nameDest'].nunique().sort_values(ascending=False).reset_index(name='distinct_destinations'))
    
    # Calculate and print fraud correlation
    fraud_correlation = df['amount'].corr(df['isFraud'])
    print("Fraud Correlation:", fraud_correlation)

def plot_visualizations(df):
    # Generate and show various plots.
    plt.figure(figsize=(14, 7))
    
    # Plot top destinations
    plt.subplot(1, 3, 1)
    df['nameDest'].value_counts().head(10).plot(kind='bar')
    plt.title('Top 10 Transaction Destinations')
    plt.xlabel('Destination')
    plt.ylabel('Frequency')
    
    # Plot transactions over time
    plt.subplot(1, 3, 2)
    df.groupby('step').size().plot(kind='line')
    plt.title('Transactions Over Time')
    plt.xlabel('Time Step')
    plt.ylabel('Number of Transactions')
    
    # Plot transaction amount distribution
    plt.subplot(1, 3, 3)
    df['amount'].hist(bins=50)
    plt.title('Distribution of Transaction Amounts')
    plt.xlabel('Transaction Amount')
    plt.ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()

def main():
    # Main function to execute the analysis.
    file_path = 'transactions.csv'
    df = load_data(file_path)
    display_data_overview(df)
    analyze_transactions(df)
    plot_visualizations(df)

if __name__ == "__main__":
    main()
