import os
import json
import csv

base_dir = "Dataset"
mushroom_csv = "mushrooms.csv"
image_csv = "images.csv"

mushroom_rows = []
image_rows = []

for species_dir in os.listdir(base_dir):
    species_path = os.path.join(base_dir, species_dir)
    metadata_path = os.path.join(species_path, "metadata.json")
    image_dir = os.path.join(species_path, "Images")
    
    if not os.path.isfile(metadata_path):
        continue
    
    print(metadata_path)
    with open(metadata_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    images = []
    if os.path.isdir(image_dir):
        for img in os.listdir(image_dir):
            if img.lower().endswith((".jpg", ".jpeg", ".png")):
                image_path = os.path.join(image_dir, img)
                images.append(image_path)
                image_rows.append({
                    "imagePath": image_path,
                    "binomialNomenclature": meta.get("binomialNomenclature")
                })

    row = {
        "binomialNomenclature": meta.get("binomialNomenclature"),
        "commonName_en": ", ".join(meta.get("commonNames", {}).get("en", [])),
        "commonName_vi": ", ".join(meta.get("commonNames", {}).get("vi", [])),
        "habitat": meta.get("habitat"),
        "shortDescription": meta.get("shortDescription"),
        "edibility": meta.get("edibility"),
        "isPoisonous": meta.get("isPoisonous"),
        "benefitsOrToxicity": meta.get("benefitsOrToxicity"),
        "cap": meta.get("identification", {}).get("cap"),
        "gills": meta.get("identification", {}).get("gills"),
        "stem": meta.get("identification", {}).get("stem"),
        "flesh": meta.get("identification", {}).get("flesh"),
        "sporePrint": meta.get("identification", {}).get("sporePrint"),
        "taste": meta.get("identification", {}).get("taste"),
        "odor": meta.get("identification", {}).get("odor"),
        "microscopicFeatures": meta.get("identification", {}).get("microscopicFeatures"),
        "lookAlikes": "; ".join([d.get("binomialNomenclature") for d in meta.get("lookAlikes", [])]),
        "medicinalProperties": meta.get("medicinalProperties"),
        "note": meta.get("note"),
        "numImages": len(images)
    }

    mushroom_rows.append(row)

#Ghi mushrooms.csv 
with open(mushroom_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=mushroom_rows[0].keys())
    writer.writeheader()
    writer.writerows(mushroom_rows)

#Ghi images.csv 
with open(image_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["imagePath", "binomialNomenclature"])
    writer.writeheader()
    writer.writerows(image_rows)

print(f"Created {mushroom_csv} and {image_csv}")