import os
import re

def genXML(name):

    xml_file=name
    xml_file="converted" + name
    xml_file=xml_file.strip('py') +'xml'
    f=open(xml_file,'w+')
    
    with open(os.path.join('statics' , name)) as models:
        Lines = models.readlines() 

        fieldDetails=""
        stringToAppend = ""
        menuItems = list()
        fieldProperies = list()

        startFlag = 0
        flag = 0;
        myflag=0
        f.write('<XML_DOC>' + '\n')

        f.write('<Entities>' + '\n\n')

        for line in Lines:
            if line.strip():
                if line.strip()[0] != '#' and line.strip()[0:3] !="'''":
                    if re.match('class',line) or myflag:
                        myflag=1

                        if flag or re.match('class',line):
                            flag =1
                            if re.match('class',line):
                                f.write(fieldDetails[:-1])
                                if startFlag:    
                                    f.write('</Fields>' + '\n')

                                startFlag = 1
                                
                                modelName  = line.split('(')[0].split(" ")[-1]
                                displayName = line.split('#')[-1].strip()
                                stringToAppend = "<Fields type='"+modelName+"' class='EntityProperties' displayProperty='"+displayName+"'>"

                                menuItems.append("<Item class='menus' displayName='"+displayName+"' target='displayRecord.html?entityType="+modelName+"' id='id_"+modelName+"'> </Item>" + '\n')

                                f.write(stringToAppend)
                                stringToAppend = ""
                                fieldDetails = ""
                            else:
                                fieldDisplayName = ''
                                if re.match(r'#',line):
                                    fieldDetails += line.split('=')[0].strip()+line.split('#')[1].strip()+","
                                    fieldDisplayName = line.split('#')[1].split('$$')[-1].strip()
                                fieldName = line.split('=')[0].strip()
                                fieldDetails += line.split('=')[0].strip() + ','
                               
                                fieldProperies.append("<DisplayText class='DisplayText' fieldName='"+modelName+"."+fieldName+"' displayName='"+fieldDisplayName+"'></DisplayText>" + '\n')
                
        f.write(fieldDetails[:-1])
        f.write('</Fields>' + '\n')
        f.write('</Entities>' + '\n')

        f.write('<Menus>' + '\n')    
        f.write("<Item class='menus' displayName='Set Data Location' target='SetLocation.html' id='setLocation'></Item> " + '\n')
        for item in menuItems:
            f.write(item)
        f.write('</Menus>' + '\n')

        f.write('<FieldProperties>' + '\n')
        for item in fieldProperies:
            f.write(item)
        f.write('</FieldProperties>' + '\n')

        f.write('<EntityRecordSet>' + '\n')
        f.write('//cursor' + '\n')
        f.write('</EntityRecordSet>' + '\n')
        f.write('</XML_DOC>' + '\n')
           
        f.close()
        return xml_file
        
