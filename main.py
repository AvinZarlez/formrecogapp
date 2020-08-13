import logging
import os
import sys

from azure.ai.formrecognizer import FormRecognizerClient, FormTrainingClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import ResourceNotFoundError

from examples.content import recognize_content
from examples.receipts import recognize_receipts
from examples.custom_forms import recognize_custom_forms


# Create a logger for the 'azure' SDK
logger = logging.getLogger("azure")
logger.setLevel(logging.DEBUG)

# Configure a console output
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)


# Set up FormRecognizerClient and FormTrainingClient
endpoint = os.environ["FORM_RECOGNIZER_ENDPOINT"]
key = os.environ["FORM_RECOGNIZER_KEY"]

form_recognizer_client = FormRecognizerClient(
    endpoint=endpoint, credential=AzureKeyCredential(key), logging_enable=True
)
form_training_client = FormTrainingClient(endpoint, AzureKeyCredential(key))


# Begin examples:
print("\n\nbegin_recognize_content:\n")
recognize_content(form_recognizer_client)

print("\n\nbegin_recognize_receipts:\n")
recognize_receipts(form_recognizer_client)

print("\n\nbegin_recognize_custom_forms:\n")
recognize_custom_forms(form_recognizer_client, form_training_client, True)


# First, we see how many custom models we have, and what our limit is
print("\n\nManaging custom models:\n")
account_properties = form_training_client.get_account_properties()
print(
    "Our account has {} custom models, and we can have at most {} custom models".format(
        account_properties.custom_model_count, account_properties.custom_model_limit
    )
)


# Next, we get a paged list of all of our custom models
custom_models = form_training_client.list_custom_models()

print("We have models with the following ids:")

for model in custom_models:
    print(model.model_id)


print("\n\nEnd of examples")
