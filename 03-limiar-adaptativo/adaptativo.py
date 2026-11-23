"""Limiarizacao adaptativa: um corte diferente para cada pixel.

bloco e C nao sao o corte: sao os dois parametros que VOCE escolhe.
O corte de cada pixel e calculado como  media_dos_vizinhos - C.

Instalar:  pip install pillow numpy
Rodar:     python adaptativo.py documento.jpg
"""

import sys

import numpy as np
from PIL import Image, ImageFilter


def carregar_cinza(caminho):
    return np.array(Image.open(caminho).convert("L"), dtype=np.uint8)


def media_local(cinza, bloco):
    """Media simples de cada janela bloco x bloco, pela IMAGEM INTEGRAL:
    a soma de qualquer retangulo sai com 4 acessos, seja qual for o bloco.
    """
    r = bloco // 2
    pad = np.pad(cinza.astype(np.float64), r, mode="edge")
    integral = pad.cumsum(axis=0).cumsum(axis=1)
    integral = np.pad(integral, ((1, 0), (1, 0)))
    h, w = cinza.shape
    soma = (integral[bloco:bloco + h, bloco:bloco + w]
            - integral[0:h, bloco:bloco + w]
            - integral[bloco:bloco + h, 0:w]
            + integral[0:h, 0:w])
    return soma / (bloco * bloco)


def media_ponderada(cinza, bloco):
    """Media ponderada por uma gaussiana: os vizinhos mais proximos do
    centro pesam mais. O sigma vem do tamanho do bloco.
    """
    sigma = 0.3 * ((bloco - 1) * 0.5 - 1) + 0.8
    borrada = Image.fromarray(cinza).filter(ImageFilter.GaussianBlur(radius=sigma))
    return np.array(borrada, dtype=np.float64)


def limiar_adaptativo(cinza, bloco=25, C=10, metodo="media"):
    """bloco: tamanho da vizinhanca, sempre impar (precisa de pixel central).
    C: folga. O pixel so vira preto se for pelo menos C tons mais escuro
    que os vizinhos dele.
    """
    if bloco % 2 == 0 or bloco < 3:
        raise ValueError("bloco precisa ser impar e >= 3")

    local = media_local(cinza, bloco) if metodo == "media" else media_ponderada(cinza, bloco)
    corte = local - C                      # um corte para CADA pixel
    return np.where(cinza > corte, 255, 0).astype(np.uint8)


def main():
    caminho = sys.argv[1] if len(sys.argv) > 1 else "documento.jpg"
    cinza = carregar_cinza(caminho)

    # 25 e 10 foram os valores que deram o melhor resultado nos nossos testes
    Image.fromarray(limiar_adaptativo(cinza, 25, 10, "media")).save("adapt_media.png")
    Image.fromarray(limiar_adaptativo(cinza, 25, 10, "gauss")).save("adapt_ponderada.png")
    print("Imagens salvas: adapt_media.png e adapt_ponderada.png")


if __name__ == "__main__":
    main()
