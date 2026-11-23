"""Algoritmo de Otsu: o proprio histograma escolhe o corte.

Instalar:  pip install pillow numpy
Rodar:     python otsu.py documento.jpg
"""

import sys

import numpy as np
from PIL import Image


def carregar_cinza(caminho):
    return np.array(Image.open(caminho).convert("L"), dtype=np.uint8)


def otsu(cinza):
    """Testa os 256 cortes e devolve o que MAXIMIZA a variancia entre
    classes:  sigma_B(T) = w0 * w1 * (mu0 - mu1) ** 2
    """
    hist = np.bincount(cinza.ravel(), minlength=256)   # pixels de cada tom
    p = hist / hist.sum()                              # probabilidade de cada tom
    niveis = np.arange(256)

    omega0 = np.cumsum(p)                  # fracao de pixels com tom <= T
    omega1 = 1.0 - omega0                  # fracao com tom > T
    soma = np.cumsum(p * niveis)           # soma de i * p_i ate T
    mu_total = soma[-1]                    # media de toda a imagem

    with np.errstate(divide="ignore", invalid="ignore"):
        mu0 = soma / omega0                        # media do grupo escuro
        mu1 = (mu_total - soma) / omega1           # media do grupo claro
        sigma_b = omega0 * omega1 * (mu0 - mu1) ** 2

    sigma_b = np.nan_to_num(sigma_b)       # cortes com um grupo vazio viram 0
    T = int(np.argmax(sigma_b))            # o corte de maior nota
    return T, sigma_b


def main():
    caminho = sys.argv[1] if len(sys.argv) > 1 else "documento.jpg"
    cinza = carregar_cinza(caminho)

    T, sigma_b = otsu(cinza)
    print(f"Corte escolhido pelo Otsu: T = {T}")
    print(f"Nota desse corte: {sigma_b[T]:.1f}")

    binaria = np.where(cinza > T, 255, 0).astype(np.uint8)
    Image.fromarray(binaria).save("otsu.png")


if __name__ == "__main__":
    main()
