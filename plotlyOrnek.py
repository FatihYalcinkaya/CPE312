import plotly.express as px

fig = px.line(x=[1, 2, 3], y=[1, 2, 3])
fig.show()


df = px.data.iris()
fig = px.line(df, x="species", y="petal_width")
fig.show()



df = px.data.iris()
fig = px.bar(df, x="sepal_width", y="sepal_length")
fig.show()
df = px.data.iris()
fig = px.histogram(df, x="sepal_length", y="petal_width")
fig.show()

df = px.data.iris()

fig = px.scatter(df, x="species", y="petal_width")
fig.show()

df = px.data.tips()
fig = px.pie(df, values="total_bill", names="day")
fig.show()
