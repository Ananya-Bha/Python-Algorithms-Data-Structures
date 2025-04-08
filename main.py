import random

# -------------------------------------------------
# CREATIVE CONSOLE STYLES
# -------------------------------------------------

# FOREGROUND (text) colour escape codes
k = "\033[30m"  # black
r = "\033[31m"  # red
g = "\033[32m"  # green
y = "\033[33m"  # yellow
b = "\033[34m"  # blue
p = "\033[35m"  # purple
c = "\033[36m"  # cyan
w = "\033[37m"  # white
reset = "\033[0m"  # reset text back to normal

# BACKGROUND colour escape codes
kb = "\033[40m"  # black
rb = "\033[41m"  # red
gb = "\033[42m"  # green
yb = "\033[43m"  # yellow
bb = "\033[44m"  # blue
pb = "\033[45m"  # purple
cb = "\033[46m"  # cyan
wb = "\033[47m"  # white

# escape codes for styles
bold = "\033[1m"
faint = "\033[2m"
underline = "\033[4m"
invert = "\033[7m"

# ===========================================================
# 1️⃣ LESSON 9.7 STRONGER STRINGS
# ===========================================================

# -------------------------------------------------
# CHALLENGE 1 - INDEXES IN LISTS
# -------------------------------------------------

words = [
    "awesome", "bananas", "I", "gravy", "flying", "am", "penguins", "love"
]
indexes = [0, 1, 2, 3, 4, 5, 6, 7]

# 🧑‍💻 YOUR CODE HERE



# -------------------------------------------------
# CHALLENGE 2 - INDEXES IN STRINGS
# -------------------------------------------------

code = "YUEISNTHTESMRTBHZEMWAQTJURITXSA IOUZA"

# 🧑‍💻 YOUR CODE HERE



# -------------------------------------------------
# CHALLENGE 3 - DECIPHERING THE CODE
# -------------------------------------------------

codex = [2, 5, 8, 9, 12, 31, 13, 15, 17, 31, 18, 20, 22, 25, 26, 28]

# 🧑‍💻 YOUR CODE HERE



# -------------------------------------------------
# CHALLENGE 4 - DECIPHERING THE CODE
# -------------------------------------------------

# 🧑‍💻 YOUR CODE HERE

# -------------------------------------------------
# CHALLENGE 5 - MAKE IT A FUNCTION
# -------------------------------------------------

code2 = "LTQASFKXGDOEPTHWLEPNREIDNPQINLLN TDKFJDIUZK"
codex2 = [1, 3, 6, 11, 32, 13, 14, 17, 32, 20, 21, 23, 32, 25, 27, 29, 30]

# 🧑‍💻 YOUR CODE HERE



# -------------------------------------------------
# CHALLENGE 6 - STRING REPLACEMENT
# -------------------------------------------------

# sentence = "I love cats.\n"
# print(sentence)

# 🧑‍💻 YOUR CODE HERE

# -------------------------------------------------
# CHALLENGE 7 - STRING REPLACEMENT 2
# -------------------------------------------------

# sentence = "In|a|hole|in|the|ground|there|lived|a|hobbit.\n"
# print(sentence)

# 🧑‍💻 YOUR CODE HERE



# -------------------------------------------------
# CHALLENGE 8 - WORD SEARCH - PART 1
# -------------------------------------------------

