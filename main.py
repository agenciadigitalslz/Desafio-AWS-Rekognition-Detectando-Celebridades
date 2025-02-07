import cv2  
from inference import inferir_reconhecimento  

def main():  
    # Caminho da imagem a ser processada  
    imagem_caminho = './reconhecimento_celebridades/espn.jpg'  

    # Carregar a imagem  
    imagem = cv2.imread(imagem_caminho)  

    # Chamar função de inferência para reconhecimento  
    resultados = inferir_reconhecimento(imagem)  

    # Exibir os resultados  
    for resultado in resultados:  
        print(f"Nome: {resultado['nome']}, Confiança: {resultado['confianca']}")  

if __name__ == "__main__":  
    main()