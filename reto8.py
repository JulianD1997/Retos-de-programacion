def decimal_to_binary(decimal):
    if decimal == 1:
        return f"{decimal%2}0"
    if decimal == 2 or decimal == 3 :
        return f"{decimal % 2}1"
    if decimal != 1 and decimal != 0:
        return f"{decimal % 2}" + f"{decimal_to_binary(decimal//2)}"

if __name__ == "__main__":
    print(f"10 a binario {decimal_to_binary(10)[::-1]}")
    print(f"44 a binario {decimal_to_binary(44)[::-1]}")
    print(f"77 a binario {decimal_to_binary(77)[::-1]}")
    print(f"450 a binario {decimal_to_binary(450)[::-1]}")
