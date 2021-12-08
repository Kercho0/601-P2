from google.cloud import language as nlp
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/home/harmangea/key.json'

def classify(text):
    category= "No Category Found"
    try:
        contents_list=[]
        client = nlp.LanguageServiceClient()
        document = nlp.Document(content=text, type_=nlp.Document.Type.PLAIN_TEXT)

        response = client.classify_text(document=document)

        for category in response.categories:
            contents_list.append(category.name)
            #print("=" * 80)
            #print(f"category  : {category.name}")
            #print(f"confidence: {category.confidence:.0%}")
        if not contents_list:
            category="No Category Found"
        else:
            category= contents_list[0]
        
        
    except Exception:
        pass

    return category
    



