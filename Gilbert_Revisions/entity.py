from google.cloud import language as nlp
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/home/harmangea/key.json'

def entity(text):
    client = nlp.LanguageServiceClient()
    document = nlp.Document(content=text, type_=nlp.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)

    for entity in response.entities:
        print("=" * 80)
        results = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1%}",
            wikipedia_url=entity.metadata.get("wikipedia_url", "-"),
            mid=entity.metadata.get("mid", "-"),
        )
        for k, v in results.items():
            print(f"{k:15}: {v}")


text = "Martin Luther King attended Boston University!"
entity(text)