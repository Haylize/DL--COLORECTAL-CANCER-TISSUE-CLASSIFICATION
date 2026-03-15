# Deep Learning for Histopathology Image Classification (PathMNIST)

## Overview

This project explores several deep learning architectures for **histopathology image classification** using the **PathMNIST dataset**, part of the MedMNIST benchmark.

The goal is to compare different model families and analyze their performance, training behavior, and generalization ability in a medical imaging context.

The following architectures are implemented and evaluated:

- Multilayer Perceptron (MLP)
- Convolutional Neural Network (CNN)
- ResNet-18 with transfer learning
- Vision Transformer (ViT)

# Dataset

The experiments use **PathMNIST**, a dataset derived from colorectal cancer histology images.

Dataset characteristics:

- Image size: **28 × 28**
- Color channels: **RGB**
- Number of classes: **9**
- Training samples: **~90,000**
- Validation samples: **10,000**
- Test samples: **~7,000**

Tissue classes:

- Adipose  
- Background  
- Debris  
- Lymphocytes  
- Mucus  
- Smooth Muscle  
- Normal Mucosa  
- Cancer Stroma  
- Tumor Epithelium  

# Data Preprocessing

Images are normalized using statistics computed on the **training set**.

```python
PATHMNIST_MEAN = [0.7405, 0.5330, 0.7058]
PATHMNIST_STD  = [0.1237, 0.1768, 0.1244]
```

Normalization improves training stability by centering and scaling the input features.

Some experiments also use data augmentation, including:
- Random horizontal flips
- Random rotations

These transformations increase data diversity and help improve generalization.

# Models

# Multilayer Perceptron (MLP)
The MLP serves as a baseline model.
Each image is flattened into a vector before being passed through fully connected layers.

Characteristics:
- Fully connected layers
- ReLU activation
- Dropout regularization

Limitations:
- No spatial inductive bias
- Cannot capture local image structures

# Convolutional Neural Network (CNN)

The CNN is trained from scratch and uses convolutional filters to extract spatial features.

Architecture:
- Convolutional blocks
- Batch normalization
- Max pooling
- Dropout
- Fully connected classifier

CNNs are well suited for image classification due to their ability to learn hierarchical visual features.

# ResNet-18 (Transfer Learning)

ResNet-18 is initialized with ImageNet pretrained weights and fine-tuned on PathMNIST.

Advantages:
- Strong feature extractor
- Faster convergence
- Better performance with limited data
- The final classification layer is adapted for the 9 PathMNIST classes.

# Vision Transformer (ViT)

The Vision Transformer processes images as sequences of patches using self-attention.

Architecture:
- Patch embedding
- Transformer encoder layers
- Multi-head self-attention
- MLP classification head

ViTs can capture global dependencies but generally require larger datasets to perform well.

# Training Setup

All models are trained using:
- Cross-entropy loss
- Adam optimizer
- Mini-batch gradient descent

Training configuration:
- Batch size: 128
- Epochs: 40
- Input resolution: 28×28 (224×224 for ResNet)

# Results

| Model |	Test Accuracy |
|--------|----------------|
| MLP | ~61.9% |
| CNN (with augmentation) | ~84.9% |
| ResNet-18 (fine-tuned) | ~92.7% |
| Vision Transformer | ~81.3% |

ResNet-18 achieved the best performance, demonstrating the effectiveness of transfer learning in medical imaging tasks.

# Analysis

Key observations from the experiments:
- Transfer learning significantly improves performance compared to training from scratch.
- CNNs provide strong results thanks to their spatial inductive bias.
- Vision Transformers underperform when trained from scratch on relatively small datasets.
- Data augmentation helps reduce overfitting and improves generalization.

Confusion matrix analysis reveals that some tissue types remain difficult to distinguish, especially Cancer Stroma and Smooth Muscle, which share similar visual patterns.

# Ethical Considerations

AI-based cancer tissue classification raises several important concerns:
- False negatives could delay cancer diagnosis.
- Dataset bias may reduce performance on data from other hospitals or scanners.
- Class imbalance may affect rare tissue types.
- Interpretability is required for clinical trust and validation.

AI systems should therefore be used as decision-support tools rather than replacements for expert pathologists.

# Technologies Used

- Python
- PyTorch
- NumPy
- Matplotlib
- Scikit-learn

# Author

Élise PRIGENT  
Édouard LACROIX
