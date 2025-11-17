import time

inicio = time.time()

for i in range(100):
    print(f"{i} - ", end="")

final = time.time()

# print(f"He tardado {round(final - inicio, 1)} segundos.")
print(f"\nHe tardado {round(final - inicio, 1)}, segundos.")



# inicio = time.time()

# time.sleep(2)
# print(time.time())

# print(f"He tardado {round(time.time() - inicio, 1)} segundos.")
# print(f"He tardado {round(time.time() - inicio) segundos.")

time.sleep(2)
print(time.time())