from collections import Counter
import operator

class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []
    
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append({ "customer": customer, "order": order, "day": day })

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = []
        for order in self.orders:
            if order["customer"] == customer:
                customer_orders.append(order["order"])
        new_dict = Counter(customer_orders)
        most_ordered = max(new_dict.items(), key=operator.itemgetter(1))[0]
        return most_ordered

    def get_never_ordered_per_customer(self, customer):
        menu = set(item["order"] for item in self.orders)
        customer_orders = []
        for order in self.orders:
            if order["customer"] == customer:
                customer_orders.append(order["order"])
        new_dict = set(customer_orders)
        return menu - new_dict


    def get_days_never_visited_per_customer(self, customer):
        menu = set(item["day"] for item in self.orders)
        customer_day = []
        for order in self.orders:
            if order["customer"] == customer:
                customer_day.append(order["day"])
        new_dict = set(customer_day)
        return menu - new_dict

    def get_busiest_day(self):
        busy = Counter(item["day"] for item in self.orders)
        busiest_day = max(busy.items(), key=operator.itemgetter(1))[0]
        return busiest_day
        # customer_day = []
        # for order in self.orders:
        #     if order["customer"] == customer:
        #         customer_day.append(order["day"])
        # new_dict = set(customer_day)
        # return menu - new_dict

    def get_least_busy_day(self):
        busy = Counter(item["day"] for item in self.orders)
        least_busy_day = min(busy.items(), key=operator.itemgetter(1))[0]
        return least_busy_day
