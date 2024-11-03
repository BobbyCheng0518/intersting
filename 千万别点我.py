for i in range(1000000000):
    with open(f'n{i}.txt', 'w', encoding='utf-8') as f:
        f.write("你好" * 100000000000)
