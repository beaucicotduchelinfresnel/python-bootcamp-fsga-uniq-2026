def calculer_moyenne(notes):
    return sum(notes)/len(notes)

def main():
    notes = [12, 17, 11, 22]
    print(calculer_moyenne(notes))
if __name__ == "__main__":
    main()

