from operators import add, mul
from logic import and_, or_

def main():
        print "My application starts..."
        a=2
        b=3
        x=true
        y=false
        print add(a,b)
        print mul(x,y)
        print add_(x,y)
        print or_(x,y)
        

if __name__ == "__main__":
        main()
