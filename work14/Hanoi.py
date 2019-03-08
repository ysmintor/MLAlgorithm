count = 0
def hanoi(n, src, dest, mid):
    global count
    if n == 1:
       print("{}:{}->{}".format(n, src, dest))
       count += 1
    else:
        hanoi(n-1, src, mid, dest)
        print("{}:{}->{}".format(n, src, dest))
        count += 1
        hanoi(n-1, mid, dest, src)

def main():
    hanoi(3, 'A', 'B', 'C')
    print("Total count ==", count)
if __name__ == "__main__":
    main()


