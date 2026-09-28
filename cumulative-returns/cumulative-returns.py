def cumulative_returns(returns: list) -> list:
    """
    Returns the compounded cumulative return after every period.
    """
    # Write code here
    result = []
    cum = 1.0
    
    for r in returns:
        cum *= (1+r)
        result.append(cum - 1)
    return result
        
        