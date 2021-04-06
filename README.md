# Projeto Syngenta 🌱

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

## Detecção da mensagem secreta

No centro da imagem existem pixels brancos que formam a seguinte mensagem:

> Syngenta Digital Hire me

Para encontrar essa mensagem não foi nem um pouco difícil, poi o próprio SO do linux (e a OpenCv) conseguem abrir a imagem em .bmp sem difículdades e a mensagem aparece sem nehum esforço.

Por mais que a mensagem seja tentadora, a facilidade de encontrar a mesma não me convenceu muito. Potanto outras estratégias foram adotadas com o intuito de se encontrar novas mensagens:

### Tentativa um

A primeira tentativa foi aglomerar todos os pixels da esquerda para a direita e de cima para baixo como se fossem bits e considerar os pixels verdes como "1" e os demais como "0", de forma a se conveter blocos de 8 bits em letras, pela tabela ASCII (como existem 420 colunas e 300 linhas, no total existem 160.000 pixels que podem ser divididos em 15.750 blocos de 8). O problema dessa tratativa foi que existiam muitos pontos diferentes de verde (ou seja, muitos zeros) e dessa forma o resultado não formava nada útil. Uma segunda ideia foi remover os blocos de bits com apenas zeros (00000000), mas novamente o resultado nao formou nada útil.

### Tentativa dois

Como a primeira tentativa não funcionou, a segunda tentativa foi explorar a quantidade de pixels em cada linha e coluna. Surpreendentemente, a quantidade de pixels em cada linha era sempre igual a um, exceto na primeira e na decima sexta linha, o que parecia muito suspeito. Por outro lado, a quantidade de pixels em cada coluna seguia um padrão intrigante:
 

 - Na primeira coluna existem 4 pixels verdes;
 - Depois, saltam-se algumas colunas vazias;
 - Aparece uma nova coluna com alguns pontos verdes;
 - A quantidade de pontos verdes em todas as colunas não-vazias é sempre menor que 10;
 - A quantidade de colunas vazias que se saltavam entre duas colunas com pixels verdes, era praticamente 3 ou 4 (e raras vezes 7);

Talvez todos esses padrões sejam mera coincidência, mas de toda forma foi gasto um certo tempo analisando essas referências, sem nenhum grande sucesso.


### Tentativa três

A terceira tentativa, foi verificar a posição relativa dos pixels dentro da linha/coluna. Alguns pixels na vertical pareciam ser alinhados, e isto poderia levar a algum lugar. Foi _printado_ portanto a posição no vetor horizontalmente (0 à 420) ou verticalmente (0 à 300) de forma a tentar transformar essa posição decimal em caracteres:

- Fazendo uma analogia ao alfabeto a = 0, b = 1, c = 2 ... z = 26; e sempre que o numero era maior que 26, retornava-se ao início;
- Usando a tabela ASCII tentando converter os pontos em em um intervalo válido na tabela;
- Aglomerando todos os números e tentando fazer alguma transformação em binário

Nenhuma dessas tentativas resultou em caracteres válidos, ou que fizessem algum sentido.
