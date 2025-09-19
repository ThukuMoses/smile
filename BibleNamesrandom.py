import random
import time

NAMES=["GENESIS","EXODUS","LEVITICUS","NUMBERS","DEUTERONOMY","JOSHUA","JUDGES","RUTH","SAMUEL","KINGS","CHRONICLES","EZRA","NEHEMIAH","ESTHER","JOB","PSALMS","PROVERBS","ECCLESIASTES","ISAIAH","JEREMIAH","LAMENTATIONS","EZEKIEL","DANIEL","HOSEA","JOEL","AMOS","OBADIAH","JONAH","MICAH","NAHUM","HABAKKUK","ZEPHANIAH","HAGGAI","ZECHARIAH","MALACHI","MATTHEW","MARK","LUKE","JOHN","ACTS","ROMANS","CORINTHIANS","GALATIANS","EPHESIANS","COLOSSIANS","THESSALONIANS","TIMOTHY","TITUS","PHILEMON","HEBREWS","JAMES","PETER","JUDE", "REVELATION"]
Names=random.shuffle(NAMES)
Names=NAMES
questionsPerRound=10
time_limit=7.0#seconds allowed per question
max_shuffle_attempts=10#no. of random shuffles before fallback

def scrambleWord(name, max_attempts=max_shuffle_attempts):
    '''return a scrambled version of 'name' that is guaranteed 
    not to equal the original one (case-insensitive).
    if impossible return none'''
    if len(name)<=1:#the name has 0 or 1 characters
        return None
    if len(set(name.lower()))==1:#the set return has 1 character eg name is aaaaa which returns a set of just a
        return None
    chars=list(name)#convert name to a list of characters

    for _ in range(max_attempts):
        random.shuffle(chars)#rearrange chars list in a random order
        candidate=''.join(chars)#gluue together the random list chars
        if candidate.lower()!=name.lower():
            return candidate
        
        orig=list(name)#new list
        n=len(orig)#length of upcoming rotation loop
        for shift in range(1,n):#backup if random shufle doesn't work
            candidate=''.join(orig[shift:]+ orig[:shift])
            if candidate.lower()!=name.lower():
                return candidate
            
        return None
def choose_scramblable_names(pool, k):#randomly select k names in pool of original names
    available=pool[:]#copy
    random.shuffle(available)
    chosen=[]
    for name in pool:
        if len(chosen)>=k:
            break
        if scrambleWord(name) is not None:#test for scramblability
            chosen.append(name)

    return chosen

def play_round():
    chosen=choose_scramblable_names(Names, questionsPerRound)
    if len(chosen)<questionsPerRound:#names lesser than requested names
        print(f"Note: Only {len(chosen)} scramblable names available for this round.")#warn the user

    score=0
    print(f"\nRound :{len(chosen)} questions, {time_limit} seconds each. \n")
    for idx, original in enumerate(chosen, start=1):
        scrambled=scrambleWord(original)
        if scrambled is None:
            print(f"Skipping {idx} ({original}) -no scramble for name.")
            continue
        print(f"Question {idx} : {scrambled}")
        start=time.perf_counter()
        guess=input("Your guess: ").strip().upper()
        elapsed_time=time.perf_counter()-start

        tries=0
        while tries<3:
            if elapsed_time>time_limit:
                print(f"Too slow... correct name is {original}\n")
                break
            if guess==original:
                print("Correct! Well done!\n")
                score+=1
                break
            else:
                if tries<3:
                    print("wrong, please try again.")
                else:
                    print(f"Wrong! Correct answer is {original}")

                
            tries+=1


    print(f"'nRound complete. You scored {score}/{len(chosen)}") 

def main():
    while True:
        play_round()
        again=input("\nPlay again? Choose (y/N): ").strip().lower()
        if again !='y':
            print("Thanks for playing.")
        break
    
if __name__=="__main__":
    main()