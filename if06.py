def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n1=n%10
    n//=10
    n2=n%10
    n//=10
    n3=n%10
    n//=10
    n4=n%10
    n//=10
    n5=n%10
    max=n1
    s=1
    if n2>max:
        max=n2
        s=2
    if n3>max:
        max=n3
        s=3
    if n5>max:
        max=n5
        s=5
    return s
    