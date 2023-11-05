import pandas as pd

df = pd.read_csv('data/fine_food_reviews_with_embeddings_1k.csv')
df['ada_embedding'] = df.ada_embedding.apply(eval).apply(np.array)
