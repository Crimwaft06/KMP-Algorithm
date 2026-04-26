from kmp import compute_lps

def kmp_trace(text, pattern):
    lps = compute_lps(pattern)

    print("\nPattern:", pattern)
    print("Text   :", text)
    print("LPS    :", lps)
    print("\nTracing process:\n")

    i = 0
    j = 0

    while i < len(text):

        print(f"Compare text[{i}]={text[i]} with pattern[{j}]={pattern[j]}")

        if text[i] == pattern[j]:
            i += 1
            j += 1
            print(" Match\n")

        if j == len(pattern):
            print("Pattern FOUND at position", i - j)
            return True

        elif i < len(text) and text[i] != pattern[j]:
            print(" Mismatch")

            if j != 0:
                print(f" Jump using LPS -> j = {lps[j - 1]}\n")
                j = lps[j - 1]
            else:
                print(" Move text pointer\n")
                i += 1

    print("Pattern NOT found")
    return False


text = input("Enter text: ")
pattern = input("Enter pattern: ")

kmp_trace(text, pattern)