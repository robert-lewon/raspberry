## Instalacja uslugi obslugujacej przycisk
1. `mkdir /home/pi/Programs`
1. `vim ambilight_run.sh`
1. skopiować dane "ambilight_run.sh"
1. `vim ambilight_toggle.py`
1. skopiować dane "ambilight_toggle.py"
1. `sudo vim /lib/systemd/system/elk_ambilight.service`
1. skopiowac dane "elk_ambilight.service"
1. `sudo systemctl enable elk_ambilight`
1. `sudo service elk_ambilight start`
