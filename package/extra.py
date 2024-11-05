import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import os
import pandas as pd
from os import listdir
from os.path import isfile, join
import time


def parse_xlsx(source_directory, output_csv_directory, output_png_directory):
    while len(os.listdir(source_directory)) == 0:
        time.sleep(1)
    files = [f for f in listdir(source_directory) if isfile(join(source_directory, f))]

    for curr in files:
        filepath = source_directory + "/" + curr
        df = pd.read_excel(filepath)
        material = df.columns[0]

        # Identify rows containing string values


        # Drop rows containing string values
        df = df[df.apply(lambda x: pd.to_numeric(x, errors='coerce').notnull().all(), axis=1)]
        #original below
        arr = df.to_numpy(dtype='float64')
        #arr = df.to_numpy()
        temps, index, counts = np.unique(df.values.T[0], return_index=True, return_inverse=False, return_counts=True)
        for i in range(len(temps)):
            start = index[i]
            end = index[i] + counts[i]
            strain = arr.T[1][start:end]
            stress = arr.T[2][start:end]

            # Create a cubic spline interpolation function
            f = interp1d(strain, stress, kind='cubic')

            # Create a vector of x values to interpolate over
            x_interp = np.linspace(strain[0], strain[-1], 1000)

            # Use the spline interpolation function to interpolate the y values
            y_interp = f(x_interp)

            # Write x and y values to a CSV file
            csv_file = f'{output_csv_directory}/{material}_{temps[i]}°C.csv'
            with open(csv_file, 'w') as file:
                file.write('Strain,Stress\n')
                for j in range(len(x_interp)):
                    file.write(f'{x_interp[j]},{y_interp[j]}\n')

            # Plot the interpolated curve and original data points
            plt.plot(x_interp, y_interp)

            # Add axis labels title and legend
            plt.xlabel('Strain [%]')
            plt.ylabel('Stress [MPa]')

            # plt.title('Stress-Strain Curve for ~MATERIAL NAME/ Temperature~')
            title = f'Stress-Strain Curve for {material}/{temps[i]}°C'
            plt.title(title)

            image_path = f'{output_png_directory}/{material}_{temps[i]}°C.jpg'
            plt.savefig(image_path)

            plt.clf()
