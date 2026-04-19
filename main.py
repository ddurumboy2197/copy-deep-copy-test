import copy

# Ro'yxatni yaratamiz
original_list = [
    {"name": "Ali", "age": 25},
    {"name": "Vali", "age": 30},
    {"name": "Hasan", "age": 35}
]

# Ichma-ich ro'yxatni nusxalaymiz
deep_copy_list = copy.deepcopy(original_list)

# O'zgartirishni ko'rsatamiz
original_list[0]["age"] = 20

# Natijani chiqaramiz
print("Asl ro'yxat:")
print(original_list)
print("\nIchma-ich nusxalangan ro'yxat:")
print(deep_copy_list)
```

Kodni ishlatib ko'ring: Asl ro'yxatda "Ali"ning yoshi 20 ga o'zgartirildi, lekin ichma-ich nusxalangan ro'yxatda uning yoshi o'zgarmagan.
