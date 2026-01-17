import time
from core.traffic_light import TrafficLight, LightState

def test_cycle():
    feu = TrafficLight()

    durations = {
        LightState.RED: 2,
        LightState.GREEN: 2,
        LightState.ORANGE: 1
    }

    print("État initial :", feu.state.value)

    for i in range(6):
        feu.update(durations)
        print("État actuel :", feu.state.value)
        time.sleep(1)

if __name__ == "__main__":
    test_cycle()
