def total_overs(balls):
    return balls / 6 if balls % 6 == 0 else balls // 6 + balls % 6 / 10
