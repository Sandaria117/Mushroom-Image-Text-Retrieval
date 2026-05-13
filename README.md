# Mushroom-Image-Text-Retrieval
Finetune CLIP with LoRA for mushroom image–text retrieval
- ưewe

# Dataset Creation
The dataset is built for a **mushroom image–text retrieval** task, including:
- Mushroom images  
- Metadata describing each species

The collected dataset contains 3,000+ images of 33 different mushroom species: [Dataset](https://www.kaggle.com/datasets/sandaria/mushroom/data)

## Data Sources

- [Images](https://www.inaturalist.org/): Download by following these [GitHub](https://github.com/Camponotus-vagus/iNaturalist-Image-Downloader) instructions 

- [Metadata](https://ultimate-mushroom.com/):Includes scientific names, descriptions, habitat, identification features, etc.

## Data Processing

- Data is organized per species:

<img width="603" height="284" alt="image" src="https://github.com/user-attachments/assets/bdb77bc7-e84c-4e15-bb01-8e121e7fb74e" />

### `images.csv`
Mapping between images and species:
- `imagePath`  
- `binomialNomenclature`  

### `mushrooms.csv`
Structured metadata for each species (converted from JSON)
