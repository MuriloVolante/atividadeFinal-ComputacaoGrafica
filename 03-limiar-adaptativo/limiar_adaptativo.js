// Roda uma vez para CADA pixel.
// pixel: o tom lido
// media: a media dos vizinhos dentro do bloco
// C: a folga escolhida no controle

function limiarAdaptativo(pixel, media, C) {
  const corteLocal = media - C
  if (pixel > corteLocal) {
    return 255
  }
  return 0
}
