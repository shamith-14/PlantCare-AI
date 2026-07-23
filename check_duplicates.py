import os

train_files = set()
val_files = set()

for root, _, files in os.walk("dataset/train"):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            train_files.add(file)

for root, _, files in os.walk("dataset/val"):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            val_files.add(file)

duplicates = train_files.intersection(val_files)

print(f"Train images: {len(train_files)}")
print(f"Validation images: {len(val_files)}")
print(f"Duplicate filenames: {len(duplicates)}")

if duplicates:
    print("\nSome duplicate filenames:")
    for file in list(duplicates)[:20]:
        print(file)
else:
    print("\n✅ No duplicate filenames found.")