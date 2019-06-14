Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

    | Method | Runtime Complexity |
    | --- | --- |
    | Array.Set | $O(1)$ |
    | Add | $O(1)$ |

    Total: $O(1)$

2. What is the space complexity of your ring buffer's `append` function?

    Total: $O(1)$

3. What is the runtime complexity of your ring buffer's `get` method?

    | Method | Runtime Complexity |
    | --- | --- |
    | For Loop | $O(n)$ |
    | &nbsp;&nbsp;&nbsp;&nbsp;Array.Get | $O(1)$ |
    | &nbsp;&nbsp;&nbsp;&nbsp;Boolean | $O(1)$ |

    Total: $O(n)$

4. What is the space complexity of your ring buffer's `get` method?

    Total: $O(1)$

5. What is the runtime complexity of the provided code in `names.py`?

    | Method | Runtime Complexity |
    | --- | --- |
    | For Loop | $O(n)$ |
    | &nbsp;&nbsp;&nbsp;&nbsp;For Loop | $O(n)$ |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Array.Get | $O(1)$ |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Array.Get | $O(1)$ |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Boolean | $O(1)$ |

    Total: $O(n^2)$

6. What is the space complexity of the provided code in `names.py`?

    Total: $O(1)$

7. What is the runtime complexity of your optimized code in `names.py`?

    | Method | Runtime Complexity |
    | --- | --- |
    | For Loop | $O(n)$ |
    | &nbsp;&nbsp;&nbsp;&nbsp;Dict.Set | $O(1)$ or $O(n)$ |
    | For Loop | $O(n)$ |
    | &nbsp;&nbsp;&nbsp;&nbsp;Dict.In | $O(1)$ or $O(n)$ |
    | &nbsp;&nbsp;&nbsp;&nbsp;Dict.In | $O(1)$ |

    Total: $O(n)$ to $O(n^2)$

    Stretch:

    | Method | Runtime Complexity |
    | --- | --- |
    | For Loop | $O(n)$ |
    | &nbsp;&nbsp;&nbsp;&nbsp;Array.Get | $O(1)$ |
    | &nbsp;&nbsp;&nbsp;&nbsp;Boolean | $O(1)$ |

    Total: $O(n \log(n))$

8. What is the space complexity of your optimized code in `names.py`?

    Total: $O(n)$

    Stretch Total: $O(n)$
