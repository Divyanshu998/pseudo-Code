# Python Programs Pseudocode

This repository contains various Python programs with their corresponding pseudocode.

## 1. ArmStrongNumber.java
```
DECLARE num : INTEGER
DECLARE num1 : INTEGER
DECLARE sum : INTEGER
DECLARE Lastdigit : INTEGER
READ num
SET num1 := num
SET sum := 0
WHILE(num > 0)
    LastDigit = num MOD 10
    sum = sum + LastDigit*LastDigit*LastDigit
    num = num/10
END WHILE
IF (sum == num1) THEN
    PRINT "Palindrome"
ELSE
    PRINT "Not Palindrome"
```

## 2. CheckWhetherDigitisPresent.java
```
DECLARE NUM: INTEGIER
DECLARE Lastdigit : INTEGER
DECLARE d: INTEGER
DECLARE found: BOOLEAN
SET found = False
Read d
WHILE num > 0
    Lastdigit =num MOD 10
    num = num/10
    If Lastdigit == d THEN
        found = TRUE
        BREAK
    END IF
END WHILE
IF Found ==TRUE THEN
    PRINT" Search Succesfull"
ELSE
    PRINT "Search unsuccesstul"
END IF
```

## 3. CountDigitsOfaNumber.java
```
DECLARE num:INTEGER
DECLARE count:INTEGER
SET count := 0
READ num
WHILE num > 0
    num = num/10
    INCREMENT count
END WHILE
PRINT count
```

## 4. CountHowManyDigits.java
```
DECLARE num: INTEGER
DECLARE d: INTEGER
DECLARE count: INTEGER
DECLARE lastdigit: INTEGER
SET count := 0
READ num, d
WHILE num > 0
    lastdigit = num MOD 10
    IF lastdigit == d THEN
        INCREMENT count
    END IF
    num = num / 10
END WHILE
PRINT count
```

## 5. ExampleOne.java
```
DECLARE x : INTEGER
DECLARE y : INTEGER
SET x = 15, y = 12
y = x-1
do {
    PRINT x
    x = y + (x-2)
} WHILE (x < 40)
END DOWHILE
```

## 6. FibonacciSeries.java
```
DECLARE n: INTEGER
DECLARE prev : INTEGER
DECLARE next : INTEGER
DECLARE sum : INTEGER
SET prev:=0,next:=1,sum:=0
READ n
PRINT prev
PRINT next
WHILE sum <= 0
    sum := prev + next
    PRINT sum
    prev := next
    next := sum
END WHILE
```

## 7. PalinDromeNumber.java
```
DECLARE n: INTEGER
DECLARE r: INTEGER
DECLARE m: INTEGER
DECLARE lastdigit: INTEGER
SET r := 0
READ n
SET m := n
WHILE n > 0
    lastdigit = n MOD 10
    r = r * 10 + lastdigit
    n = n / 10
END WHILE
IF m == r THEN
    PRINT "Palindrome"
ELSE
    PRINT "Not Palindrome"
END IF
```

## 8. PrimeNumber.java
```
DECLARE N:INTEGER
READ N
IF(N == 2)THEN
    PRINT "Prime Number"
    STOP
ELSE
    for i ← 2 TO √n DO
        IF N MOD i = 0 THEN
            PRINT "Not Prime Number"
            STOP
        END IF
    END FOR
END IF
PRINT "Prime"
```

## 9. PrintAllEvenNumber.java
```
DECLARE num : INTEGER
DECLARE i : INTEGER
SET i := 0
READ num
FOR i := 0 TO num
    IF i MOD 2 == 0
        PRINT i
    END IF
END FOR
```

## 10. QuestionEight.java
```
DECLARE p,q,r,sum : INTEGER
SET p = 3, q = 8, r = 1
SET sum := p+q+r
IF((p NOT EQUALS 0) and (sum EQUALS 11) and (q EQUALS 4) and (r NOT EQUALS 0))
    PRINT "Success"
ELSE
    PRINT "Fail"
END IF
```

## 11. QuestionEleven.java
```
SET x to 0
SET n to 1
WHILE(n <= 100)
    x = x + n
    n = n + 1
END WHILE
WRITE x
```

