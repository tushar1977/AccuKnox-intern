class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}


# Driver Code to Test
def test():
    rec = Rectangle(2, 3)
    for i in rec:
        print(i)


if __name__ == "__main__":
    test()
