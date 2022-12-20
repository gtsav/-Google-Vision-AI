import json
import pip._vendor.requests 
import xlwt

features = [
  {
    "maxResults": 50,
    "type": "LANDMARK_DETECTION"
  },
  {
    "maxResults": 50,
    "type": "FACE_DETECTION"
  },
  {
    "maxResults": 50,
    "type": "OBJECT_LOCALIZATION"
  },
  {
    "maxResults": 50,
    "type": "LOGO_DETECTION"
  },
  {
    "maxResults": 50,
    "type": "LABEL_DETECTION"
  },
  {
    "maxResults": 50,
    "model": "builtin/latest",
    "type": "DOCUMENT_TEXT_DETECTION"
  },
  {
    "maxResults": 50,
    "type": "SAFE_SEARCH_DETECTION"
  },
  {
    "maxResults": 50,
    "type": "IMAGE_PROPERTIES"
  },
  {
    "maxResults": 50,
    "type": "CROP_HINTS"
  }
]

#Ftiaxnoume thn prwth eikona
imageSource1 = {
  'imageUri': "https://pbs.twimg.com/media/FjQyEcCacAAK3TP?format=jpg&name=medium"
}
image1 = {
  'source': imageSource1
}
annotateImageRequest1 = {
  "features": features,
  'image': image1
}

#Ftiaxnoume thn defterh eikona
imageSource2 = {
  'imageUri': "https://pbs.twimg.com/media/FiH4qFsaYAADb9g?format=jpg&name=medium"
}
image2 = {
  'source': imageSource2
}
annotateImageRequest2 = {
  "features": features,
  'image': image2
}

#Ftiaxnoume thn trith eikona
imageSource3 = {
  'imageUri': "https://pbs.twimg.com/media/FiIAHZ4aEAI4nRH?format=jpg&name=medium"
}
image3 = {
  'source': imageSource3
}
annotateImageRequest3 = {
  "features": features,
  'image': image3
}

#Ftiaxnoume thn tetarth eikona
imageSource4 = {
  'imageUri': "https://pbs.twimg.com/media/Fiv7sp0XoAI2O9A?format=jpg&name=900x900"
}
image4 = {
  'source': imageSource4
}
annotateImageRequest4 = {
  "features": features,
  'image': image4
}

#Ftiaxnoume thn pempth eikona
imageSource5 = {
  'imageUri': "https://pbs.twimg.com/media/FiiOJKYacAAc4sJ?format=jpg&name=large"
}
image5 = {
  'source': imageSource5
}
annotateImageRequest5 = {
  "features": features,
  'image': image5
}

#Ftiaxnoume thn ekth eikona
imageSource6 = {
  'imageUri': "https://pbs.twimg.com/media/FiIdJYbWIAEkmNT?format=jpg&name=small"
}
image6 = {
  'source': imageSource6
}
annotateImageRequest6 = {
  "features": features,
  'image': image6
}

#Ftiaxnoume thn ebdomh eikona
imageSource7 = {
  'imageUri': "https://pbs.twimg.com/media/FiMFwHmXwAklpOE?format=jpg&name=360x360"
}
image7 = {
  'source': imageSource7
}
annotateImageRequest7 = {
  "features": features,
  'image': image7
}

#Ftiaxnoume tto antikeimeno request
requests = [annotateImageRequest1, annotateImageRequest2, annotateImageRequest3, annotateImageRequest4, annotateImageRequest5, annotateImageRequest6, annotateImageRequest7]
requestItem = {
    'requests': requests
}

#Stelnoume to request kai lambanoume to response
response = pip._vendor.requests.post("https://vision.googleapis.com/v1/images:annotate?key=YOURAPIKEY", json.dumps(requestItem))

#Kanoume desirialize to content toy response apo JSON se Dictionary
responceContent = json.loads(response.content)
print(response.content)
responses = responceContent['responses']


#Dhmioyrgoume to excel workbook
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

#Grafoume ta Headers
sheet1.write(0, 0, "Image")
sheet1.write(0, 1, "Adult Annotation")
sheet1.write(0, 2, "Spoof Annotation")
sheet1.write(0, 3, "Medical Annotation")
sheet1.write(0, 4, "Violence Annotation")
sheet1.write(0, 5, "Racy Annotation")
sheet1.write(0, 6, "Error")

#Symplhrwnoume ta pedia
for i in range(0,7):
  response = dict[str, any](responses[i])
  if 'error' not in response:
    x = response
    sheet1.write(i + 1, 0, i + 1)
    x = response['safeSearchAnnotation']['adult']
    sheet1.write(i + 1, 1, x)
    x = response['safeSearchAnnotation']['spoof']
    sheet1.write(i + 1, 2, x)
    x = response['safeSearchAnnotation']['medical']
    sheet1.write(i + 1, 3, x)
    x = response['safeSearchAnnotation']['violence']
    sheet1.write(i + 1, 4, x)
    x = response['safeSearchAnnotation']['racy']
    sheet1.write(i + 1, 5, x)
  else:
    sheet1.write(i + 1, 0, i + 1)
    x = response['error']['message']
    sheet1.write(i + 1, 6, x)

#Apothikevoume to Excel
book.save("Results.xls")
print("done")