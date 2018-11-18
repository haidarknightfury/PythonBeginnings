# Loops

## For Loops 

- range(101)
    - A sequence of integers from 0 to 100 can be generated.
- range(1, 100)
    - A sequence of integers from 1 to 99 can be generated.
- range(1, 100, 2)
    - An odd sequence of 1 to 99 can be generated, where 2 is the step size, ie   the increment of the sequence of values.

```python
    Sum  =  0 
    for x in  range ( 101 ):
	 sum  += x
    print ( sum )
```

## While Loops

- break to break out of loops
- continue to skip rest of loop and move to next cycle

```python 
Import random

Answer = random.randint( 1 , 100 )
Counter =  0 
while  True :
	Counter +=  1 
	number =  int ( input ( ' Please enter: ' ))
	 if number < answer:
		 print ( ' bigger ' )
	 elif number > answer:
		 print ( ' small ' )
	 else :
		 print ( ' Congratulations you guess up! ' )
		 break 
print ( ' you guess the total of % d times '  % counter)
if Counter >  7 :
    print ( ' Your IQ balance is obviously insufficient ' )
```



