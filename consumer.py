import pika
import sys
 
#abre a conexão com o broker RabbitMQ instalado na máquina local
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
 
#declara um exchange do tipo topic
channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')
 
#cria a fila de onde as mensagens serão lidas (consumidas)
result = channel.queue_declare(queue = '')
#requisita o nome da fila criada
queue_name = result.method.queue
 
#passando-se as binding_keys como argumentos ao executar o script
binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)
 
#varre as binding_keys passadas como argumento.
for binding_key in binding_keys:
#cria o binding (associação) entre o binding key e a fila
   channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)
 
print(' [*] Waiting for logs. To exit press CTRL+C')
 
#definição da função a ser chamada sempre que uma mensagem com binding_key correspondente for recebida na fila
def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
 
#consome da fila criada na aplicação
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)
 
channel.start_consuming()