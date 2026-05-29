# DisasterM3 Repository Analysis

## Repository Structure

The repository is minimal in structure:

DisasterM3/
├── models/
├── pyscripts/
│   └── run_vllm.py
├── __init__.py
└── README.md

The benchmarking logic is in the `run_vllm.py` script. 

## Code Organization Analysis

The current framework is a research script, not a modular system. The entry point is the `run_vllm.py` is called directly with command-line arguements.

```
python disaster_m3/pyscripts/run_vllm.py --model_id Qwen/Qwen2.5-VL-7B-Instruct --subset bearing_body

```

There is no configuration file system nor any abstraction layer for datasets,and no experiment tracking. The logic for loading data, running the model, and evaluating results is coupled within a single script.

## Is the Framework Tied to a Specific Dataset?

Yes. The framework is built entirely around the DisasterM3 dataset.
The `--subset` argument only selects subsets within DisasterM3 
(e.g. bearing_body, report) — it does not support loading a completely 
different dataset like EarthVQA or MONITRS without rewriting the script.

To support another dataset you would need to:
- Rewrite the data loading logic for the new dataset format
- Modify the evaluation logic if the task type differs
- Hardcode new paths and parameters

There is no shared interface that a new dataset could plug into.

## Proposed Modular Redesign

A modular redesign would introduce:

- `datasets/base.py` — abstract BaseDataset class with load(), 
  __len__(), __getitem__()
- `datasets/disasterm3.py` — DisasterM3-specific implementation
- `models/base.py` — abstract BaseModel with run(image, question)
- `evaluation/base.py` — abstract BaseEvaluator
- `configs/` — YAML-based configuration to select dataset/model 
  without touching code
- `experiments/tracker.py` — MLflow or W&B integration

This decouples dataset, model, and evaluation logic so any combination
can be run by changing a config file only.
