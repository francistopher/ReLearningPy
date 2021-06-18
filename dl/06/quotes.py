just = 0
came = 1
to = 2
say = 3
hello = 4

if __name__ == "__main__":
    import sys
    for index in range(len(sys.argv)):
        print("Argument", index, "=", sys.argv[index])
