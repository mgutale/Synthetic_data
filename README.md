# Synthetic Data Generator

This is a Python script for generating synthetic data based on user-specified column information. The generated data can be saved as a CSV file and is accompanied by a metadata file describing the data columns.

## Installation

To run this script, you will need to have Python 3.x installed on your system along with the following packages:

numpy
pandas
faker

To install these packages, you can run the following command:

pip install numpy pandas faker

## Usage

To use this script, you need to specify the column information in the columns_info dictionary in the main section of the script. The dictionary should have the following structure:

columns_info = {
    'column1': {'dtype': 'object', 'values': [...], 'description': '...'},
    'column2': {'dtype': 'int', 'mean': ..., 'std': ..., 'description': '...'},
    'column3': {'dtype': 'float', 'mean': ..., 'std': ..., 'description': '...'},
    ...
}

For each column, you need to specify the data type (object, int, or float), possible values (for object columns), mean and standard deviation (for numeric columns), and a description of the column (optional).

To generate the synthetic data, you can run the script from the command line:

python main.py

The script will generate a synthetic data set with 1000 rows (you can change this in the generate_synthetic_data function), and save it as a CSV file called synthetic_data.csv. It will also generate a metadata file called metadata.csv that describes the columns of the synthetic data.

## License

This script is licensed under the MIT License - see the LICENSE.md file for details.
