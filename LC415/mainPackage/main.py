#main.py

# Entry point and test code for LeetCode problem 415
# Solution has been provided
from solutionPackage.Solution import *

# instantiate an object of type solution
mySolution = Solution()
'''
result = mySolution.addStrings("123", "456")
print(result) # We expect 579

#Do tests that we know should fail
testResults = mySolution.addStrings("cat", "hat")    
#print(testResults) # we do not know what to expect

testResults = mySolution.addStrings("-123", "456")
#print(testResults) # we expect 333

testResults = mySolution.addStrings("123.5", "456.1")
#print(testResults) # we expect 579.6

testResults = mySolution.addStrings("123a", "456b")
#print(testResults) # we do not know what ot expect

testResults = mySolution.addStrings("123!", "456@")
#print(testResults) # we do not know what to expect
'''
# Build a list of test cases and expected results
num1 = ["123", "999", "1000"]
num2 = ["456", "111", "2000"]
expectedResult = ["579", "1110", "3000"]
# Loop to try all these cases
for i in range(0,3):
    result = mySolution.addStrings(num1[i], num2[i])
    if result == str(expectedResult[i]):
        print("Test passed")
    else:
        print("Test failed. Just give up.")
        print("Expected result:", expectedResult[i], "Actual result:", result)