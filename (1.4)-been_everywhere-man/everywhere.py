u = int(input())

output_arr = []

for i in range(u):
    city_arr = []
    num_cities = int(input())
    for i in range(num_cities):
        city_input = input()
        if city_input not in city_arr:
            city_arr.append(city_input)
    output_arr.append(len(city_arr))
    
for i in output_arr:
    print(i)