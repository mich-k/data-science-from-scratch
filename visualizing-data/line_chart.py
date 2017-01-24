from matplotlib import pyplot as plt

# plot performs numerical ordering of x values*
days = [1,2,3,4,5,6,7]
steps = [7074, 11722, 8282, 6086, 8373, 8417, 10471]

plt.plot(days, steps, color='blue', marker='*', linestyle='--', label='steps')
plt.title('Weekly Steps')
plt.legend(loc=9)
plt.ylabel('Steps')
plt.xlabel('Days of the Week')
plt.show()
# plt.savefig('weekly_steps.png', format='png')
