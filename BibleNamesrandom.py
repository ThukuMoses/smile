import random
import time

Names=["GENESIS","EXODUS","LEVITICUS","NUMBERS","DEUTERONOMY","JOSHUA","JUDGES","RUTH","SAMUEL","KINGS","CHRONICLES","EZRA","NEHEMIAH","ESTHER","JOB","PSALMS","PROVERBS","ECCLESIASTES","ISAIAH","JEREMIAH","LAMENTATIONS","EZEKIEL","DANIEL","HOSEA","JOEL","AMOS","OBADIAH","JONAH","MICAH","NAHUM","HABAKKUK","ZEPHANIAH","HAGGAI","ZECHARIAH","MALACHI","MATTHEW","MARK","LUKE","JOHN","ACTS","ROMANS","CORINTHIANS","GALATIANS","EPHESIANS","COLOSSIANS","THESSALONIANS","TIMOTHY","TITUS","PHILEMON","HEBREWS","JAMES","PETER","JUDE", "REVELATION"]
questionsPerRound=10
time_limit=7.0#seconds allowed per question
max_shuffle_attempts=10#no. of random shuffles before fallback

def scrambleWord(name, max_attempts=max_shuffle_attempts):
    '''return a scrambled version of 'name' that is guaranteed 
    not to equal the original one (case-insensitive).
    if impossible return none'''
    if len(name)<=1:#all characters are the same, eg aaaaa
        return None
    chars=list(name)#convert name to a list of characters

    for _ in range(max_attempts):
        random.shuffle(chars)
        candidate=''.join(chars)
        if candidate.lower()!=name.lower():
            return candidate
        
        orig=list(name)
        n=len(orig)
        for shift in range(1,n):
            candidate=''.join(orig[shift::]+ orig[::])
            if candidate.lower()!=name.lower():
                return candidate
            
        return None
    