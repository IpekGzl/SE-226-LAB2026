import geometry_utils as gu

operations = {
    "circle_area": gu.circle_area,
    "circle_perimeter": gu.circle_perimeter,
    "rectangle_area": gu.rectangle_area,
    "rectangle_perimeter": gu.rectangle_perimeter,
    "triangle_area": gu.triangle_area
}

# sürekli çalışsın ki tüm sample outputları al
while True:
    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: _area, _perimeter (e.g., circle_area)")

    operation = input("Enter the operation you want to perform: ")

    try:
        if operation.startswith("circle"):
            r = float(input("Enter radius: "))
            result = operations[operation](r)

        elif operation.startswith("rectangle"):
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            result = operations[operation](w, h)

        elif operation.startswith("triangle"):
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            result = operations[operation](b, h)

        else:
            print("Invalid operation")
            continue

        print(f"Result: {round(result, 2)}")

    except ValueError as e:
        print(f"Input Error: {e}")
