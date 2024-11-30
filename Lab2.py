import matplotlib.pyplot as plt

file_path = "DS3.txt"
with open(file_path, "r") as file:
    data = file.readlines()

x_coords = []
y_coords = []
for line in data:
    try:
        x, y = map(int, line.split())
        x_coords.append(x)
        y_coords.append(y)
    except ValueError:
        continue

plt.figure(figsize=(12.8, 7.2)) 
plt.scatter(x_coords, y_coords, s=1, c="blue")  
plt.title("Visualization of points from the dataset")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

output_file = "output.png"
plt.savefig(output_file, dpi=100)
plt.show()

print(f"Image was saved in file {output_file}")
