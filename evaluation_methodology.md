# VLM Evaluation Methods
This document examines ways of evaluating models and measuring their correctness. We will see, with reference to disaster related tasks, which methods work and which do not. Before we see those it is a good idea to look at the nature of data for these kinds of tasks.
Data used for training VLMs in disaster-related contexts are usually:
- Imbalanced - more non damage events than damaged
- Multimodal - will include image, text question, and text answer
- Temporal - can contain before/after image pairs like the MONITRS dataset
- Geospatial - like satellite images, locations correlate to coordinates, often top-down view with variable scales

## Challenges in Evaluation
VLMs output text freely, therefore it is harder to score automatically.
For example, if the ground truth was "damaged", how would we go about scoring "the building seems to be damaged to a significant extent"?
The later section will show different methods which can be used to score these.
## Evaluation Metrics
- Accuracy (or Exact Match): best used if the answer is single word like "yes" or "damaged" or for non open ended questions. Can be a bad indicator for imbalanced datasets (a model that always predicts "no" will have a 98% accuracy if 98% of the data is "no" classes)
- F1 Score: For classification tasks, this gives a good score if it has both good recall and precision. Both are important as it is bad if we miss a case and also bad if we missclassify a case. Offers a solution instead of relying on Accuracy only for imbalanced data specially.
- BLEU: checks the word sequence overlap between the ground truth and the open ended model answer. It penalizes answers which are paraphrases of valid answers.
- ROUGE: focuses on recall and better for longer answers as it looks at overlap and scores based on similar words.

Other than these some commonly used good evaluation methods based on specific tasks are given below.
## Task Specific Evaluation Methods
Based on the task we may prefer specific methods for evaluation. 
- VQA - uses soft matching of the VLMs answer to multiple human answers as reference
- Counting - uses exact match with a ±1 tolerance
- Damage Assessment - uses F1 on each damage category

Each metric has its strengths and weaknesses and shines when used in the right context. The best one to use is always a combination of these to ensure a better overall look at the model.
