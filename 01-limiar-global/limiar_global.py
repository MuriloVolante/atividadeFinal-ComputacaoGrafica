"""Limiarizacao global: um unico corte T para a imagem inteira.

Instalar:  pip install pillow numpy
Rodar:     python limiar_global.py documento.jpg
"""

import sys

import numpy as np
from PIL import Image


def carregar_cinza(caminho):
    """Abre a imagem e converte para tons de cinza (modo L: 0 a 255)."""
    return np.array(Image.open(caminho).convert("L"), dtype=np.uint8)


def limiar_global(cinza, T):
    """Pixel > T vira branco (255); senao, preto (0).

    Uma unica comparacao vetorizada sobre a matriz inteira:
    nao existe laco sobre pixels.
    """
    return np.where(cinza > T, 255, 0).astype(np.uint8)


def main():
    caminho = sys.argv[1] if len(sys.argv) > 1 else "documento.jpg"
    cinza = carregar_cinza(caminho)

    for T in (60, 100, 140, 180):
        binaria = limiar_global(cinza, T)
        Image.fromarray(binaria).save(f"global_T{T}.png")
        brancos = (binaria == 255).mean() * 100
        print(f"T = {T:3d}  ->  {brancos:5.1f}% dos pixels ficaram brancos")


if __name__ == "__main__":
    main()
