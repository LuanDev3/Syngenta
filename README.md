# Projeto Syngenta

O objetivo desse projeto é o desenvolvimento de um sistema capaz de realizar a contagem de pixels verdes em uma imagem ".bmp", e em seguida encontrar uma mensagem escondida na mesma caso possível.

# Dependências

Para se realizar a detecção e contagens dos pixels verdes foi utilizada a linguagem de programação **python** dentro do SO linux devido a facilidade de implementação e integração com bibliotecas de tratamento de imagens. Com o intuito de se conseguir abrir a imagem e trabalhá-la sem maiores complicações foi utilizada a biblioteca **OpenCV**. Um guia de intalação simplificado da biblioteca para o SO linux pode ser encontrado neste [link](https://docs.opencv.org/master/d7/d9f/tutorial_linux_install.html).

Com o intuito de se trabalhar de forma facilitada com os vetores de pontos da imagem principalmente na parte relativa à mensagem escondida foi utilizada a bilbioteca numérica do python, **numpy** que posse ser facilmente instalada utilizado o instalador pdrão de bibliotecas do python pelo comando:

> pip install numpy

## Detecção dos pixels verdes

A detecção dos pixels verdes foi realizada inicialmente a partir do valor RGB desses pixels. Para isso a imagem foi aberta com a ajuda da biblioteca **OpenCv**, e foi analisado um contunto de pontos verdes, que retornaram o seguinte valor de coloração:

> nível de verde em RGB = (96, 192, 0)

Todos os pontos aparentemente possuem a mesma coloração, todavia, alterar uma unidade em qualquer canal pode gerar uma nova cor, de forma que não seja visível para os olhos. Outro ponto importante também, é que em projetos reais muitas das vezes um valor de interesse não é padrão e portanto o ideal é se trabalhar com um _intervalo de cor_. Nesse aspecto, foi definido um intervalo de cor com 15% de tolerância para cada canal do padrão RGB.

Com posse do intervalo definido, cada pixel da imagem foi analisado individualmente e seu valor em RGB foi comparado para ver se estava dentro do intervalo definido. Em caso positivo, esse era considerado um pixel verde, e a contagem continuava, até se percorrer toda a imagem.
