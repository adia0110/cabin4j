with open('Challenge-3-Input.txt', 'r') as infile:
    with open('output.txt', 'w') as outfile:
        for line in infile:
            lhs, rhs = line.strip().split('=')
            result = eval(lhs.strip())
            print(result)
            outfile.write(f"{lhs} = {result}\n")
