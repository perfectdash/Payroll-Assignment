import tkinter as tk

def calculate_bill():
    quantity = int(quantity_entry.get())
    price = float(price_entry.get())
    
    total = quantity * price
    total_label.config(text="Total Bill: $ {:.2f}".format(total))

# Create the main window
root = tk.Tk()
root.title("Bill Calculator")

# Create labels and entries for quantity and price
quantity_label = tk.Label(root, text="Quantity:")
quantity_label.grid(row=0, column=0, padx=10, pady=5)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=0, column=1, padx=10, pady=5)

price_label = tk.Label(root, text="Price per item:")
price_label.grid(row=1, column=0, padx=10, pady=5)
price_entry = tk.Entry(root)
price_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a button to calculate the bill
calculate_button = tk.Button(root, text="Calculate", command=calculate_bill)
calculate_button.grid(row=2, columnspan=2, padx=10, pady=5)

# Create a label to display the total bill
total_label = tk.Label(root, text="")
total_label.grid(row=3, columnspan=2, padx=10, pady=5)

# Run the main event loop
root.mainloop()
