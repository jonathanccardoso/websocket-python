<?php
    class server {
        public function soma($a, $b){
            return $a+$b;
        }
        public function subtracao($a, $b){
            return $a-$b;
        }
        public function divisao($a, $b){
            return $a/$b;
        }
        public function multiplicacao($a, $b){
            return $a*$b;
        }
    }

    // server
    $parametros = array(
        'uri' => 'localhost:5000/server.php',
    );

    // null is wsdl
    $server = new SoapServer (null, $parametros);
    $server->setObject(new server());
    
    // server to get URL
    $server->handle();
    