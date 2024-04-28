import matplotlib.pyplot as plt

# Data for sales of different products over a month
products = ['Product A', 'Product B', 'Product C']
sales = [350, 500, 400]  # Sales data for each product

# Plot the bar chart
plt.bar(products, sales, color=['red', 'green', 'blue'])

# Add labels and title
plt.xlabel('Products')
plt.ylabel('Sales (in units)')
plt.title('Monthly Sales of Products')

# Show plot
plt.show()
