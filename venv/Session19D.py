from matplotlib import pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

# Scatter Graph

# tips = sns.load_dataset("tips")
# print(tips)

# sns.relplot(x="total_bill",y="tip", data=tips)
# sns.relplot(x="total_bill", y="tip", hue="time", data=tips)

# plt.show()

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")

# Plot the responses for different events and regions
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)

plt.show()