def presenteer(tekst):
    bt = {}
    bt.update(tekst)
    
    print()

    for key, value in bt.items():
        print(key, ':', value, 'euro')

    print("=" * 25)

    print("Totaal", ':', sum(bt.values()), 'euro')

    return bt