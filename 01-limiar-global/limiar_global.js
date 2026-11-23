// Roda uma vez para CADA pixel da imagem.
// pixel: o tom lido, de 0 (preto) a 255 (branco)
// T: o limiar escolhido no controle
// Devolva 255 para branco ou 0 para preto.

function limiarGlobal(pixel, T) {
  if (pixel > T) {
    return 255
  }
  return 0
}
