# Vision Tasks

This document is a brief outlook on computer vision tasks that can be done on data and the distinction between each of them.

We will talk about 3 types of tasks:
1. [[#Classification]]
2. [[#Detection]]
3. [[#Segmentation]]

## Classification
This is a type of task that deals with giving a label to an image.
- Single label for the whole image
- Input: An Image
- Output: A class label (can be binary like yes/no or multiclass like severity low/medium/high)
- Example: Taken an image, classification can say, was this area disaster effected, yes or no. Or if this structure is damaged or intact.
- Limitation - We cant know where or how much the damage is. 
## Detection
With detection we try to draw bounding boxes as well as labels for objects within images. 
If classification could only describe (classify) the image as a category, detection algorithm can detect objects, and mark them enabling us to locate/count them.
- **Input**: An image
- **Output**: Bounding boxes against objects with classifications for each one
- **Example**: With a satellite image of a flood affected area, a detection model can identify all the buildings, cars and people and mark their locations
- **Limitation**: It only draws a rough rectangle around the objects, not the exact shape of the object.
## Segmentation
This is a more detailed task in which we classify each pixel. We are able to draw pixel boundaries or outlines for each object and classify them.
There are 2 types; 
- Semantic segmentation which labels each pixel by category and therefore has no clear distinction between individual objects.
- Instance segmentation which seperates each object. It classifies build 1, building 2, building 3 etc for example within the same category.
- **Input**: An image
- **Output**: Pixels distinction of objects
- **Example**: With a satellite image of a flood affected area, a detection model can identify how much flooding (area of number of flood pixels) or can distinguish the number of buildings distinctly labeling each one depending on the model.

## Comparison Table
| Task           | Output         | Answers                   | Disaster Use Case            |
| -------------- | -------------- | ------------------------- | ---------------------------- |
| Classification | Single label   | What?                     | Did a flood occur?           |
| Detection      | Bounding boxes | What and Where?           | Where are damaged buildings? |
| Segmentation   | Pixel mask     | What, Where and How much? | Exact flood area coverage    |

## Disaster Context
These tasks are often used in combination. Detection can be used to find damaged structures. Segmentation is used to map zones based on severity or if it was affected. Classification can flag the level of severity. 
However using these does come with some challenges. especially when working with satellite imagery. 
Some challenges include:
- top-down view: traditional models are not trained on top down images so these could throw off models if they have not been specifically trained for this. 
- scale: satellite images have big sizes and can have variable scales. A building could look the size of a car or a whole area could look the size of one building. 
These challenges make disaster remote sensing a difficult domain even for modern Vision-Language Models, which are typically trained on ground-level imagery.
