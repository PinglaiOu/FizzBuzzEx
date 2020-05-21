with open('input.txt', encoding='utf-8') as f:
    lines = f.read().split('\n')
    m = int(lines[-2].strip())
    input_data = [l.strip().split(':') for l in lines[:-2]]
    output = ''.join([s for i, s in sorted(input_data, key=lambda x: int(x[0])) if m % int(i) == 0])
    print(output if len(output) else m)
