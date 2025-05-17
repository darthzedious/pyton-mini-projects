import matplotlib.pyplot as plt
import os

# years and data
years = [2019, 2020, 2021, 2022, 2023, 2024]
portugal_current_account = [11.3, 15.3, 20.9, 15.4, 15, 16.7]
# spain_current_account = [72.7, 71.7, 73.0, 74.6, 75.3, 75.8]

# save path
save_dir = "charts"
os.makedirs(save_dir, exist_ok=True)  # Създава директория, ако не съществува
save_path = os.path.join(save_dir, "5.3_portugal.png")

# create chart
plt.figure(figsize=(10, 5))
plt.plot(years, portugal_current_account, marker='o', color='green', label='Португалия')
# plt.plot(years, spain_current_account, marker='s', color='blue', label='ЕС')

plt.title("Коефициент на младежка безработица (%) (2019–2024)")
# plt.title("Инфлация (%) (2019–2024)")
# plt.title("Търговски баланс (% от БВП): Португалия и Испания (2019–2023)")
# plt.title("Търговски баланс (% от БВП): Португалия (2019–2023)")

plt.xlabel("Година")
plt.ylabel("Коефициент на младежка безработица (%)")

plt.xticks(years)
plt.grid(True)
plt.legend()
plt.tight_layout()

# save as png
plt.savefig(save_path, dpi=300)  # save with high resolution
plt.show()

print(f"Chart saved at: {save_path}")
