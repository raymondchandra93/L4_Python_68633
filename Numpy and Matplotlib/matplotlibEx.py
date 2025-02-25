import matplotlib.pyplot as plt

# -- 1 Basic Plot --

x = [50, 60, 70, 80, 90]
y = [2, 5, 8, 10, 12]

# plt.plot(x, y)

# -- 2 Adding Lables and Title
plt.xlabel("Temperature of the Day")
plt.ylabel("Number of Ice Cream Sold")
plt.title("Relation between temperature and ice cream sold")

# -- 3 Bar Chart
# plt.bar(x, y)

# -- 4 Scatter Plot
# plt.scatter(x, y)

# -- 5 Histogram
# data = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 7,7]
# plt.hist(data)

# -- 6 Customizing Plot
# plt.plot(x, y, color='red', linestyle='--', marker='o')
# plt.grid(True)

# -- 7 Multiple Plots
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# plt.plot(x1, y1, label="New York")
# plt.plot(x1, y2, label="Washington")

# plt.legend()

# -- 8 Subplot

plt.subplot(1, 2, 1)        # 1 row, 2 columns, 1st plot
plt.plot(x1, y1)
plt.title("First Plot")

plt.subplot(1, 2, 2)        # 1 row, 2 columns, 2nd plot
plt.plot(x1, y2)
plt.title("Second Plot")

# plt.tight_layout()        # elimintaing the extra space in the middle

# Show
# plt.show()

# -- 9 Saving plot
plt.savefig("IceCreamSales.png")