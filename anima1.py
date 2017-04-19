""" 
   Este pequeno trecho de código utiliza a biblioteca *Visual* para Python para
ilustrar a criação de objetos e a animação.

   Para instalar a biblioteca, use: apt-get install python-visual

   Inicialmente é criada um sólido que em um de seus vértices está localizada
uma esfera que deve se movimentar para outro vértice percorrendo uma aresta do 
sólido.


   +----------------------+       +----------------------+
   |                      |       |                      |
   |                      |       |                      |
   |                      |       |                      |
   |                      |  -->  |                      |
   |                      |       |                      |
   |                      |       |                      |
   |                      |       |                      |
   |                      |       |                      |
   +----------------------O       O----------------------+

   A esfera move-se pela aresta com velocidade inicial de 0.1 e sujeita a aceleração
de 0.001.


   Finalizar o percurso sobre a face superior do sólido percorrendo todas as arestas
e voltanto ao ponto inicial fica como exercício.

"""

from visual import *


caixa = box(height=12, length=70, width=70, color = color.green)
scene.center = vector(0,30,-10)

bola = sphere(radius = 2, color= color.red, z=35, x=35, y=7 )
bola.velocidade = 0.1
bola.aceleracao = 0.001

tempo = 0.0
dt=0.001
dest = -35.0

while not(bola.pos.x <= dest):
   rate(1000)
   bola.pos.x = -(bola.velocidade*tempo) + bola.pos.x
   bola.velocidade = bola.velocidade * bola.aceleracao + bola.velocidade
   print "tempo: ",tempo, "\tpos:", bola.pos.x, "\tvelocidade: ", bola.velocidade
   tempo+=dt
