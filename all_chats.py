from matplotlib import pyplot as plt
def get_data(Month):
    month_totals = [[597, 87, 16, 672, 587, 599, 498],
                    [509, 67, 17, 611, 579, 535, 578],
                    [535, 86, 17, 563, 559, 499, 475],
                    [482, 85, 13, 430, 578, 575, 471]]

    month_dates = [['5/1', '5/2', '5/3', '5/4', '5/5', '5/6', '5/7'],
                   ['5/8', '5/9', '5/10', '5/11', '5/12', '5/13', '5/14'],
                   ['5/15', '5/16', '5/17', '5/18', '5/19', '5/20', '5/21'],
                   ['5/22', '5/23', '5/24', '5/25', '5/26', '5/27', '5/28']]

    weeks = [f'{month_dates[0][0]} to {month_dates[0][-1]}',
             f'{month_dates[1][0]} to {month_dates[1][-1]}',
             f'{month_dates[2][0]} to {month_dates[2][-1]}',
             f'{month_dates[3][0]} to {month_dates[3][-1]}']



    months_missed = [[34, 28,  6, 46, 23, 6, 51],
                     [13, 30, 1, 40, 39, 142, 6],
                     [58, 6, 0, 194, 33, 35, 145],
                     [29, 23, 4, 85, 32, 36, 72]]

    week_totals = [sum(month_totals[0]), sum(month_totals[1]), sum(month_totals[2]), sum(month_totals[3])]
    #week_missed_totals = [sum(months_missed[0]), sum(months_missed[1]), sum(months_missed[2]), sum(months_missed[3])]


    plt.close('all')
    plt.figure(figsize=(13, 10))

    plt.subplot(3, 2, 1,)
    plt.plot(month_dates[0], month_totals[0], color='blue', marker='s')
    plt.plot(month_dates[0], months_missed[0], color='red', marker='s')
    plt.title(f'Chats from {month_dates[0][0]} to {month_dates[0][-1]}')
    plt.legend(["Total chats", "Missed chats"], loc='best')


    plt.subplot(3, 2, 2)
    plt.plot(month_dates[1], month_totals[1], color='blue', marker='s')
    plt.plot(month_dates[1], months_missed[1], color='red', marker='s')
    plt.title(f'Chats from {month_dates[1][0]} to {month_dates[1][-1]}')

    plt.subplot(3, 2, 3)
    plt.plot(month_dates[2], month_totals[2], color='blue', marker='s')
    plt.plot(month_dates[2], months_missed[2], color='red', marker='s')
    plt.title(f'Chats from {month_dates[2][0]} to {month_dates[2][-1]}')

    plt.subplot(3, 2, 4)
    plt.plot(month_dates[3], month_totals[3], color='blue', marker='s')
    plt.plot(month_dates[3], months_missed[3], color='red', marker='s')
    plt.title(f'Chats from {month_dates[3][0]} to {month_dates[3][-1]}')

    plt.subplot(3, 1, 3)
    plt.plot(weeks, week_totals, color='blue', marker='s')
    #plt.plot(weeks, week_missed_totals, color='red', marker='s')
    plt.legend(["Total chats"], loc='best')
    plt.title('Chat totals by weeks')

    plt.subplots_adjust(hspace=0.3)
    plt.savefig(f'Month Totals/{Month}_chats.png')
    plt.show()


get_data("May")
