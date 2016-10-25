def simplify_fraction(fraction):
    while fraction[1] % fraction[0] == 0 or fraction[0] == 1:
        fraction[1] /= fraction[0]
        # fraction[0] /=