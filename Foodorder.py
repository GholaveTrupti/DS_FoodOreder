# Food Delivery Order Processing

class Node:
    def __init__(self, order_id, food):
        self.order_id = order_id
        self.food = food
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_order(self, order_id, food):
        new_node = Node(order_id, food)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print("Order added successfully!")

    def process_order(self):
        if self.front is None:
            print("No orders to process.")
            return None

        order = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print("Order processed:", order.order_id, "-", order.food)
        return order

    def display(self):
        if self.front is None:
            print("No pending orders.")
            return

        temp = self.front
        print("\nPending Orders:")

        while temp:
            print(temp.order_id, "-", temp.food)
            temp = temp.next


# Stack Orders
class Stack:
    def __init__(self):
        self.top = None

    def add_completed(self, order):
        order.next = self.top
        self.top = order

    def display(self):
        if self.top is None:
            print("No completed orders.")
            return

        temp = self.top
        print("\nCompleted Orders:")

        while temp:
            print(temp.order_id, "-", temp.food)
            temp = temp.next

orders = Queue()
completed = Stack()

while True:

    print("\n===== FOOD DELIVERY SYSTEM =====")
    print("1. Place Order")
    print("2. Process Order")
    print("3. Show Pending Orders")
    print("4. Show Completed Orders")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        order_id = int(input("Enter Order ID: "))
        food = input("Enter Food Name: ")

        orders.add_order(order_id, food)

    elif choice == 2:
        order = orders.process_order()

        if order:
            completed.add_completed(order)

    elif choice == 3:
        orders.display()

    elif choice == 4:
        completed.display()

    elif choice == 5:
        print("Thank you for using Food Delivery System!")
        break

    else:
        print("Invalid choice!")
