no1 = 45
no2 = 34
no3 = 23

# ans = "no1 is gretter" if no1 > no2 else "no2 is gretter" 
# print("no1 is gretter") if no1 > no2 else print("no2 is gretter")
# ans = no1 if no1 > no2 else no2
# print(f"{ans} is gretter")

# ans = no1 if no1 > no2 and no1 > no3 else no2 if no2 > no3 and no2 > no1 else no3 
# print(f"{ans} is gretter")

ans = no3 if (no1 if no1 > no2 else no2) < no3 else (no1 if no1 > no2 else no2)
