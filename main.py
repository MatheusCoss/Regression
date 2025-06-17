import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega os dados

def main():
    df = pd.read_csv('csv/Video_Games_Sales_as_at_22_Dec_2016.csv')
    df.head()


if __name__ == "__main__":
    main()
