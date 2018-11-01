"""
This file is able to extract out text from images Use case is certificates
We dont use text_detection as its more relaxed and can be used for street signs as opposed
to document_text_detection
"""
import io
import os
from google.cloud import vision
from google.cloud.vision import types
from sys import argv
import urllib.error as errors

"""There are 2 components to extraction - vision and nlp """
""" Vision(extraction of text component) """
def text(files):
    try :
        vision_client = vision.ImageAnnotatorClient()
        file_name = os.path.join(
            os.path.dirname(__file__),files
        )

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)
        response = vision_client.document_text_detection(image=image)
        all_text = []
        for text in response.text_annotations:
            all_text.append(text.description)
        return all_text
    except errors.HttpError as e:
        print("Http error for the file : %s" % e)
    except KeyError as e1:
        print("Key error :%s" % e1)

if __name__ =="__main__" :
    files = argv[1]
    extracted_text = text(files)
    print(extracted_text)

