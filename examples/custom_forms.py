import os
from azure.ai.formrecognizer import FormRecognizerClient, FormTrainingClient


def format_bounding_box(bounding_box):
    if not bounding_box:
        return "N/A"
    return ", ".join(["[{}, {}]".format(p.x, p.y) for p in bounding_box])


def recognize_custom_forms(
    form_recognizer_client: FormRecognizerClient,
    form_training_client: FormTrainingClient,
    training_labels: bool,
):
    trainingDataUrl = str(os.environ["TRAINING_DATA_URL"])
    formUrl = str(os.environ["FORM_DATA_URL"])

    poller = form_training_client.begin_training(
        trainingDataUrl, use_training_labels=training_labels
    )
    model = poller.result()

    # Custom model information
    print("Model ID: {}".format(model.model_id))
    print("Status: {}".format(model.status))
    print("Training started: {}".format(model.training_started_on))
    print("Training completed: {}".format(model.training_completed_on))

    print("Recognized fields:")
    # Looping through the submodels, which contains the fields they were trained on
    for submodel in model.submodels:
        print(
            "...The submodel with form type {} has accuracy '{}'".format(
                submodel.form_type, submodel.accuracy
            )
        )
        for name, field in submodel.fields.items():
            print(
                "...The model found field '{}' to have label '{}' with name '{}' with an accuracy of {}".format(
                    name, field.label, field.name, field.accuracy
                )
            )

    # Make sure your form's type is included in the list of form types the custom model can recognize
    poller = form_recognizer_client.begin_recognize_custom_forms_from_url(
        model_id=model.model_id, form_url=formUrl
    )
    forms = poller.result()

    for idx, form in enumerate(forms):
        print("--------Recognizing Form #{}--------".format(idx))
        print("Form {} has type {}".format(idx, form.form_type))
        for name, field in form.fields.items():
            # each field is of type FormField
            # The value of the field can also be a FormField, or a list of FormFields
            # In our sample, it is just a FormField.
            print(
                "...Field '{}' has value '{}' with a confidence score of {}".format(
                    name, field.value, field.confidence
                )
            )
            # label data is populated if you are using a model trained with unlabeled data, since the service needs to make predictions for
            # labels if not explicitly given to it.
            if field.label_data:
                print(
                    "...Field '{}' has label '{}' with a confidence score of {}".format(
                        name, field.label_data.text, field.confidence
                    )
                )
        print("-----------------------------------")
