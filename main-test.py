from main import Add, Subtract

def TestAdd():
    assert Add(2,3) == 5
    print("Add Function works correctly")

def TestSubtract():
    assert Subtract(5,4) == 1
    print("Subtract Function works correctly")

if __name__ == '__main__':
    TestAdd()
    TestSubtract()