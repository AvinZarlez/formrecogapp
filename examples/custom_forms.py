import os
from azure.ai.formrecognizer import FormRecognizerClient, FormTrainingClient


def format_bounding_box(bounding_box):
    if not bounding_box:
        return "N/A"
    return ", ".join(["[{}, {}]".format(p.x, p.y) for p in bounding_box])


def recognize_custom_forms(
    form_recognizer_client: FormRecognizerClient, form_training_client: FormTrainingClient
):
    trainingDataUrl = str(os.environ["TRAINING_DATA_URL"])