grid = """
    MATRESSOJACFCQYKIVWIJKQIVCKFOUBG
    ATKRWYLCGGPBYPMXUUBMOWPQNWRBMIPX
    TEDHORANDTGITHEONESNBFKGGUNJOQKY
    SCQGRPKQWSMWXEJSGMFJYAOJXUOXKKOS
    YWFCYMATRIXSTNDBBIIBGDHQHWHQKXVF
    HRTLJKPOYALXOWLZLNQHNNXKVVWGMQMG
    AVTIPGCKEVBEOYKVUTODWBMAHWDAWGBW
    BTICSFHWYUBJYSBPIMYDAOAWMATRIXFJ
    VCFYATIDVNLRWDRHRYAENAOSWGOSMMUN
    IDOXKZEKCXUPXDEZYQGFXGDBIHODQBPG
    LQXKWDJQWQOUMATRIXLROACLAZYLTFBJ
    PYHQFPINCUYSYHPZVCFZFDZSTJMZIBNG
    BZDKYRBQMFSIPXUGPUVHMBRBOLJLCRVM
    XQGLCPRIXIWLHIBHAJNEOXADDWQJOHOJ
    NHDIQTFOVFUMEEPILLBIPRQJHJJQZNPM
    ZGJSNUPDYVVELBPKEOWZLNAUGIYPSSLJ
    QCWNEOIDBWRDJSZDFRDOXHKHIWZNSDQR
    JQKVCJOASUOEVULUCUSUJSANXTJKCIBS
    YWBDMATRIXMLIJMDCOUBWUYJKQXVRBQJ
    AWMJDHQXODQBMZEQZQDWWJSZVVKLRATC
    BNBPFWGKFXMMJFJVDFPPLXUQAUBWAQLO
    WSEICXXXKNMATRIXJJAZEMDJRYICMYFW
    JASEGZXKEFHPSJXAFRWMBGFPGPEJPWBV
    ZGPTUPOLVYAJLRXHXBWTTBSAYQNZRMHH
    UNHWBMAXXFLXLDAISPOONXOWTENRSWQP
    DBKBXPOVILMWYONFKKLUESAGOTTTEHLL
    DSMVDBMKLLSSYTDBHYPLPFAZYXTHNXKY
    FRFIACPILLSRMFAVWVDAFFTZXWSFPVLS
    WCLJYIVZTUDQILPOMATRIXEHURPGEJKX
    PZFOTJGNSVUSUMORPHEUSWSWJNNDVAAT
    KCBMORPHEUSCZONAYHSQFMJZWCKMYVNM
    MNKNGPNUWKMMGNCCIJHQFWGKSCCTOEPE
"""

# print(grid)

# 🧑‍💻 YOUR CODE HERE



# -------------------------------------------------
# CHALLENGE 9 - WORD SEARCH - PART 2
# -------------------------------------------------

words = ["pill", "matrix", "Neo", "spoon", "one", "Morpheus"]

# 🧑‍💻 YOUR CODE HERE



# -------------------------------------------------
# CHALLENGE 10 - WORD SEARCH - PART 3
# -------------------------------------------------

new_grid = """
    UYLZOLUKCUJMDZKDGVWQQOWEFKXDQSNL
    UZWMOGWGPPPYTHONWBZEKSVTZNAUTBLB
    DXCODINGTCGVNNRZNLDYCCONCEMPFDHP
    WOPQVDFFQKHPWCJWCGZCXFSEZUSNWUZH
    EQTIUNYCDXISROCKETHOURIGKEKKHEWY
    ZZPYEBOXKBZXFPGCXUYNHQPOTIFMKSAL
    PHTJBGTDLTNQOPTLIMOQMGPVDTTYBDMP
    SMVGLYMYDCDTYUVWZEAFEHGFUNLGKIYF
    XIFKPJOQCODINGPTZGASJZZGEYUHVBEV
    NCHLQISBWRYOJJERLYHUVNRBMMAONBGN
    NDFBHUPWWZUUMKVVASPIOSBKLQYXZYQW
    ROQBVCMPYTHONOQMCYPORVDQZCXXPLUF
    SUZJSNAAJHCGMFVROKYTTUYJIKYMCIFN
    ZCKLDPXLYYWKMOMRERASUCKTWANSRGLC
    REVPOCODINGXBBUKXVDUSTUDLPKKMWPR
    QUIRPROCKETHOURLIPAEVEFCNVNMUQGZ
    KOPMEAVIENBMATVBNUXLJDOSXBPLWDCI
    LJKVNSFMMUFFQBZWHOJPKEIQBDAKVPJE
    HGZSPQKCGQBHFUDXUZRGMVIDLTJSVSER
    APSHAPYTHONKSTMZQXBGWZAGJQYHPXRR
    OXJWCYGHNKJEWTMYKODFNGMYHCCUCEKU
    UOPPWDMTBASEWPAROHHWAWTUCPJVWNDR
    CPSGUXKKJLIQDZEGKATDWNUBNARDCDFJ
    VXLWVBCLYZLHLMXZMGRONWNPYTHONKPO
    CMJDBQVDSMYOTAMDGMYZPJRYEBCXXQRE
    RXXCRTXZOPYUBVWQHHWQYWYLNOLSCFHJ
    AZOCGKVUFFZRROCKETHOURHSMZLHSEOF
    JPPWAAMUZMJUHYFUNQDJNDFUHUTJZJWB
    GMRHUUEAEWQMMFYSLBHNBWUTFPYTHONV
    RCGSETFFUNNPNOITHUWHERUGTWHZFUFT
    NSWTXCLZBXWERQAZNJCVJJUXNLLDJQDY
    GYFXXYFIHUQWPMTJRZAILAFYIMFUTWIY
"""
new_words = ["rockethour", "coding", "fun", "python"]

# 🧑‍💻 YOUR CODE HERE
