# Calculating the optimal road bike seat height using a formula based on the rider's inseam length with the "LeMond Method".


def calculate_seat_height(inseam_length):
    return round(0.883 * inseam_length, 2)


try:
    inseam = float(input("Enter inseam height (cm): "))
    if 50 <= inseam <= 150:
        saddle_height = calculate_seat_height(inseam)
        print(f"Saddle height (from crank axle center): {saddle_height} cm")
    else:
        print("Invalid inseam length. Please enter a number between 50 cm and 150 cm.")
except ValueError:
    print("Invalid input. Please enter a number.")
