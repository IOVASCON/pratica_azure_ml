# scripts/train.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def main():
    # Ler o CSV (ajuste o caminho conforme seu arquivo)
    df = pd.read_csv("./data/metadata.csv")
    
    # Supondo que 'label' seja a coluna alvo
    X = df.drop("label", axis=1)
    y = df["label"]
    
    # Dividir em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Instanciar e treinar o modelo
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    # Verificar a acurácia
    accuracy = model.score(X_test, y_test)
    print(f"Acurácia do modelo: {accuracy:.2f}")

if __name__ == "__main__":
    main()
