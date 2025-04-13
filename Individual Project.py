import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Days of the week
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# sample sales data
groceries_sales = np.random.randint(500, 1500, size=7)
electronics_sales = np.random.randint(200, 1000, size=7)
clothing_sales = np.random.randint(300, 900, size=7)
cash_payments = np.random.randint(50, 100, size=7)
card_payments = np.random.randint(30, 80, size=7)
upi_payments = np.random.randint(20, 70, size=7)

#  DataFrame
df = pd.DataFrame({
    'Day': days,
    'Groceries': groceries_sales,
    'Electronics': electronics_sales,
    'Clothing': clothing_sales,
    'Cash': cash_payments,
    'Card': card_payments,
    'UPI': upi_payments
})

# Line plot for product sales
plt.plot(df['Day'], df['Groceries'], label='Groceries', color='green', marker='o')
plt.plot(df['Day'], df['Electronics'], label='Electronics', color='blue', marker='s')
plt.plot(df['Day'], df['Clothing'], label='Clothing', color='red', marker='^')
plt.title('Weekly Sales by Product Category')
plt.xlabel('Day')
plt.ylabel('Units Sold')
plt.legend()
plt.tight_layout()
plt.show()


# Bar plot for overall weekly payment method usage
total_cash = df['Cash'].sum()
total_card = df['Card'].sum()
total_upi = df['UPI'].sum()


plt.bar(['Cash', 'Card', 'UPI'], [total_cash, total_card, total_upi], color=['orange', 'gray', 'pink'])
plt.title('Total Weekly Payment Method Usage')
plt.xlabel('Payment Method')
plt.ylabel('Number of Transactions')
plt.tight_layout()
plt.show()