## 12. QuestionFive.java
```
INTEGER p, q, r
SET p = 6, q = 3, r = 5
q = 1 + r
q = 5 + q
IF(5 < r or (p + r) > (r - p))
    p = (9 & 7) + p * p
    q = 5 + q * q
END IF
PRINT (p + q + r)
```

## 13. QuestionFour.java
```
INTEGER a, b, c
SET a = 7, b = 8, c = 9
IF((a ^ b ^ c) < (b + c + a))
    b = 6 + a
END IF
a = 8 ^ b
PRINT a + b + c
```

## 14. QuestionFourteen.java
```
INTEGER a,b,c
SET a := 7, b := 10, c := 9
FOR (EACH i FROM 3 to 4)
    a = b
    IF((b - a + i) < (c + b))
        CONTINUE
    ELSE
        JUMP OUT OF THE LOOP
    END IF
    a = (5 + 6) ^ c
END FOR
PRINT a + b
```

## 15. QuestionNine.java
```
INTEGER x,y,z
SET x := 10, y := 6, z = 6
IF(x > y)
    x = y
ELSE
    y = x
END IF
IF(z > y)
    z = y
ELSE
    y = z
END IF
PRINT x + y + z
```

## 16. QuestionOne.java
```
INTEGER a,b,c
SET a = 4, b = 4, c = 4
IF(a & (b ^ b) & c)
    a = a >> 1
END IF
PRINT a + b + c
```

## 17. QuestionSeven.java
```
INTEGER x,y,z
SET x = 8, y = 6, z = 4
IF(x > y)
    x = y
ELSE
    y = x
END IF
IF(z > y)
    z = y
ELSE
    y = z
END IF
PRINT x + y + z
```

## 18. QuestionSix.java
```
INTEGER x,y,z
SET x = 10,y = 16,z = 3
IF(x > y)
    x = 2 * y
ELSE
    y = x / 2
END IF
IF(z > y)
    z = 2 * y
ELSE
    y = z / 2
END IF
PRINT x + y + z
```

## 19. QuestionTen.java
```
INTEGER x = 9, y = 2, z = 6
INTEGER a
a = x & y | z
PRINT a
```

## 20. QuestionThirteen.java
```
INTEGER a = 2, b = 50
IF(a MOD 3 IS EQUAL 0)
    PRINT a
ELSE
    PRINT b - 1
END IF
b = b / 5
a = a + 1
```

## 21. QuestionThree.java
```
DECLARE x : INTEGER
SET x := 259
IF(x MOD 9 EQUALS 5)
    PRINT "0"
ELSE IF(x MOD 9 EQUALS 0)
    PRINT '9'
ELSE
    PRINT x MOD 9
END IF
```

## 22. QuestionTwelve.java
```
INTEGER p , q , r
SET p = 0, q = 2, r = 9
r = 7 + p
q = q + r
FOR EACH i FROM 4 to 7
    p = (p + p) & q
    if((p + q) < (r - p) || 8 < p)
        p = (p + 2) + q
        JUMP OUT OF THE LOOP
    END IF
END FOR
PRINT p + q
```

## 23. QuestionTwo.java
```
INTEGER a,b,c
SET a = 2, b = 5, c = 10
FOR(EACH i from 3 to 6)
    a = (a + a) + a
    a = (a ^ 11) + i
END FOR
b = (9 + 7) + a
PRINT a + b
```

## 24. ReverseaNumber.java
```
DECLARE n: INTEGER
DECLARE r: INTEGER
DECLARE lastdigit: INTEGER
SET r := 0
READ n
WHILE n > 0
    lastdigit = n MOD 10
    r = r * 10 + lastdigit
    n = n / 10
END WHILE
PRINT r
```

## 25. SumOfnIntegers.java
```
DECLARE n : INTEGER
DECLARE sum : INTEGER
READ n
sum := 0
FOR i := 1 TO n
    sum := sum + i
END FOR
PRINT sum
```

## 26. SumofSquareOfNumbers.java
```
DECLARE num : INTEGER
DECLARE sum : INTEGER
READ num
SET sum := 0
FOR i := 1 TO num
    sum = sum + i * i
END FOR
PRINT sum
```

## 27. AreaofCircle.py
```
FUNCTION AOC (rad : real) RETURN REAL  
DECLARE A : REAL  
A = 3.14 * rad * rad  
RETURN A  
END FUNCTION  
PRINT CALL AOC (5)
```


