Ir documentando cambios <n> \
IDEAS:
	
	integrar el event_finder del GOE para determinar la duración de la ventana para mandar comandos.
	
	
# Pasos iniciales para instalación de software de vuelo
## Instalación de Sistema operativo.

Instrucciones para instalacion desde cero: <n> \
Descargar imagen de RASPBIAN BULLSEYE 11 <n> \
Descargar https://www.raspberrypi.com/software/ y montar imagen en tarjeta SD de 16GB o más <n> \
- Habilitar SSH y definir Usuario:Hostname:Contraseña <n> 
- Configurar red local WiFi que se usará <n> \
	
## Actualización de sistema e instalación de librerías
	
Insertar SD en RPZ <n>\
Conectar HUB USB con teclado y Smartphone que permita compartir internet via USB <n>\
Conectar alimentación de RPZ y luego esperar boot de sistema <n>\
Una vez haya iniciado el sistema y entre a la linea de comandos, verificar que hay acceso a internet ingresando en la linea de comando de Raspberry:
	
	ifconfig -a

Debe verse el tag ```usb0``` y tener una ip asignada en el tag ```inet```  

Con el acceso a internet confirmado, ejecutar las siguientes lineas:
>Esto buscará e instalar actualizaciones para el sistema operativo
	
	sudo apt-get update && sudo apt-get install -f
	

Luego se instalaran paquetes necesarios para la instalacion de los drivers
	
	sudo apt-get install -y build-essential git raspberrypi-kernel-headers

Otra linea a ejecutar es la siguiente:

	sudo apt-get dist-upgrade -f
>Seguido de ```Y``` confirmando que aceptamos la instalación. Esto tomara varios minutos asi que solo queda esperar.
	

Finalmente se reiniciará el sistema usando ```sudo reboot```

	
## Descarga e instalación de driver de TP-Link WN725N  
Cambiaremos el directorio en el cual descagaremos los archivos con el comando ```cd Downloads```, luego ejecutar la siguiente linea:
	
	git clone https://github.com/lwfinger/rtl8188eu.git
	
>Esto lo que hará será clonar los archivos de este git a la carpeta en la cual nos encontramos
	
Luego ejecutaremos la siguiente linea ```cd rtl8188eu``` que nos cambiara el directorio a la carpeta descarga, acto seguido ejecutar ```make```, esto nuevamente tomará bastante tiempo. Finalizada esto ejecutar ```sudo make install```, tomará bastante tiempo por lo que solo queda esperar.  
Una vez finalida la tarea anterior, ingresar ```sudo reboot``` para aplicar los cambios, una vez iniciado, apagar el sistema con ```sudo shutdown now```
Conectar el WIFI USB y prender la Raspberry.

## Configurar WIFI
En este paso se tiene que editar dos archivos del sistema. Primero ejecutaremos:
		
	sudo nano /etc/network/interfaces
	
Dejar el archivo tal como se indica a continuación:
	
	source /etc/network/interfaces.d/*
	auto lo
	iface lo inet loopback
	auto wlan0
	allow-hotplug wlan0
	iface wlan0 inet manual
	wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
	
EL siguiente archivo a editar se logra con:
	
	sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
	
Debe contener lo siguiente
	
	country = CL
	update_config=1
	ctrl_interfaces=DIR=/var/run/wpa_supplicant GROUP=netdev
	network={
		scan_ssid=1
		ssid="Nombre red WIFI"
		psk="Contraseña red WIFI"
	}
Hecho esto se reinicia el sistema con ```sudo reboot``` para hacer efectivos los cambios y una vez que inicie el sistema, la Raspberry debería estar conectada a la red que configuramos cada vez que inicie.
	
	
# REFERENCIAS
	https://gist.github.com/MBing/de297a8ae5e8a191c55a67a568d20d31#file-install_wlan_dongle-sh-L51
	https://www.electronicshub.org/setup-wifi-raspberry-pi-2-using-usb-dongle/
	
En caso de cambiar de tarjeta SD manteniendo el nombre de usuario y hostname:
	
	https://docs.bluehosting.cl/troubleshooting/servidores/como-solucionar-el-mensaje-de-error-la-clave-del-equipo-remoto-ha-cambiado-al-iniciar-sesion-via-ssh.html
	

