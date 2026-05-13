# Mushroom-Image-Text-Retrieval
This project implements a specialized text-to-image retrieval system for mushrooms by fine-tuning CLIP (ViT-B/32) using LoRA (Low-Rank Adaptation). The system enables precise semantic search across a multilingual dataset (English and Vietnamese) by aligning mycological descriptions with visual features.

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

- Run dataset_to_csv.py and get output: 2 file csv
  
  - images.csv: Mapping between images and species: imagePath, binomialNomenclature
    
  - mushrooms.csv: Structured metadata for each species (converted from JSON

# Train Pipeline
All experiments and implementations in this notebook were conducted using Kaggle Notebook.
## 1. Data Engineering & Augmentation
- Prompt Construction: Raw metadata fields—including scientific names, habitats, edibility, and morphological features (cap, gills, stem, spores)—are synthesized into descriptive natural language captions.
- Back-Translation: To increase linguistic diversity without losing scientific accuracy, 30% of English prompts undergo **EN → FR → EN** back-translation, outperforming standard random-deletion methods for technical terms.
- Visual Augmentation: Standard image transformations (crop, flip, jitter, and blur) are applied to improve the model's robustness against real-world photo variations.

## 2. LoRA Fine-Tuning
- Architecture: LoRA adapters ($r=16, \alpha=32$) are integrated into all 12 transformer blocks of the **CLIP Text Encoder**, specifically targeting the attention output and MLP layers.
- Training Strategy: The Image Encoder remains frozen to preserve CLIP's foundational visual knowledge. The Text Encoder is fine-tuned for 12 epochs using a -Symmetric Contrastive Loss with a temperature of 0.07.
- Optimization: Training utilizes the AdamW optimizer ($\eta = 10^{-5}$) and mixed-precision (FP16) to ensure memory efficiency and faster convergence.

## 3. Vector Indexing & Retrieval
- Embedding Generation: The fine-tuned model encodes the entire image library into a high-dimensional vector space.
- FAISS Indexing: Embeddings are L2-normalized and stored in a **FAISS IndexFlatIP** structure. This allows the Inner Product calculation to effectively serve as a high-speed cosine similarity search.
- Query Execution: User queries are processed through the LoRA-enhanced Text Encoder to retrieve the Top-K most relevant images in real-time.

## 4. Evaluation Framework
Retrieval performance is rigorously validated at $k = \{1, 5, 10, 50, 100, 1000\}$ using:
- Precision@k & Recall@k: Measuring the accuracy and the hit rate of species retrieval.
- mAP (Mean Average Precision): Evaluating the overall quality of the ranked results.
- mRR (Mean Reciprocal Rank): Assessing how quickly the correct species appears in the retrieved list.

# Tech Stack
- Core Frameworks: PyTorch, OpenAI-CLIP, PEFT (LoRA)
- Vector Search: FAISS (GPU-accelerated)
- NLP Tools: Hugging Face Transformers (for Back-translation augmentation)

# Collaborator
- [Kieu Hong Phong](https://github.com/haiphong-0132)
