def scale(json):
    return (float(json['boundedBy']['Envelope']['upperCorner'].split()[1]) - float(
        json['boundedBy']['Envelope']['lowerCorner'].split()[1])) / 3
