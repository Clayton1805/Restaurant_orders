import csv


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
            c = order_obj['costumer']
            o = order_obj['order']
            if costumer == c and order == o:
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


def analyze_log(path_to_file):
    track_orders = TrackOrders()
    with open(path_to_file) as file:
        status_reader = csv.DictReader(
            file,
            fieldnames=['name', 'food', 'day_of_week']
        )
        for ob in status_reader:
            name, food, day_of_week = ob.values()
            track_orders.add_new_order(name, food, day_of_week)
    with open('data/mkt_campaign.txt', mode='w') as file:
        file.write(
            f"{track_orders.get_most_ordered_dish_per_costumer('maria')}\n"
        )
        frequency = track_orders.get_order_frequency_per_costumer(
            'arnaldo',
            'hamburguer'
        )
        file.write(
            f"{frequency}\n"
        )
        file.write(
            f"{track_orders.get_never_ordered_per_costumer('joao')}\n"
        )
        file.write(
            f"{track_orders.get_days_never_visited_per_costumer('joao')}\n"
        )
