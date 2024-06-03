dish= input("Enter a dish name")
indian=["samosa", "dal","roti"]
chinese=["noodles","egg role","fried rice"]
italian=["pasta","pizza","risotto"]
if dish in indian:
    print("The dish is Indian")
elif dish in chinese:
    print("The dish is chinese")
elif dish in italian:
    print("The dish is italian")
else:
    print("None")
