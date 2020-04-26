import pandas as pd  # import pandas library; easy to read csv files
import matplotlib.pyplot as plt

df = pd.read_csv("training.csv")  # df = data frame; parameter is the Japan Data Set
fig = plt.figure(figsize=(18, 6))

print(df.shape)
print(df.count())

# the following is a bar graph of those that recovered or not
plt.subplot2grid((2, 3), (0, 0))
df.recovered.value_counts(normalize=True).plot(kind="bar", alpha=0.5)
plt.title("recovered")

# the following is a plot grid of those that recovered with respects to their age
plt.subplot2grid((2, 3), (0, 1))
plt.scatter(df.recovered, df.age, alpha=0.1)
plt.title("age with respects to recovered")

# the following is a plot grid of those that survived based off of gender
plt.subplot2grid((2, 3), (0, 2))
df.gender.value_counts(normalize=True).plot(kind="bar", alpha=0.5)
plt.title("gender")

#idk why i can't get this graph to work
plt.subplot2grid((2,3), (1,0), colspan=2)
for x in ["male", "female"]:
    df.age[df.gender == x].plot(kind="kde")
plt.title("gender with respect to age")
plt.legend(("male", "female"))

#figure out how to break out symptoms

#decide if we're going to use location as a label, then create a chart

plt.show()
