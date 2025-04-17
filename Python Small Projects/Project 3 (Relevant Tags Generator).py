from keybert import KeyBERT

kw_model = KeyBERT()
# title = "How to Build an AI Assistant Using Python and Transformers"
title = "Old Lady hitting sky with broom"
keywords = kw_model.extract_keywords(title, keyphrase_ngram_range=(1, 2), stop_words='english')
# print(keywords)
print(keywords[0][0])
print(keywords[0][1])

for k in keywords:
    tag = k[0]    # keyword text
    score = k[1]  # relevance score
    print(f"Tag: {tag}\nSEO Score: {score}\n")
