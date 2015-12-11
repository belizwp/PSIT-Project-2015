'''
Main of Program
=========================
Parameter Instruction.
sex    --> 0 == male and femal (default)
           1 == male only
           2 == female only

year_0 --> begin range of year. (default=1900)
year_1 --> end range of year.   (default=2011)

age_0  --> begin range of age.  (default=0)
age_1  --> end range of age.    (default=119)

'''
from data_tool import *
import numpy as np
from matplotlib.dates import YearLocator, DateFormatter
from matplotlib.ticker import FormatStrFormatter
import datetime as dt
import matplotlib.pyplot as plt

def calculate_meandeath_men(num):
    """return a average death of men"""
    date = load_data(1)
    mean = sum(date[num])/120
    return mean

def calculate_meandeath_female(num):
    """return a average death of female"""
    date = load_data(2)
    mean = sum(date[num])/120
    return mean

def death_probability_graph_of_male_and_female():
    """Create death probability graph of male and female, black line represent as male and pink line represent as female"""

    date_lis = []
    mean_lis_men = []
    mean_lis_fem = []
    for i in range(1900, 2012):
        dates = dt.datetime(i, 1, 1)
        values_m = calculate_meandeath_men(i)
        values_f = calculate_meandeath_female(i)
        mean_lis_men.append(values_m*100)
        mean_lis_fem.append(values_f*100)
        date_lis.append(dates)

    fig, ax = plt.subplots()
    ax.plot_date(date_lis, mean_lis_men, 'b-', label = 'MALE', alpha=3, linewidth=2)
    ax.plot_date(date_lis, mean_lis_fem, '-', color='#ff3366', label = 'FEMALE', alpha=2, linewidth=2)
    plt.rcParams.update({'font.size': 17})
    plt.xlabel('Year')
    plt.ylabel('Death Probability (%)')
    plt.title('Overall of death percent in each years')

    # format the ticks
    yearsFmt = DateFormatter('%Y')
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.autoscale_view()
    ax.grid(True)

    fig.autofmt_xdate()
    plt.legend()
    plt.show()

def overall_death_probability_graph(year_0=1900, year_1=2011):
    """Create Overall death probability graph, male female average,
       black represent as male,
       pink represent as female,
       blue represent as average.
    """
    # prepare data.---------------------------------------#
    dates, mean_m, mean_f, avg = [], [], [], []
    data_m = load_data(1)
    data_f = load_data(2)

    # process data.---------------------------------------#
    for year in range(year_0, year_1 + 1):
        date = dt.datetime(year, 12, 31)
        values_m = sum(data_m[year]) / len(data_m[year]) * 100
        values_f = sum(data_f[year]) / len(data_f[year]) * 100
        mean = (values_m + values_f) / 2

        dates.append(date)
        mean_m.append(values_m)
        mean_f.append(values_f)
        avg.append(mean)

    # plot graph.-----------------------------------------#
    fig, ax = plt.subplots(figsize=(18, 6))

    ax.plot_date(dates, mean_m, 'b-', label='Male', alpha=0.9, linewidth=2)
    ax.plot_date(dates, mean_f, 'r-', label='Female', alpha=0.9, linewidth=2)
    ax.plot_date(dates, avg, 'k-', label='avg.', alpha=1)

    # format the ticks.-----------------------------------#
    years = YearLocator(5, 12, 31) # every year, month, day
    yearsFmt = DateFormatter('%Y')
    yticks = FormatStrFormatter('%.0f%%')
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.yaxis.set_major_formatter(yticks)
    ax.autoscale_view()
    ax.grid(True)

    # expression.-----------------------------------------#
    plt.rcParams.update({'font.size': 17})
    plt.xlabel('Years')
    plt.ylabel('Death Probability')
    plt.title('Overall of death percent in each years.')

    fig.autofmt_xdate()
    plt.legend()
    plt.show()

