# Limiarização e Segmentação

Trabalho da matéria de Introdução a Computação Gráfica da UNIFIL, tema 2, limiarização e segmentação.

Aqui tem os códigos que a gente usou na apresentação e a apresentação em si.

Feito por João Gabriel Romanin Seti e Murilo Bertalha Volante.

## O que tem em cada pasta

- `01-limiar-global`: limiar global, um corte T só pra imagem toda
- `02-otsu`: Otsu, onde o próprio histograma escolhe o corte
- `03-limiar-adaptativo`: adaptativo, um corte pra cada pixel
- `apresentacao`: a apresentação, é só abrir o html no navegador

Em cada pasta de método tem um `.js` e um `.py`. O `.js` é o pedacinho que dá pra editar dentro da apresentação, não roda sozinho. O `.py` é o script completo mesmo.

## Testando os js

Abre o `apresentacao/limiarizacao3.html` no navegador. Nos slides que tem o botão `</>` do lado esquerdo, dá pra clicar ali e mexer na função, o slide muda na hora.

## Testando os py no VSCode

Abre a pasta, não o arquivo. `File > Open Folder` e escolhe a pasta `limiarizacao-e-segmentacao`.

Joga uma imagem de teste chamada `documento.jpg` na raiz da pasta. De preferência uma foto de documento com sombra, que é onde dá pra ver a diferença. Tem que ser na raiz porque o botão de play roda a partir dali, então é lá que ele vai procurar a imagem e é lá que ele salva os resultados.

Abre o terminal (`Ctrl+'`) e roda:

```
python -m venv .venv
.venv\Scripts\activate
pip install pillow numpy
```

Depois `Ctrl+Shift+P`, `Python: Select Interpreter` e escolhe o `.venv`.

Agora abre o `02-otsu/otsu.py` e aperta o play (`Ctrl+F5`). Ele mostra o T que escolheu no terminal e salva o `otsu.png` na raiz. Os outros dois é a mesma coisa.

Se quiser rodar com outra imagem, pelo terminal:

```
python 03-limiar-adaptativo/adaptativo.py minhafoto.png
```

Se o `python` não funcionar no Windows, tenta `py`.

## O que cada um cospe

- `limiar_global.py`: salva `global_T60.png`, `global_T100.png`, `global_T140.png` e `global_T180.png`, e mostra no terminal quantos % de pixel ficou branco em cada T
- `otsu.py`: salva `otsu.png` e mostra o T escolhido
- `adaptativo.py`: salva `adapt_media.png` e `adapt_ponderada.png`
