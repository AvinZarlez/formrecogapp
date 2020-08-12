import os

from examples.begin_recognize_content import begin_recognize_content
from examples.begin_recognize_receipts import begin_recognize_receipts

from azure.ai.formrecognizer import FormRecognizerClient, FormTrainingClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import ResourceNotFoundError

endpoint = os.environ["FORM_RECOGNIZER_ENDPOINT"]
key = os.environ["FORM_RECOGNIZER_KEY"]

form_recognizer_client = FormRecognizerClient(endpoint=endpoint, credential=AzureKeyCredential(key))

form_training_client = FormTrainingClient(endpoint, AzureKeyCredential(key))

print("\n\nbegin_recognize_content:\n")
begin_recognize_content(form_recognizer_client, form_training_client)
print("\n\nbegin_recognize_receipts:\n")
begin_recognize_receipts(form_recognizer_client, form_training_client)

trainingDataUrl = str(os.environ["TRAINING_DATA_URL"])
