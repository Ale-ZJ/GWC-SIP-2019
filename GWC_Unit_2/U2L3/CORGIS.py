import school_scores
import matplotlib.pyplot as plt
import numpy as np

def main():
    #get the data into a list
    list_of_record = school_scores.get_all()
    years = ['2005','2006', '2007','2008','2009','2010', '2011', '2012', '2013', '2014', '2015']
    incomes = ["Less than 20k", "Between 20-40k", "Between 40-60k", "Between 60-80k", "Between 80-100k", "More than 100k"]

    takers_1_list = get_takers_per_income1(list_of_record)
    takers_6_list = get_takers_per_income6(list_of_record)

    get_table_test_takers(takers_1_list, takers_6_list, years)


def get_takers_per_income1(list_of_record):
    #initializing variables
    dict = {}
    list = []

    for row in list_of_record:
        test_year = row["Year"] #get the year in a row of data

        #if the year is in the dict, then add the test taker numbers with the value that is already stored,
        #if the year is not in the list, then add the year and the test takers into the dictionary
        if test_year in dict:
            dict[test_year] += row["Family Income"]["Less than 20k"]["Test-takers"]
        else:
            dict[test_year] = 0

    for val in dict:
        list.append(dict[val])

    return list

def get_takers_per_income6(list_of_record):
    #initializing variables
    dict = {}
    list = []

    for row in list_of_record:
        test_year = row["Year"]
        if test_year in dict:
            dict[test_year] += row["Family Income"]["More than 100k"]["Test-takers"]
        else:
            dict[test_year] = 0

    for val in dict:
        list.append(dict[val])

    return list

def get_table_test_takers(takers1, takers6, x_label):
    fig, ax = plt.subplots()
    index = np.arange(len(x_label))

    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, takers1, bar_width,
    color = 'pink',
    label = "Less than 20k")

    rects2 = plt.bar(index + bar_width, takers6, bar_width,
    color = 'purple',
    label = "More than 100k")

    plt.xlabel("Years", fontsize = 10)
    plt.ylabel("Number of test takers", fontsize = 10)
    plt.title("Number of test takers over 10 years")
    plt.xticks(index + bar_width, x_label)
    plt.legend()

    plt.show()



if __name__ == "__main__":
    main()
