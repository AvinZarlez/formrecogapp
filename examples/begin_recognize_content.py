import os
from azure.ai.formrecognizer import FormRecognizerClient, FormTrainingClient


def format_bounding_box(bounding_box):
    if not bounding_box:
        return "N/A"
    return ", ".join(["[{}, {}]".format(p.x, p.y) for p in bounding_box])


def begin_recognize_content(
    form_recognizer_client: FormRecognizerClient, form_training_client: FormTrainingClient
):
    formUrl = str(os.environ["FORM_DATA_URL"])

    poller = form_recognizer_client.begin_recognize_content_from_url(formUrl)
    contents = poller.result()

    for idx, content in enumerate(contents):
        print("----Recognizing content from page #{}----".format(idx))
        print(
            "Has width: {} and height: {}, measured with unit: {}".format(
                content.width, content.height, content.unit
            )
        )
        for table_idx, table in enumerate(content.tables):
            print(
                "Table # {} has {} rows and {} columns".format(
                    table_idx, table.row_count, table.column_count
                )
            )
            for cell in table.cells:
                print(
                    "...Cell[{}][{}] has text '{}' within bounding box '{}'".format(
                        cell.row_index,
                        cell.column_index,
                        cell.text,
                        format_bounding_box(cell.bounding_box),
                    )
                )
        for line_idx, line in enumerate(content.lines):
            print(
                "Line # {} has word count '{}' and text '{}' within bounding box '{}'".format(
                    line_idx, len(line.words), line.text, format_bounding_box(line.bounding_box)
                )
            )
        print("----------------------------------------")
