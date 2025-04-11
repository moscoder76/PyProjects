book_1= "Automate the Boring Stuff with Python"
librarian_1 = "Mr. Conway"
student_1 = "Jessie"
student_lastname_1 = "Jamson"


print('''Now, a (nomenclature variable based) Dialogue between a Student & a Librarian 
      regarding finding a book about Python Programming is given below 
      (You can, however, change the names by only changing the string value of the above two variables):''')
print("\n" + "-"*50 + "\n")
print(f"""
{student_1}: Excuse me, sir. 
Could you help me find 
a book on Python programming?\n\n
{librarian_1}: Of course! 
Are you looking for something for 
Beginners or a more Advanced level?\n\n
{student_1}: Something in between, I guess? 
I’ve done a few tutorials online, but I want to go deeper.\n\n
{librarian_1}: Got it. Let me check the catalog real quick… [types on keyboard]\n\n
{student_1}: I’m especially interested in 
Data-Science and maybe a bit of Automation.\n\n
{librarian_1}: Then I think 
"{book_1}" might be perfect for you. 
We also have "Python Crash Course" available.\n\n
{student_1}: Oh! I’ve heard of 
"{book_1}". 
Do you have a copy I can borrow?\n\n
{librarian_1}: Yes, one copy is available in the 'Computer Science' section, Row-3, Shelf-B.\n\n
{student_1}: Awesome. I’ll go grab it now!\n\n
{librarian_1}: Would you like me to hold it at the front desk for you, just in case?\n\n
{student_1}: That’d be great, actually. Thanks!\n\n
{librarian_1}: No problem. I’ll put it under your name. The name is {student_1}, right?\n\n
{student_1}: Yes, {student_1} {student_lastname_1}.\n\n
{librarian_1}: Got it. Happy coding!\n\n
{student_1}: Thanks, {librarian_1}! I appreciate it.
""")