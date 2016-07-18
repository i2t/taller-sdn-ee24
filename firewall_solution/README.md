# Taller de Software-Defined Networking (SDN) de la Euskal Encounter 24
## Software-Defined Networking. ¿Sabías que tu red se puede programar?

### Reto: Aplicación Firewall


#### Objetivo del reto

El objetivo de este taller es modificar el fichero `firewall.py` para hacer una aplicación SDN de firewall que filtre la comunicacion entre pares de direcciones MAC indicadas en el fichero `firewall-policies.csv`.

El fichero `firewall.py` viene comentado con pistas de como programarlo.


### Ejecución de la aplicación SDN

```
cd ~/pox
./pox.py pox.forwarding.l2_learning pox.taller_sdn_ee24.firewall_solution.firewall
```
