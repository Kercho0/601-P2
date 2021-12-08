from google.cloud import language as nlp
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/home/harmangea/key.json'


def sentiment(text):
    try:
        client = nlp.LanguageServiceClient()
        document = nlp.Document(content=text, type_=nlp.Document.Type.PLAIN_TEXT)

        response = client.analyze_sentiment(document=document)


        sentiment = response.document_sentiment
        score=sentiment.score
        results = dict(
            text=text,
            score=f"{sentiment.score:.1%}",
            magnitude=f"{sentiment.magnitude:.1%}",
        )
    
    except Exception:
        pass

    
    #for k, v in results.items():
    #    print(f"{k:10}: {v}")
    return score
