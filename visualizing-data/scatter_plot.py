from matplotlib import pyplot as plt

steps = [7074, 11722, 8282, 6086, 8373, 8417, 10471]
hours_slept = [4, 9, 7, 5, 7, 8, 9]
labels = ['su', 'm', 'tu', 'w', 'th', 'f', 'sa']

plt.scatter(steps, hours_slept)

#lable each pt
# for label, steps, hours_slept in zip(labels, steps, hours_slept):
#     plt.annotate(
#         label,
#         xy=(steps, hours_slept),
#         xytext=(5, -5),
#         textcoords='offset points'
#     )

plt.title('Steps vs. Hours Slept')
plt.xlabel('Steps')
plt.ylabel('Hours Slept')
plt.show()
# plt.savefig('weekly_steps_vs_hours_slept.png', format='png')
