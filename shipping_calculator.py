def calculate_shipping_cost(weight, distance):
    base = 10.0
    cost = base + 0.5 * weight + 0.15 * distance
    return round(cost, 2)

def estimate_delivery_time(distance):
    speed = 40  # km/h
    time = distance / speed
    return round(time, 2)

if __name__ == "__main__":
    w = float(input("Enter package weight in kg: "))
    d = float(input("Enter shipping distance in km: "))
    cost = calculate_shipping_cost(w, d)
    time = estimate_delivery_time(d)
    print(f"Shipping cost: {cost}€")
    print(f"Estimated delivery time: {time} hours")
