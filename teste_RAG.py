from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModel

import faiss

import torch

import warnings

warnings.filterwarnings("ignore")

from sklearn.feature_extraction.text import TfidfVectorizer

# foi usada uma versão anterior do Python para rodar esse projeto. Utilizamos a python-3.10.11.

# Dados de exemplo

documents = [

"""

Astrologia é um sistema de crenças que relaciona a posição dos astros com a personalidade e o destino das pessoas. Usa signos do zodíaco, mapas astrais e datas de nascimento para fazer previsões. Não é ciência, mas é popular em horóscopos e tradições culturais.

  

Astronomia é a ciência que estuda corpos celestes e fenômenos além da atmosfera da Terra, como estrelas, planetas, luas, galáxias, buracos negros e mais. Busca entender origem, evolução e características do universo.

  

Terra: 149,6 mi km do Sol, 12.742 km de diâmetro, rotação 24h, translação 365 dias, único planeta com vida.

  

Marte: 227,9 mi km do Sol, 6.779 km de diâmetro, rotação 24,6h, translação 687 dias, planeta vermelho devido à ferrugem.

  

Saturno: 1,43 bi km do Sol, 116.460 km de diâmetro, rotação 10,7h, translação 29 anos, famoso pelos anéis.

  

Júpiter: 778,5 mi km do Sol, 139.820 km de diâmetro, rotação 9,9h, translação 12 anos, maior planeta, tem 90+ luas.

  

Vênus: 108,2 mi km do Sol, 12.104 km de diâmetro, rotação 243 dias, translação 225 dias, mais quente, atmosfera densa de CO₂.

"""

]

  

# Vetorização dos documentos

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

  

def embed(texts):

inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

with torch.no_grad():

embeddings = model(**inputs).last_hidden_state.mean(dim=1)

return embeddings.numpy()

  

document_embeddings = embed(documents)

  

# Indexação com FAISS

index = faiss.IndexFlatL2(document_embeddings.shape[1])

index.add(document_embeddings)

  

# Modelo Gerador

generator_tokenizer = AutoTokenizer.from_pretrained("t5-small")

generator_model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")

  

# Função de busca e geração

def rag(question, top_k=1):

# Embedding da pergunta

question_embedding = embed([question])

# Recuperação dos documentos mais similares

distances, indices = index.search(question_embedding, top_k)

retrieved_docs = [documents[idx] for idx in indices[0]]

# Concatenar documentos recuperados ao prompt

input_text = " ".join(retrieved_docs) + " " + question

inputs = generator_tokenizer.encode(input_text, return_tensors="pt", truncation=True)

with warnings.catch_warnings():

warnings.simplefilter("ignore")

utputs = generator_model.generate(inputs, max_length=50, num_beams=2)

answer = generator_tokenizer.decode(outputs[0], skip_special_tokens=True)

return answer

  

# Exemplo de uso

question = "O que é astronomia ? E me passe dados de um planeta"

print(rag(question))