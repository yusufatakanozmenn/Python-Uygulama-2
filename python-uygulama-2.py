import math

# Örnek Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8)]  # Örnek nokta listesi

# Öklid Mesafesi İçin Fonksiyon Tanımlama
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mesafelerin Hesaplanması ve distances listesine ekleme
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
min_distance = min(distances)

# Sonucun Yazdırılması
print("Minimum mesafe:", min_distance)
