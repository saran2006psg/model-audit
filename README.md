# ModelAudit

ModelAudit is an open-source Python toolkit designed to help machine learning developers thoroughly evaluate, diagnose, and audit trained ML models beyond standard aggregate metrics.

---

## Current Development Phase: Phase 1 (Baseline Package)

> **Important Notice:** ModelAudit is currently in **Phase 1**. This phase establishes the baseline package architecture, configuration, public API, and test suite. **Actual machine learning evaluation algorithms and diagnostic calculations are not implemented yet.**

---

## Installation

For local development, clone the repository and install the package in editable mode along with development dependencies:

```bash
# 1. Create a virtual environment
python -m venv .venv

# 2. Activate the virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (CMD):
.venv\Scripts\activate.bat
# Linux / macOS:
source .venv/bin/activate

# 3. Install in editable mode with development dependencies
pip install -e ".[dev]"
```

---

## Basic Usage

Expose and run the baseline evaluator:

```python
from modelaudit import ModelEvaluator

# Initialize the baseline evaluator
evaluator = ModelEvaluator()

# Run baseline verification
result = evaluator.run()

print(result)
```

### Expected Output

```text
ModelAudit
----------
Evaluation engine initialized successfully.
Status: Ready
```

---

## Running Tests

ModelAudit uses `pytest` for testing:

```bash
python -m pytest -v
```

---

## Current Limitations

- **No ML computation**: Phase 1 is strictly a baseline skeleton verifying packaging, imports, and execution.
- **Model-agnostic baseline**: The `ModelEvaluator` does not yet accept model weights, datasets, or predictions.
- **Static output**: The `run()` method returns an initial status string indicating readiness.

---

## Future Roadmap

Subsequent phases will introduce modular, in-depth evaluation capabilities:

- **Phase 2: Core Metrics & Class-Wise Performance** (per-class precision, recall, confusion matrix, sliced evaluation)
- **Phase 3: Data Quality Checks** (label noise, missing data, distribution shifts, feature anomalies)
- **Phase 4: Overfitting & Generalization Analysis** (train-test discrepancy, cross-validation variance)
- **Phase 5: Robustness & Adversarial Testing** (perturbation sensitivity, noise injection)
- **Phase 6: Confidence Calibration** (expected calibration error, reliability diagrams)
- **Phase 7: Out-of-Distribution & Unknown-Input Detection** (novelty detection, uncertainty estimation)
- **Phase 8: Reporting & Dashboard** (HTML/JSON export, interactive visualizations)

---

## License

This project is licensed under the terms of the [MIT License](LICENSE).

