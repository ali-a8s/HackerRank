num_test_cases = int(input())

for _ in range(num_test_cases):
    try:
        a, b = map(int, input().split())
        result = a // b
        print(result)
    except Exception as error:
        print(f"Error Code: {error}")