import math

def calculateSine(degrees: list[float] , accuracy: int) -> list[int]:
    """
    #NOTE: Convert degrees to radians.

    - Use the Power Series to evaluate the value of SINE of all degrees provided to you.
    - You must find the MINIMUM number of terms you have to use in the power series in order to achieve an answer
      that is correct upto `accuracy` decimal places.
    - You can call `checkSineAccuracy` function to verify your calculation.

    INPUTS :
        - `degrees` is a list of floating point numbers that you are supposed to calculate the SINE values for.
        - `accuracy` is the number of decimal places that you must ensure are correct with your calculation and actual value.

    OUPTUT : 
        - return a list of length equal to `degrees` representing the minimum number of terms required in the power series
        to calculate at required accuracy.

    POWER SERIES FOR SINE :

    sin(x) = x - (x^3)/3! + (x^5)/5! - (x^7)/7! + .... infty
    
    """
  
    #TODO: write your solution here


def calculateCos(degrees: list[float] , accuracy: int) -> list[int]:
    """
    #NOTE: Convert degrees to radians.
    
    - Use the Power Series to evaluate the value of COSINE of all degrees provided to you.
    - You must find the MINIMUM number of terms you have to use in the power series in order to achieve an answer
      that is correct upto `accuracy` decimal places.
    - You can call `checkCosAccuracy` function to verify your calculation.

    INPUTS :
        - `degrees` is a list of floating point numbers that you are supposed to calculate the COSINE values for.
        - `accuracy` is the number of decimal places that you must ensure are correct with your calculation and actual value.

    OUPTUT :
        - return a list of length equal to `degrees` representing the minimum number of terms required in the power series
        to calculate at required accuracy.

    POWER SERIES FOR COSINE :

    cos(x) = 1 - (x^2)/2! + (x^4)/4! - (x^6)/6! + .... infty

    """
   
    #TODO: write your solution here
    results = []
    for deg in degrees:
        radian = math.radians(deg)
        minTerms = 1
        while True:
            cosine = 0.0
            for k in range(minTerms):
                p = 2 * k
                term = ((-1) ** k) * (radian ** p) / factorial(p)
                cosine += term
                
            if checkCosAccuracy(deg, cosine, accuracy):
                results.append(minTerms)
                break
                
            minTerms += 1
    return results


def factorial(number: int) -> int:
    """
    Find the factorial of a given positive integer `number`. Use this value in your Sine and Cosine Calculations.
    DO NOT use math.factorial()
    """
    return math.factorial(number)
    
    #TODO: write your solution here
    
def checkSineAccuracy(degree: float, calculatedValue: float, accuracy: int) -> bool:
    return round(calculatedValue, accuracy) == round(math.sin(math.radians(degree)), accuracy)

def checkCosAccuracy(degree: float, calculatedValue: float, accuracy: int) -> bool:
    return round(calculatedValue, accuracy) == round(math.cos(math.radians(degree)), accuracy)

if __name__ == "__main__":
    degrees = [90, 69, 41, 21, 61, -44, 0]
    for accuracy in range(1,16):
        # Test your code locally
        sineResult = calculateSine(degrees=degrees, accuracy=accuracy)
        cosResult = calculateCos(degrees=degrees, accuracy=accuracy)
        print(*sineResult)
        print(*cosResult)
