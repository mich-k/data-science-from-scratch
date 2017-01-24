from matplotlib import pyplot as plt

# plot performs numerical ordering of x values*
days = ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat']
steps = [7074, 11722, 8282, 6086, 8373, 8417, 10471]

x_left_scalars = [i + 0.1 for i, _ in enumerate(days)]

plt.bar(x_left_scalars, steps)
plt.title('Weekly Steps')
plt.ylabel('Steps')

#lable x axis with strings
plt.xticks([i + 0.1 for i, _ in enumerate(days)], days)
# plt.show()

plt.savefig('weekly_steps_bar.png', format='png')
