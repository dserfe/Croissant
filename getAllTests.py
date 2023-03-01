from posixpath import split
from bs4 import BeautifulSoup
import os
import sys
import csv


all_results=[]
surefire_dirs=[]
test_classes=[]
def get_all_xml(project_dir,csv_dir):
    project=project_dir.split('/')[-1]

    for dirs in os.walk(project_dir):
        if "target/surefire-reports" in dirs[0]:
               surefire_dirs.append(dirs[0])

    all_tests_save_csv=csv_dir+'/all_tests_'+project+'.csv'
    withnumbers_csv = csv_dir+'/all_tests_with_nums'+project+'.csv'
    with open(all_tests_save_csv,"w",newline='') as tests_csv:
        with open(withnumbers_csv,"w",newline='') as tests_csv2:
            writer = csv.writer(tests_csv)
            writer2 = csv.writer(tests_csv2)
            print(all_tests_save_csv)
            print(project)
        
            for eachsurefire_dir in surefire_dirs:
                files = os.listdir(eachsurefire_dir)
                for eachfile in files:
                    if eachfile.endswith('.txt'):
                        file_path = os.path.join(eachsurefire_dir, eachfile)

                        file = open(file_path,"r")
                        lines = file.read().splitlines()
                        file.close()
                        testRuns = 0

                        for line in lines:
                            if 'Tests run:' in line:
                                testRuns = line.split(',')[0].split(':')[-1].strip()


                        module = eachsurefire_dir.replace('surefire-reports','').replace('.','')
                        testClass = '.'.join(eachfile.split('.')[0:-1])
                        if "commons-math/commons-math-legacy/target/" not in module and "commons-math/commons-math-core/target/" not in module and "commons-math/commons-math-transform/target/" not in module:
                            writer.writerow([module,testClass,testRuns])  
                            writer2.writerow([module,testClass,testRuns])                   

get_all_xml(sys.argv[1],sys.argv[2])
