import numpy as np
import pandas as pd
import random
from faker import Faker
import json


def generate_synthetic_data(num_rows, columns_info):
    """
    Generates synthetic data based on user-specified column information.

    Args:
        num_rows (int): Number of rows to generate.
        columns_info (dict): Dictionary containing information about columns.
            Each key is the name of a column, and the corresponding value is
            another dictionary with the following keys:
            - 'dtype' (str): Data type of the column, either 'object', 'int', or 'float'.
            - 'values' (list): List of possible values for object columns, or list of
                numeric values for int/float columns.
            - 'mean' (float, optional): Mean value for int/float columns. Required if
                dtype is 'int' or 'float'.
            - 'std' (float, optional): Standard deviation for int/float columns. Required if
                dtype is 'int' or 'float'.
        output_path (str): File path to save the generated synthetic data as a CSV file.

    Returns:
        A pandas DataFrame containing the synthetic data.
    """
    synthetic_df = pd.DataFrame()

    for column, info in columns_info.items():
        if info['dtype'] == 'object':
            unique_values = info['values']
            num_unique = len(unique_values)
            synthetic_column = np.random.choice(unique_values, size=num_rows)
        else:
            mean = info.get('mean', 0)
            std = info.get('std', 1)
            synthetic_column = np.random.normal(
                loc=mean, scale=std, size=num_rows)
            if column == 'Age':
                synthetic_column = synthetic_column.astype(int)
            elif column == 'CustomerID':
                synthetic_column = np.arange(1, num_rows + 1)
            elif column == 'Fee':
                synthetic_column = np.round(synthetic_column, 2)
            elif column == 'Mosaic_profile':
                low, high = info.get('range', (1, 75))
                synthetic_column = np.random.randint(
                    low=low, high=high+1, size=num_rows)
        synthetic_df[column] = synthetic_column
    return synthetic_df


if __name__ == '__main__':
    # Define column information
    columns_info = {
        'Location': {'dtype': 'object', 'values': ['Bournemouth', 'London', 'Manchester', 'Liverpool', 'Leeds']},
        'CustomerID': {'dtype': 'int'},
        'Age': {'dtype': 'int', 'mean': 40, 'std': 10},
        'Gender': {'dtype': 'object', 'values': ['Male', 'Female']},
        'Subscription Type': {'dtype': 'object', 'values': ['Gold', 'Silver', 'Diamond', 'Copper']},
        'Subscription Subtype': {'dtype': 'object', 'values': ['A', 'B', 'C']},
        'Fee': {'dtype': 'float', 'mean': 20, 'std': 5},
        'Activity': {'dtype': 'object', 'values': ['gym', 'swim', 'fitness classes']},
        'Mosaic_profile': {'dtype': 'int', 'range': (1, 75)}
    }

    # Generate synthetic dataset with 10 rows
    synthetic_df = generate_synthetic_data(100000, columns_info)

    # Generate metadata for the synthetic dataset
    metadata = {}
    for column, info in columns_info.items():
        data = synthetic_df[column]
        if data.dtype == object:
            data = data.astype(str)
        elif data.dtype == bool:
            data = data.astype(int)
        metadata[column] = {
            'dtype': str(data.dtype),
            'description': '',
            'values': info['values'] if info['dtype'] == 'object' else [],
            'min': np.min(data) if data.dtype != object else None,
            'max': np.max(data) if data.dtype != object else None,
            'mean': np.mean(data) if data.dtype != object else None,
            'std': np.std(data) if data.dtype != object else None,
        }

    # Save metadata to CSV file
    metadata_df = pd.DataFrame.from_dict(metadata, orient='index')
    metadata_df.to_csv('metadata.csv', index=True)

    # Print metadata
    print(metadata_df)

    # Print the synthetic dataset
    print(synthetic_df.head())

    # Save the synthetic dataset to CSV file
    synthetic_df.to_csv('synthetic_data.csv', index=False)
