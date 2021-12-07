import re

def parseSentence(str) :

    # sentence structure pattern
    # subject (is the| is a | is an| is | an | a) predicate
    pattern1 = re.compile(r"^\s*([A-Za-z]+)\s+(is the|is a|is an|is|an|a)\s+([A-Za-z]+)\s*$")
    match1 = pattern1.match(str)
    
    if match1 :
     print(f"atom - {match1.group(3)}({match1.group(1)})")
     print(f"variable - {match1.group(1)}")
     return
    
    # sentence structure pattern
    # subject and subject (are) predicate
    pattern2 = re.compile(r"^\s*([A-Za-z]+)\s(and)*\s([A-Za-z]+)*\s+(are)\s+([A-Za-z]+)\s*$")
    match2 = pattern2.match(str)

    if match2 :
      print(f"atom - {match2.group(5)}({match2.group(1)},{match2.group(3)})")
      print(f"variable - {match2.group(1)},{match2.group(3)}")
      return
     
    # sentence structure pattern
    # subject (adverbs) predicate
    pattern3 = re.compile(r"([A-Za-z]+)\s([A-Za-z0-9]+\s)+([A-Za-z]+)")
    match3 = pattern3.match(str)
    if match3 :
        print(f"atom - {match3.group(3)}({match3.group(1)})")
        print(f"variable - {match3.group(1)}")
        return

    print("Invalid sentence cannot be parsed")


def main() :
    str = input("enter a simple sentence : ")
    parseSentence(str)


if __name__ == "__main__" :
  main()