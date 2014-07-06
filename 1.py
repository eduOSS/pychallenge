from multiprocessing import Process, Manager
import string,copy


def fun1(list1):
    for si in range(len(list1)):
        ssi = list1[si]
        osi = ord(ssi)
        if osi>96 and osi<121:
            list1[si]= chr(osi+2)
        elif osi>120 and osi<123:
            list1[si]= chr(osi-24)
    #list1 = ''.join(change_list)
    print ''.join(list1),'list1'

def fun2(list2):
    l = string.lowercase
    tran = string.maketrans(l,l[2:]+l[:2])
    string2 = ''.join(list2)
    list2 = copy.deepcopy(list(string2.translate(tran)))
    print ''.join(list2),'list2'

if '__main__'==__name__:
    input_string_file = open('1_in.txt')
    change_string = input_string_file.readline()
    input_string_file.close()
    #change_list = list(change_string)
    manager = Manager()

    change_list1= manager.list(change_string)
    p1 = Process(target=fun1,args=(change_list1,))
    p1.start()
    p1.join()
    print ''.join(change_list1),'main_list1\n'
    change_string1 = ''.join(change_list1)
    output_string_file = open('1.1_out.txt','w')
    output_string_file.write(change_string1)
    output_string_file.close()

    change_list2= manager.list(change_string)
    p2 = Process(target=fun2,args=(change_list2,))
    p2.start()
    p2.join()
    print ''.join(change_list2),'main_list2\n'
    change_string2 = ''.join(change_list2)
    output_string_file = open('1.2_out.txt','w')
    output_string_file.write(change_string2)
    output_string_file.close()

    
