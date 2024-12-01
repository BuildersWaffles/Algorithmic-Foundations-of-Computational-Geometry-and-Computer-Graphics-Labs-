import math
import matplotlib.pyplot as plt

CENTER_X, CENTER_Y = 480, 480
N = 9 
ALPHA_DEGREES = 10 * (N + 1)  
ALPHA_RADIANS = math.radians(ALPHA_DEGREES)  

cos_alpha = math.cos(ALPHA_RADIANS)
sin_alpha = math.sin(ALPHA_RADIANS)

file_path = "DS3.txt"
with open(file_path, "r") as file:
    data = file.readlines()
    
original_coords = []
rotated_coords = []

for line in data:
    try:
        x, y = map(int, line.split())
        original_coords.append((x, y))

        x_shifted, y_shifted = x - CENTER_X, y - CENTER_Y
        x_rotated = cos_alpha * x_shifted - sin_alpha * y_shifted + CENTER_X
        y_rotated = sin_alpha * x_shifted + cos_alpha * y_shifted + CENTER_Y
        rotated_coords.append((x_rotated, y_rotated))
    except ValueError:
        continue  

plt.figure(figsize=(12.8, 12.8))  
rotated_x, rotated_y = zip(*rotated_coords)
plt.scatter(rotated_x, rotated_y, s=1, c="blue")
plt.title(f"Афінне перетворення: Обертання на {ALPHA_DEGREES}°")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

output_file = "rotated_output.png"
plt.savefig(output_file, dpi=100)
plt.show()

print(f"Зображення збережено у файл {output_file}")