def calculate_mean_of_each_generation(num, k, mem):
    """return mean of each generation"""
    if k <= 3:
        mem.append(num)
        if len(mem) == 4:
            return sum(mem)/4
    elif k <= 6:
        mem.append(num)
        if len(mem) == 3:
            return sum(mem)/3
    elif k <= 12:
        mem.append(num)
        if len(mem) == 6:
            return sum(mem)/6
    elif k <= 19:
        mem.append(num)
        if len(mem) == 7:
            return sum(mem)/7
    elif k <= 39:
        mem.append(num)
        if len(mem) == 20:
            return sum(mem)/20
    elif k <= 59:
        mem.append(num)
        if len(mem) == 20:
            return sum(mem)/20
    elif k <= 79:
        mem.append(num)
        if len(mem) == 20:
            return sum(mem)/20
    elif k <= 119:
        mem.append(num)
        if len(mem) == 40:
            return sum(mem)/40


def death_probability_graph_men_in_each_generation():
    """Create Men death probability of each generation, a graph points about men death probability in each age
        0 - 3 baby
        4 - 6 early childhood
        7 - 12 middle childhood
        13 -19 teenager
        20 - 39 early adulthood
        40 - 59 middle adulthood
        60 - 119 old age"""
    data = load_data(1)
    date_lis = []
    baby_list = []
    early_child_list = []
    middle_child_list = []
    teenager_list = []
    early_adult_list = []
    middle_adult_list = []
    old_age_list = []
    mem = []
    for i in range(1900, 2012):
        lis_age = []
        dates = dt.datetime(i, 1, 1)
        date_lis.append(dates)
        lis_age.append(data[i])
        for k in range(len(lis_age[0])):
            if k <= 3:
                values = calculate_mean_of_each_generation(lis_age[0][k], k, mem)
                if values != None:
                    baby_list.append(values*100)
                    mem = []
            elif k <= 6:
                values = calculate_mean_of_each_generation(lis_age[0][k], k, mem)
                if values != None:
                    early_child_list.append(values*100)
                    mem = []
            elif k <= 12:
                values = calculate_mean_of_each_generation(lis_age[0][k], k, mem)
                if values != None:
                    middle_child_list.append(values*100)
                    mem = []
            elif k <= 19:
                values = calculate_mean_of_each_generation(lis_age[0][k], k, mem)
                if values != None:
                    teenager_list.append(values*100)
                    mem = []
            elif k <= 39:
                values = calculate_mean_of_each_generation(lis_age[0][k], k, mem)
                if values != None:
                    early_adult_list.append(values*100)
                    mem = []
            elif k <= 59:
                values = calculate_mean_of_each_generation(lis_age[0][k], k, mem)
                if values != None:
                    middle_adult_list.append(values*100)
                    mem = []
            elif k <= 119:
                values = calculate_mean_of_each_generation(lis_age[0][k], k, mem)
                if values != None:
                    old_age_list.append(values*100)
                    mem = []

    fig, ax = plt.subplots()
    ax.plot_date(date_lis, baby_list, 'b-', label = 'baby', alpha=3, linewidth=2)
    ax.plot_date(date_lis, early_child_list, '-', color='#ff3366', label = 'early childhood', alpha=2, linewidth=2)
    ax.plot_date(date_lis, middle_child_list, 'y-', label = 'middle childhood', alpha=3, linewidth=2)
    ax.plot_date(date_lis, teenager_list, 'c-', label = 'teenager', alpha=3, linewidth=2)
    ax.plot_date(date_lis, early_adult_list, 'r-', label = 'early adult', alpha=3, linewidth=2)
    ax.plot_date(date_lis, middle_adult_list, 'g-', label = 'middle adult', alpha=3, linewidth=2)
    ax.plot_date(date_lis, old_age_list, '-', label = 'old age', alpha=3, linewidth=2)
    plt.rcParams.update({'font.size': 17})
    plt.xlabel('Generation')
    plt.ylabel('Death Probability (%)')
    plt.title('Death probability of each generation')

    # format the ticks
    yearsFmt = DateFormatter('%Y')
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.autoscale_view()
    ax.grid(True)

    fig.autofmt_xdate()
    plt.legend()
    plt.show()

