# -*- coding: UTF-8 -*-  

import sys

import cognitive_face as CF

if len(sys.argv) < 2: #len小於2也就是不帶參數啦

 print 'no argument'

 sys.exit()

if sys.argv[1].startswith('--'):

 option = sys.argv[1][2:] # 取出sys.argv[1]的數值但是忽略掉'--'這兩個字元

 if option == 'version': 

  print 'Version 1.0'

 if option == 'create_list':
     CF.face_list.create("NCKU")

 if option == 'add_face':
     CF.face_list.add_face(sys.argv[2][:], 'NCKU')

 elif option == 'help':

  print 'Usage : [--version] [--create_list] [--add_face [face_id]]'

 else:

  print 'only --version --help can be used'

  sys.exit()