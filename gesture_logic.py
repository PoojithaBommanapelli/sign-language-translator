# gesture_logic.py

def finger_states(landmarks):

    

    """
    Returns finger open/close states
    [Thumb, Index, Middle, Ring, Pinky]
    """
    tips = [4, 8, 12, 16, 20]
    pips = [3, 6, 10, 14, 18]

    states = []

    # Thumb (x-axis check)
    states.append(landmarks[tips[0]].x > landmarks[pips[0]].x)

    # Other fingers (y-axis check)
    for i in range(1, 5):
        states.append(landmarks[tips[i]].y < landmarks[pips[i]].y)

    return states


def detect_letter(landmarks):
    fingers = finger_states(landmarks)

    gesture_map = {
        (0,0,0,0,0): "A",
        (1,0,0,0,0): "B",
        (0,1,0,0,0): "C",
        (0,1,1,0,0): "D",
        (0,1,1,1,0): "E",
        (0,1,1,1,1): "F",
        (1,1,0,0,0): "G",
        (1,1,1,0,0): "H",
        (0,0,1,0,0): "I",
        (1,0,1,0,0): "J",
        (1,1,1,1,0): "K",
        (1,1,1,1,1): "L",
        (1,0,0,1,1): "M",
        (0,1,0,1,1): "N",
        (0,1,1,0,1): "O",
        (1,1,0,0,1): "P",
        (1,0,1,1,0): "Q",
        (0,0,1,1,1): "R",
        (0,1,0,0,1): "S",
        (1,0,0,0,1): "T",
        (1,1,0,1,0): "U",
        (0,1,1,1,0): "V",
        (1,0,1,0,1): "W",
        (0,0,0,1,1): "X",
        (1,1,0,1,1): "Y",
        (0,0,1,0,1): "Z"
    }

    return gesture_map.get(tuple(map(int, fingers)), "")
