// Roda uma vez para CADA corte T, de 0 a 255.
// w0, w1: fracao de pixels no grupo escuro e no grupo claro
// mu0, mu1: tom medio de cada grupo
// O Otsu escolhe o T que devolver a MAIOR nota.

function nota(w0, w1, mu0, mu1) {
  const distancia = mu0 - mu1
  return w0 * w1 * distancia * distancia
}
