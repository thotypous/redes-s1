#!/usr/bin/env python3
import asyncio
from camadafisica import ZyboSerialDriver
from ip import IP               # copie o arquivo do T3
from slip import CamadaEnlace   # copie o arquivo do T4


driver = ZyboSerialDriver()

serial1 = driver.obter_porta(0)
serial2 = driver.obter_porta(4)

enlace = CamadaEnlace({'192.168.200.4': serial1,
                       '192.168.200.2': serial2,})

rede = IP(enlace)
rede.definir_endereco_host('192.168.200.3')
rede.definir_tabela_encaminhamento([
    ('192.168.200.0/24', '192.168.200.2'),
    ('192.168.200.4/32', '192.168.200.4'),
])

asyncio.get_event_loop().run_forever()