def death_probability_graph_in_bar_graph():
    """Create Death probability of each generation in bar graph, a graph points about death probability in each age
    0 - 3 baby
    4 - 6 early childhood
    7 - 12 middle childhood
    13 -19 teenager
    20 - 39 early adulthood
    40 - 59 middle adulthood
    60 - 119 old age
    60 - 79 old age less than 80
    80 - 119 old age more than 80"""
    age = ('baby', 'early', 'middle', 'teenager', 'early adulthood', 'middle adulthood', 'old age less 80', 'old age more 80')
    men_data = load_data(1)
    female_data = load_data(2)
    lis_men = []
    lis_fm = []
    baby_list = []
    early_child_list = []
    middle_child_list = []
    teenager_list = []
    early_adult_list = []
    middle_adult_list = []
    old_age_less80_list = []
    old_age_more80_list = []
    baby_list_fm = []
    early_child_list_fm = []
    middle_child_list_fm = []
    teenager_list_fm = []
    early_adult_list_fm = []
    middle_adult_list_fm = []
    old_age_less80_list_fm = []
    old_age_more80_list_fm = []
    sex_men = []
    sex_fm = []
    mem = []
    for i in range(1900, 2012):
        lis_men = []
        lis_fm = []
        lis_men.append(men_data[i])
        lis_fm.append(female_data[i])
        for k in range(len(lis_men[0])):
            if k <= 3:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    baby_list.append(values)
                    mem = []
            elif k <= 6:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    early_child_list.append(values)
                    mem = []
            elif k <= 12:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    middle_child_list.append(values)
                    mem = []
            elif k <= 19:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    teenager_list.append(values)
                    mem = []
            elif k <= 39:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    early_adult_list.append(values)
                    mem = []
            elif k <= 59:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    middle_adult_list.append(values)
                    mem = []
            elif k <= 79:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    old_age_less80_list.append(values)
                    mem = []
            elif k <= 119:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    old_age_more80_list.append(values)
                    mem = []
        for j in range(len(lis_fm[0])):
            if j <= 3:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    baby_list_fm.append(values)
                    mem = []
            elif j <= 6:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    early_child_list_fm.append(values)
                    mem = []
            elif j <= 12:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    middle_child_list_fm.append(values)
                    mem = []
            elif j <= 19:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    teenager_list_fm.append(values)
                    mem = []
            elif j <= 39:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    early_adult_list_fm.append(values)
                    mem = []
            elif j <= 59:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    middle_adult_list_fm.append(values)
                    mem = []
            elif j <= 79:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    old_age_less80_list_fm.append(values)
                    mem = []
            elif k <= 119:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    old_age_more80_list_fm.append(values)
                    mem = []
    sex_men.append((sum(baby_list)/112)*100)
    sex_men.append((sum(early_child_list)/112)*100)
    sex_men.append((sum(middle_child_list)/112)*100)
    sex_men.append((sum(teenager_list)/112)*100)
    sex_men.append((sum(early_adult_list)/112)*100)
    sex_men.append((sum(middle_adult_list)/112)*100)
    sex_men.append((sum(old_age_less80_list)/112)*100)
    sex_men.append((sum(old_age_more80_list)/112)*100)
    sex_fm.append((sum(baby_list_fm)/112)*100)
    sex_fm.append((sum(early_child_list_fm)/112)*100)
    sex_fm.append((sum(middle_child_list_fm)/112)*100)
    sex_fm.append((sum(teenager_list_fm)/112)*100)
    sex_fm.append((sum(early_adult_list_fm)/112)*100)
    sex_fm.append((sum(middle_adult_list_fm)/112)*100)
    sex_fm.append((sum(old_age_less80_list_fm)/112)*100)
    sex_fm.append((sum(old_age_more80_list_fm)/112)*100)
    
    index = np.arange(len(age))
    bar_width = 0.4

    x = index
    
    plt.barh(x, sex_men, bar_width, color='b', label='MALE')
    plt.barh(x + bar_width, sex_fm, bar_width, color='#ff3366', label='FEMALE')
    # pick graph x point and (0, 45 , 5) 45 = max 5 = jump
    plt.xticks(np.arange(0, 45, 5))
    #plt.xticks(np.arange(min(x), max(x)+0.5, 0.5))
    plt.yticks(x + bar_width, age)
    plt.ylabel('Generation')
    plt.xlabel('Death Probability (%)')
    plt.title('Death probability of each generation')
    plt.legend()

    plt.show()
#death_probability_graph_men_in_each_generation()
death_probability_graph_in_bar_graph()
#overall_death_probability_graph()
#death_probability_graph_of_male_and_female()
