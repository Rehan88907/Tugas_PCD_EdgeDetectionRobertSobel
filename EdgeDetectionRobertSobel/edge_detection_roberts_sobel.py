import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt
import os

# Gambar input JPG
img_path = "contoh.jpg"

if not os.path.exists(img_path):
    print(f"ERROR: File '{img_path}' tidak ditemukan!")
    exit()

print("Membaca gambar:", img_path)

# Load gambar
img = imageio.imread(img_path)
gray = np.dot(img[..., :3], [0.299, 0.587, 0.114])

# Roberts Operator
roberts_x = np.array([[1, 0], [0, -1]])
roberts_y = np.array([[0, 1], [-1, 0]])

def apply_filter(image, kernel):
    h, w = image.shape
    kh, kw = kernel.shape
    output = np.zeros((h - kh + 1, w - kw + 1))
    for i in range(h - kh + 1):
        for j in range(w - kw + 1):
            output[i, j] = np.sum(image[i:i+kh, j:j+kw] * kernel)
    return output

edge_roberts = np.sqrt(apply_filter(gray, roberts_x)**2 + apply_filter(gray, roberts_y)**2)

# Sobel Operator
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

edge_sobel = np.sqrt(apply_filter(gray, sobel_x)**2 + apply_filter(gray, sobel_y)**2)

# Simpan hasil sebagai file PNG
plt.imsave("output_grayscale.png", gray, cmap="gray")
plt.imsave("output_roberts.png", edge_roberts, cmap="gray")
plt.imsave("output_sobel.png", edge_sobel, cmap="gray")

# Gabungkan dalam satu gambar
plt.figure(figsize=(12, 5))

plt.subplot(1,3,1)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(edge_roberts, cmap="gray")
plt.title("Roberts")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(edge_sobel, cmap="gray")
plt.title("Sobel")
plt.axis("off")

plt.savefig("output_all.png")
plt.close()

print("\n=== SELESAI ===")
print("File telah dibuat:")
print(" - output_grayscale.png")
print(" - output_roberts.png")
print(" - output_sobel.png")
print(" - output_all.png\n")
