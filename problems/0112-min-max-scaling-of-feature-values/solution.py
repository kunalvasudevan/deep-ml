def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    mini=min(x)
    maxi=max(x)
    sol=[]
    for i in range(len(x)):
        res= ((x[i] - mini)/(maxi-mini))
        sol.append(res)
    return sol
    pass