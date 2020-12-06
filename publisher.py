import pika
import sys
 
#abre a conexão com o broker RabbitMQ instalado na máquina local
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
 
#declara um exchange do tipo topic (que pode já estar declarado no broker)
channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')
 
#a routing key da mensagem é passada diretamente como argumento durante a execução do script
routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
#ainda como argumento, é possível escrever a mensagem como argumento
message = ' '.join(sys.argv[2:]) or 'Hello World!'
#publica a mensagem com o routing key no exchange topic_logs
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()