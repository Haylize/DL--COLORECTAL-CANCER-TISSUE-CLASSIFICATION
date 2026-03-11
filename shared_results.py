# shared_results.py
# Static constants are defined here.
# All other values are computed and written by their respective notebooks.

CLASS_NAMES = [
    'Adipose', 'Background', 'Debris', 'Lymphocytes', 'Mucus',
    'Smooth Muscle', 'Normal Mucosa', 'Cancer Stroma', 'Tumor Epithelium'
]
BATCH_SIZE = 256

# ── Written by Part 1 ──────────────────────────────────────────────────────
PATHMNIST_MEAN = None
PATHMNIST_STD  = None

# ── Written by Part 2 ──────────────────────────────────────────────────────
mlp_test_acc = None

# ── Written by Part 3 ──────────────────────────────────────────────────────
cnn_params         = None
cnn_noaug_test_acc = None
cnn_aug_test_acc   = None

# ── Written by Part 4 ──────────────────────────────────────────────────────
resnet_frozen_test_acc = None
resnet_full_test_acc   = None

# ── Written by Part 5 ──────────────────────────────────────────────────────
vit_test_acc = None
