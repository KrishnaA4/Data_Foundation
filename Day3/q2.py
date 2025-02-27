users = [("Alice", 25, "New York"), ("Bob", 17, "Los Angeles"), ("Charlie", 30,
"Chicago")]

ans = {t[0]:t[1] for t in users if t[1]>18}

print(ans)