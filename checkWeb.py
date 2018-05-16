import pickle
import httplib
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
import sys
tree = ET.parse('output.xml')
root = tree.getroot()
arr = []
newlist= []
#myfile = open('publicIP.txt', 'w')


def main():

    for node in root.findall('.//address'):
        #for l in app.findall('addr'):
        #arr.append(list(node.attrib["addr"]))
        arr = node.attrib["addr"]         
    

        try: 
            c = httplib.HTTPConnection(arr, timeout = 1)
            c.request("HEAD", '/')
            if c.getresponse().status == 200:
                
                with open('publicIP.txt','a+b') as file1:
                    file1.write(arr+'\n')
            
                print "written to file "+arr
                #with open("publicIP.txt", "w") as text_file:
                    #text_file.write(arr+'\n')

            else:

                print('nope'+arr)

            #with open("publicIP.txt", "a+b") as fp:
            #pickle.dump(arr, fp)


        except:


                pass
     
    


            #print('web site exists')
            #print('Nope') 



#def pingCheck():
#        c = httplib.HTTPConnection('www.google.com')
#        c.request("HEAD", '/')
#        if c.getresponse().status == 200:
#            print('web site exists')
#        else: 
#	    print('Nope')


#with open("publicIP.txt", "w") as text_file:
#    text_file.write(" Amount: %s")



main()
#test()

#myfile = open('publicIP.txt', 'w')
#myfile.write("hello%s\n" % arr)#
#myfile.close()