## 28. AreaofTriangle.py
```
FUNCTION Tri (base : real, height : real) RETURN REAL  
DECLARE T : REAL  
T = 0.5 * base * height  
RETURN T  
END FUNCTION  
PRINT CALL Tri (5,4)
```

## 29. Functions + Conditional Statement
```
FUNCTION max (a : INTEGER, b : INTEGER) : INTEGER
DECLARE c : INTEGER
IF a > b then
    c := a
else
    c := b
END IF
RETURN c
END FUNCTION
PRINT max (23,6)
```

## 30. Absolute Value
```
FUNCTION abs (x : REAL) : RETURN REAL
DECLARE B : REAL
IF x > 0 Then
    B := x
else
    B := -(x)
END IF
RETURN B
END FUNCTION
PRINT B (5)
```

## 31. FACTORIAL
```
FUNCTION factorial (n : INTEGER) RETURN INTEGER
DECLARE fact : INTEGER
SET fact = 1
FOR i in n to 1 step -1
    fact = fact * i
END FOR
RETURN fact

END FUNCTION
PRINT factorial (5)
```

## 32. Called with a = 9, b = 7
```
INTEGER funn (INTEGER a, INTEGER b)
DECLARE c : INTEGER
SET c = 2
b := b mod c
a := a mod c
RETURN a + b
END function
```

## 33. called with a = 9, b = 7, and c = 20
```
INTEGER funn (INTEGER a, INTEGER b, INTEGER c)
IF (a + 3) < (b - 2)
    c = 4 + b
    b = (c + c) + b
ELSE
    c = (a + 3) ^ 2
    c = (10 + 8) + b
END IF

return a + b + c

END fun
```
## 34. a = 5, b = 9, c = 2
```
INTEGER funn(INTEGER a, INTEGER b, INTEGER c)
FOR (each i from 4 to 8)
    a = (a + b) / b
    a = (c + b) + a
END FOR
b = (5 + 10) + a
a = (10 + b) + a
FOR (each c from 2 to 5)
    a = (c - 2) * a
    b = (3 * c) + a
END FOR
RETURN a + b
END funn

```

## 35.  sum the series 1....n
```
FUNCTION sum(n : INTEGER) : RETURN INTEGER
DECLARE s : INTEGER
SET s := 0
FOR i := 1 TO n
    s := s + i
END FOR
RETURN s
END FUNCTION
PRINT sum(5)
```

## 36. Sum the series 1/2 + 1/3 + .... + 1/n

```
FUNCTION sum (n : REAL) : RETURN REAL
DECLARE s : REAL
SET s := 0
FOR i := 1 TO n
    s := s + 1 / i
END FOR
RETURN s
END FUNCTION
PRINT sum(5)
```

## 37. reverse number

```
FUNCTION reverse (n : INTEGER) : RETURN INTEGER
DECLARE a : INTEGER
DECLARE b : INTEGER
SET b := 0
DECLARE x : INTEGER
SET x := n
WHILE x > 0 DO
    a := x MOD 10
    x := x / 10
    b := b * 10 + a
END WHILE
RETURN b
END FUNCTION
PRINT reverse(1234)
```

## 38. Palindrome
```
FUNCTION Palindrome (n : Integer)

DECLARE b : Integer
DECLARE x : Integer
DECLARE a : Integer
WHILE x > 0 DO
    a := n MOD 10
    n := n / 10
    b := b * 10 + a
END WHILE
RETURN b
IF b = n THEN
    PRINT Palindrome
ELSE
    PRINT Not a Palindrome
ENDIF
END Palindrome
PRINT Palindrome(121)
```

## 39. what will be the output of the following if a = 4, b = 4, c = 7 ?

```
INTEGER funn(INTEGER a, INTEGER b, INTEGER c)

for each c from 2 to 5
    if (c + a) > b then
        c = c + a + b
    if (a % c) < (c + a)
        b = (a + 1) + c
    else
        c = b + b
        a = a + b
        continue
    end if
end for
return a + b
```

## 40. If a = 3, b = 8, c = 7 
```
Integer funn (integer a, integer b, integer c)

if (a < b)
    c = a + 2
    c = a + c
end if

Return a + b + c
```

## 41. If whose will be the value of s if n = 12
```
Read n
s = 0 ; i = 0

while (i <= n)
    s = s + i * i
    i = i + 2
end while
```
