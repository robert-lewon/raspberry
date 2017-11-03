# Arduino

1. Łączymy z dowolnym portem USB w Rasperry PI.
1. Masę taśmy LED łączymy z dowolnym pinem GND.
1. Sygnał taśmy LED łączymy z pinem nr 10.

# Raspberry PI

**Integracja do obsługi LEDów**
1. Jedno USB do połączenia z Arduino (tu idzie sterowanie Rasp -> Ard)
1. Drugie USB do podłączenia USB Grabbera.
1. Najlepiej połączyć te urządzenia do osobnych kontrolerów (tj. obok siebie a nie jeden nad drugim).

**Obsługa przycisku do włączania / wyłączania hyperiona**
1. Jeden przewód od przycisku łączymy do masy (dowolny pin GND).
1. Drugi przewód od przycisku łączymy do GPIO 17.
