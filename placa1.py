#!/usr/bin/env python3
import asyncio
from camadafisica import PTY, ZyboSerialDriver
from ip import IP               # copie o arquivo do T3
from slip import CamadaEnlace   # copie o arquivo do T4


driver = ZyboSerialDriver()

serial1 = driver.obter_porta(0)
pty1 = PTY()

outra_ponta = '192.168.200.1'
nossa_ponta = '192.168.200.2'

print('Para conectar a outra ponta da camada física, execute em outro terminal:')
print('  sudo slattach -v -p slip {}'.format(pty1.pty_name))
print()
print('E, em um terceiro terminal, execute:')
print('  sudo ifconfig sl0 {} pointopoint {}'.format(outra_ponta, nossa_ponta))
print('  sudo ip route add 192.168.200.0/24 via {}'.format(nossa_ponta))
print()

# Os endereços IP que especificamos abaixo são os endereços da outra ponta do enlace.
enlace = CamadaEnlace({outra_ponta: pty1,
                       '192.168.200.3': serial1,})

rede = IP(enlace)
rede.definir_endereco_host(nossa_ponta)

# A tabela de encaminhamento define através de qual enlace (especificado pelo IP
# que está na outra ponta daquele enlace) o nosso roteador pode alcançar cada
# faixa de endereços IP.
rede.definir_tabela_encaminhamento([
    ('192.168.200.1/32', outra_ponta),
    ('192.168.200.0/24', '192.168.200.3'),
])

asyncio.get_event_loop().run_forever()
