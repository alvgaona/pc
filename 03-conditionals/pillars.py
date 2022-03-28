def dist_first_last(num_pillars: int, distance: float, width: float) -> float:
    """
    Parameters
    ----------
    num_pillars : int
        Number of pillars (>= 1).
    distance : float
        Distance between pillars (10 - 30 meters).
    width : float
        Width of a pillar (10 - 50 cm).

    Returns
    -------
    Distance between first and last pillar (float).
    """
    pass


def main():
    d = dist_first_last(10, 2, 30)
    print(d)


if __name__ == '__main__':
    main()
