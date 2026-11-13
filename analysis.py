"""NumPy + Matplotlib practice: 30 monthly values arranged as 5 years x 6 months."""
import matplotlib.pyplot as plt
import numpy as np

DATA = [
    5000, 5000, 5500, 5800, 6000, 6500,
    8000, 8000, 8000, 8500, 9000, 9500,
    10000, 10500, 10500, 10500, 11000, 12000,
    16000, 16000, 16500, 17000, 17500, 18000,
    20000, 21000, 22000, 22000, 23000, 43000,
]
YEARS = ["1396", "1397", "1398", "1399", "1400"]
MONTHS = ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar"]


def to_matrix(data):
    return np.array(data).reshape(len(YEARS), len(MONTHS))


def peak_position(matrix):
    """Return (year_number, month_number), 1-based, of the largest value."""
    row, col = np.unravel_index(np.argmax(matrix), matrix.shape)
    return row + 1, col + 1


def percent_change(old, new):
    return (new - old) / old * 100


def plot_yearly_means(means):
    plt.figure()
    plt.plot(YEARS, means)
    plt.title("Mean per year")


def plot_dashboard(matrix, means):
    plt.figure(figsize=(10, 8))
    for i, year_values in enumerate(matrix):
        plt.subplot(3, 2, i + 1)
        plt.plot(MONTHS, year_values)
        plt.title(YEARS[i])
        plt.xticks(rotation=45, fontsize=7)
    plt.subplot(3, 2, 6)
    plt.plot(YEARS, means)
    plt.title("Mean per year")
    plt.tight_layout()


def main():
    matrix = to_matrix(DATA)
    print(matrix)

    yearly_means = matrix.mean(axis=1)
    print("Mean per year:", yearly_means)
    print("Mean per month (across years):", matrix.mean(axis=0))

    year, month = peak_position(matrix)
    print(f"Max value {matrix.max()} -> year: {year}\tmonth: {month}")

    print("First year:", matrix[0])
    print("Last year: ", matrix[-1])
    print("Percent change (last vs first year, per month):",
          percent_change(matrix[0], matrix[-1]))

    plot_yearly_means(yearly_means)
    plot_dashboard(matrix, yearly_means)
    plt.show()


if __name__ == "__main__":
    main()
