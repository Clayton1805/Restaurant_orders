class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({
            'costumer': costumer,
            'order': order,
            'day': day,
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        count_order = dict()
        for order_obj in self.orders:
            if order_obj['costumer'] == costumer:
                get_key = count_order.get(order_obj['order'], 0)
                count_order[order_obj['order']] = get_key + 1
        return max(count_order, key=count_order.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        qnt = 0
        for order_obj in self.orders:
            costumer, order = order_obj.values()
            if costumer == costumer and order == order:
                qnt += 1
        return qnt

    def get_never_ordered_per_costumer(self, costumer):
        order = set()
        order_costumer = set()
        for order_obj in self.orders:
            order.add(order_obj['order'])
            if order_obj['costumer'] == costumer:
                order_costumer.add(order_obj['order'])
        return order.difference(order_costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        order = set()
        order_costumer = set()
        for order_obj in self.orders:
            order.add(order_obj['day'])
            if order_obj['costumer'] == costumer:
                order_costumer.add(order_obj['day'])
        return order.difference(order_costumer)

    def get_busiest_day(self):
        count_day = dict()
        for order_obj in self.orders:
            day = order_obj['day']
            count_day[day] = count_day.get(day, 0) + 1
        return max(count_day, key=count_day.get)

    def get_least_busy_day(self):
        count_day = dict()
        for order_obj in self.orders:
            day = order_obj['day']
            count_day[day] = count_day.get(day, 0) + 1
        return min(count_day, key=count_day.get)
