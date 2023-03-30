from name_function import get_formatted_name
while True:
    first = input("Please give me a first name")
    last = input("Please give me a last name")
    if first == 'q' or last == 'q':
        break

    formatted_name = get_formatted_name(first,last)
    print(f"\tNeatly formatted name:{formatted_name}")