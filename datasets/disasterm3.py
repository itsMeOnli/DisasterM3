import os
import json
from datasets.base import BaseDataset

class DisasterM3Dataset(BaseDataset):
    def __init__(self, image_dir, annotation_file):
        self.image_dir = image_dir
        self.annotation_file = annotation_file
        self.data = []

    def load(self):
        with open(self.annotation_file, 'r') as f:
            self.data = json.load(f)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        image_path = os.path.join(self.image_dir, item['image'])
        question = item['question']
        answer = item['answer']
        return image_path, question, answer
