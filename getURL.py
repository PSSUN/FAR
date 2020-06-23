#!usr/bin/python3
import argparse


def readfile(file):
    link_1 = []
    link_2 = []
    link_3 = []
    command = 'wget -nc '
    forward = 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/'
    back = '.fastq.gz &'
    list_1 = []

    for i in file:
        list_1.append(i.strip('\n'))
    for i in list_1:
        link_1.append(command + forward + str(i[0:6]) + '/' + str(i) + '/' + str(i) + back)
        link_2.append(command + forward + str(i[0:6]) + '/0' + str(i[-2:]) + '/' + str(i) + '/' + str(i) + back)
        link_3.append(command + forward + str(i[0:6]) + '/00' + str(i[-1:]) + '/' + str(i) + '/' + str(i) + back)
    final_list = link_2 + link_1 + link_3
    return final_list


def writefile(x):
    f1 = open('result.csv', 'w+')
    for i in x:
        f1.write(i)
        f1.write('\n')
    f1.close()


if __name__ == '__main__':
    parse = argparse.ArgumentParser('Generate url link of EBI from SRRid')
    parse.add_argument('-f', dest='file', required=True, help='SRRid file')
    arg = parse.parse_args()
    file = open(arg.file)
    f_list = readfile(file)
    writefile(f_list)
