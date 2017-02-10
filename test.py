#coding: UTF-8
'''
Created on Nov 27, 2016

@author: jinhua
'''

def printinfo(lista):
    print 'A test of Python function.';
    print lista[1];
    return;

def addition(a,b):
    total = a+b;
    return total;

if __name__ == '__main__':
    pass
    print 'こんにちは　世界';
    'n = raw_input("please input you word.-->");'
    'print n;'
    a=b=c=100;
    print a;print b;print c;print '\n';
    'this is a comment'
    arr=(1,2,3,4,5,6,7,8,9,10);
    lista = ['one','two','three'];
    dic = {'a':'abandon','b':'brand','c':'country'};
    'delete the second member of lista'
    del lista[1];
    print 'firstly output the 2nd number of arr %d, then lista %s, at last dic %s'%(arr[1],lista[1],dic['a']);
    printinfo(lista);
    print addition(10,20);
    print addition(a=40,b=50);
    print addition(20,50);


    