import pandas as pd  # import pandas library; easy to read csv files
import matplotlib.pyplot as plt

female_color = "#FA0000"

df = pd.read_csv("training.csv")  # df = data frame; parameter is the Japan Data Set
fig = plt.figure(figsize=(18, 10))

print(df.shape)
print(df.count())

plt.subplot2grid((3, 4), (0, 0))
df.recovered.value_counts(normalize=True).plot(kind="bar", alpha=0.5)
plt.title("recovered")

plt.subplot2grid((3, 4), (0, 1))
df.recovered[df.gender == "male"].value_counts(normalize=True).plot(kind="bar", alpha=0.5)
plt.title("men recovered")

plt.subplot2grid((3, 4), (0, 2))
df.recovered[df.gender == "female"].value_counts(normalize=True).plot(kind="bar", alpha=0.5, color=female_color)
plt.title("women recovered")

plt.subplot2grid((3, 4), (0, 3))
df.gender[df.recovered == 1].value_counts(normalize=True).plot(kind="bar", alpha=0.5, color=['b', female_color])
plt.title("gender of recovered")

plt.subplot2grid((3,4), (1,0), colspan=4)
for x in ["male", "female"]:
    df.recovered[df.gender == x].plot(kind="kde")
plt.title("gender with respect to recovered")
plt.legend(("male", "female"))

plt.subplot2grid((3, 4), (2, 0))
df.recovered[(df.gender == "male") & (df.age < 50)].value_counts(normalize=True).plot(kind="bar", alpha=0.5)
plt.title("men younger than 50 recovered")

plt.subplot2grid((3, 4), (2, 1))
df.recovered[(df.gender == "male") & (df.age > 50)].value_counts(normalize=True).plot(kind="bar", alpha=0.5)
plt.title("men older than 50 recovered")

plt.subplot2grid((3, 4), (2, 2))
df.recovered[(df.gender == "female") & (df.age < 50)].value_counts(normalize=True).plot(kind="bar", alpha=0.5, color=female_color)
plt.title("women younger than 50 recovered")

plt.subplot2grid((3, 4), (2, 3))
df.recovered[(df.gender == "female") & (df.age > 50)].value_counts(normalize=True).plot(kind="bar", alpha=0.5, color=female_color)
plt.title("women older than 50 recovered")

plt.show()