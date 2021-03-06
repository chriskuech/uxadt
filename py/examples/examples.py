#####################################################################
## 
## examples.py
##
##   Small examples that illustrate how the uxadt.py module can be
##   used.
##
##

import uxadt
_ = None

#####################################################################
## Defining constructors in the local scope as stand-alone functions.
##

uxadt._({\
    'Red': [],\
    'Blue': []\
  })

## The algebraic data type name is optional; the first argument
## can be the type name, or it can be the dictionary defining the
## constructors:
##
##   uxadt._('Tree', {\
##       'Node': ['Tree', 'Tree'],\
##       'Leaf': []\
##     })
##
##   uxadt._({\
##       'Node': [_, _],\
##       'Leaf': []\
##     })
##
  
uxadt._('Tree', {\
    'Node': ['Tree', 'Tree'],\
    'Leaf': []\
  })

c0 = Red()
t0 = Node(Node(Leaf(), Leaf()), Node(Leaf(), Leaf()))
t1 = Leaf()
t2 = Node(Node(Leaf(), Leaf()), Leaf())

def size(t):
    return t\
        ._(Leaf(),     lambda:     1)\
        ._(Node(_, _), lambda x,y: 1 + size(x) + size(y))\
        .end

print("Example #1")
print(t0)
print(t0.toData())
t0.at('size', size(t0))
print(str(t0.at('size')))
print("")

#####################################################################
## Using alternate interface for pattern matching.
##

def width(t):
    if t < Leaf():
        return 1
    elif t < Node(_, _):
        (x, y) = t
        return width(x) + width(y)

print("Example #2")
print(str(t0) + " has width " + str(width(t0)) + ".")
print("")

#####################################################################
## Defining name-qualified constructors.
##

Color = uxadt.qualified('Color', {\
    'Red': [],\
    'Blue': []\
  })

uxadt.qualified('Tree', {\
    'Node': [_, _],\
    'Leaf': []\
  })

c0 = Color.Red()
t3 = Tree.Node(Tree.Node(Tree.Leaf(), Tree.Leaf()), Tree.Leaf())

def height(t):
    if t < Tree.Leaf():
        return 0
    elif t < Tree.Node(_, _):
        (x, y) = t
        return 1 + max(height(x), height(y))

print("Example #3")
print(c0)
print(str(t3) + " has height " + str(height(t3)) + ".")
print("")

#####################################################################
## Constructors wrapping values of other non-UxADT types.
##

uxadt._({\
    'Just': [_],\
    'Nothing': []\
  })

def unwrap(m):
    return m._(Just(_), lambda x: x).end

print("Example #4")
print(unwrap(Just(123)))
print(unwrap(Just('ABC')))
print(unwrap(Just(Just(['a', 'b', 'c']))))
print(Just(123).toData())
print(Just('ABC').toData())
print(Just(Just(['a', 'b', 'c'])).toData())
print("")

##eof
