import os

from azure.ai.formrecognizer import FormRecognizerClient, FormTrainingClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import ResourceNotFoundError

endpoint = os.environ["FORM_RECOGNIZER_ENDPOINT"]
key = os.environ["FORM_RECOGNIZER_KEY"]

form_recognizer_client = FormRecognizerClient(endpoint=endpoint, credential=AzureKeyCredential(key))

form_training_client = FormTrainingClient(endpoint, AzureKeyCredential(key))

trainingDataUrl = str(os.environ["TRAINING_DATA_URL"])
formUrl = str(os.environ["FORM_DATA_URL"])
receiptUrl = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/receipt/contoso-receipt.png"

poller = form_recognizer_client.begin_recognize_content_from_url(formUrl)
contents = poller.result()


def format_bounding_box(bounding_box):
    if not bounding_box:
        return "N/A"
    return ", ".join(["[{}, {}]".format(p.x, p.y) for p in bounding_box])


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


poller = form_recognizer_client.begin_recognize_receipts_from_url(receiptUrl)
receipts = poller.result()

for idx, receipt in enumerate(receipts):
    print("--------Recognizing receipt #{}--------".format(idx))
    receipt_type = receipt.fields.get("ReceiptType")
    if receipt_type:
        print(
            "Receipt Type: {} has confidence: {}".format(
                receipt_type.value, receipt_type.confidence
            )
        )
    merchant_name = receipt.fields.get("MerchantName")
    if merchant_name:
        print(
            "Merchant Name: {} has confidence: {}".format(
                merchant_name.value, merchant_name.confidence
            )
        )
    transaction_date = receipt.fields.get("TransactionDate")
    if transaction_date:
        print(
            "Transaction Date: {} has confidence: {}".format(
                transaction_date.value, transaction_date.confidence
            )
        )

print("Receipt items:")
for idx, item in enumerate(receipt.fields.get("Items").value):
    print("...Item #{}".format(idx))
    item_name = item.value.get("Name")
    if item_name:
        print(
            "......Item Name: {} has confidence: {}".format(item_name.value, item_name.confidence)
        )
    item_quantity = item.value.get("Quantity")
    if item_quantity:
        print(
            "......Item Quantity: {} has confidence: {}".format(
                item_quantity.value, item_quantity.confidence
            )
        )
    item_price = item.value.get("Price")
    if item_price:
        print(
            "......Individual Item Price: {} has confidence: {}".format(
                item_price.value, item_price.confidence
            )
        )
    item_total_price = item.value.get("TotalPrice")
    if item_total_price:
        print(
            "......Total Item Price: {} has confidence: {}".format(
                item_total_price.value, item_total_price.confidence
            )
        )

subtotal = receipt.fields.get("Subtotal")
if subtotal:
    print("Subtotal: {} has confidence: {}".format(subtotal.value, subtotal.confidence))
tax = receipt.fields.get("Tax")
if tax:
    print("Tax: {} has confidence: {}".format(tax.value, tax.confidence))
tip = receipt.fields.get("Tip")
if tip:
    print("Tip: {} has confidence: {}".format(tip.value, tip.confidence))
total = receipt.fields.get("Total")
if total:
    print("Total: {} has confidence: {}".format(total.value, total.confidence))
print("--------------------------------------")
