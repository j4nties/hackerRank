
def count_substring(string, substring):
    loopSize = len(string) - len(substring)
    substringList = [string[i:i+len(substring)] for i in range(loopSize+1)]
    return substringList.count(substring)

def main():
    string = "ABCDCDC"
    substring = "CDC"
    result = count_substring(string, substring)
    print(result)

main()
