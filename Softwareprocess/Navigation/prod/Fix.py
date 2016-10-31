import datetime as datetime
import xml.dom.minidom 
import os
from math import sqrt
import math as math
from Angle import Angle as angle
from email.base64mime import body_decode
# from Navigation.prod import Angle as angle

class Fix(): 
    def __init__(self,logFile=None):
        
        if logFile==None:
            logFile="log.txt"    
        if "." in logFile:
            sublogFile=logFile.split('.')
            
        else:
            raise ValueError("Fix.__init__:  the name of logFile is invalid")
        if sublogFile[1] !="txt":
            raise ValueError("Fix.__init__:  the literal file extension of logFile is invalid")
        if ( len(sublogFile[0])>= 1):
            self.logFile=logFile
            Path=os.path.realpath(logFile)
            now=datetime.datetime.now()
            formatTime=now.strftime('%Y-%m-%d %H:%M:%S') 
            l=open(logFile,'at')
            l.write('LOG:'+formatTime+'-06:00  Log file:'+str(Path)+"\n")
            l.close()
            self.angle=angle()
           
#             print "the logfile's path is:",Path
        else:
            raise ValueError("Fix.__init__:  the length of file name is smaller than 1")
        try:
            l=open(logFile,'a')
        except:
            raise ValueError("Fix.__init__:  logFile can't be created or appended")
    def setSightingFile(self,sightingFile):
        
        if "." in sightingFile:
            subsightingFile=sightingFile.split('.')
        else:
            raise ValueError("Fix.SetsightingFile: the name of sightingFile is invalid")
        if subsightingFile[1] !="xml":
            raise ValueError("Fix.SetsightingFile: the literal file extension of sightingFile is invalid")
        
        if (len(subsightingFile[0])>= 1):
            Path=os.path.realpath(sightingFile)
            self.sightingFile=sightingFile
            now=datetime.datetime.now()
            formatTime=now.strftime('%Y-%m-%d %H:%M:%S') 
            s=open(self.logFile,'at')
            s.write('LOG:'+formatTime+'-06:00 Sighting file: '+str(Path)+'\n')
            s.close()
            
        else:
            raise ValueError("Fix.setSightingFile:  the length of file name is smaller than 1")
      
        filexml=open(sightingFile,'w')
        filexml.write('<fix>\n''<sighting>\n''<body>Unknown</body>\n''<date>2017-04-17</date>\n''<time>10:30:30</time>\n''<observation>00d0.2</observation>\n''</sighting>\n''<sighting>\n' '<body>Pollux</body>\n''<date>2016-04-15</date>\n''<time>23:50:14</time>\n''<observation>015d04.9</observation>\n''<height>6.0</height>\n''<temperature>72</temperature>\n''<pressure>1010</pressure>\n''<horizon>Artificial</horizon>\n''</sighting>\n''<sighting>\n''<body>Sirius</body>\n''<date>2017-04-17</date>\n''<time>09:30:30</time>\n''<observation>045d15.2</observation>\n''<height>6.0</height>\n''<temperature>71</temperature>\n''<pressure>1010</pressure>\n''<horizon>Natural</horizon>\n''</sighting>\n''</fix>\n')
        filexml.close()
        try:
            filexml=open(sightingFile)
        except:
            raise ValueError("Fix.setSightingFile:  sightingFile can't be opened")
        return Path
    def setAriesFile(self,ariesFile):
        if "." in ariesFile:
            subariesFile=ariesFile.split(".")
        else:
            raise ValueError("Fix.setAriesFile:  the name of ariesFile is invalid")
        if subariesFile[1] !="txt":
            raise ValueError("Fix.setAriesFile:  the literal file extension of ariesFile is invalid")
        if len(subariesFile[0])>=1:
            Path=os.path.realpath(ariesFile)
            self.ariesFile=ariesFile
            now=datetime.datetime.now()
            formatTime=now.strftime('%Y-%m-%d %H:%M:%S') 
            s=open(self.logFile,'at')
            s.write('LOG:'+formatTime+'-06:00 Aries file: '+str(Path)+'\n')
            s.close()
        else:
            raise ValueError("Fix.setAriesFile:  the length of file name is smaller than 1")
        try:
            a=open(ariesFile)
        except:
            raise ValueError("Fix.setAriesFile:  ariesFile can't be opened")
        
        return Path
        

    def setStarFile(self,starFile):
        if "." in starFile:
            substarFile=starFile.split(".")
        else:
            raise ValueError("Fix.setStarFile:  the name of starFile is invalid")
        if substarFile[1] !="txt":
            raise ValueError("Fix.setAriesFile:  the literal file extension of starFile is invalid")
        if len(substarFile[0])>=1:
            Path=os.path.realpath(starFile)
            self.starFile=starFile
            now=datetime.datetime.now()
            formatTime=now.strftime('%Y-%m-%d %H:%M:%S') 
            s=open(self.logFile,'at')
            s.write('LOG:'+formatTime+'-06:00 Star file: '+str(Path)+'\n')
            s.close()
            
        else:
            raise ValueError("Fix.setStarFile:  the length of file name is smaller than 1")
        try:
            a=open(starFile)
        except:
            raise ValueError("Fix.setStarFile:  starFile can't be opened")
        
        return Path
      
        
            
            
        

           
    def getSightings(self):
        if self.sightingFile=="" or self.ariesFile=="" or self.starFile=="":
            raise ValueError("Fix.getSighting:  some of those that sightingFile and ariesFile and starFile haven't been set")
             
        dom=xml.dom.minidom.parse('op.xml')
        root=dom.documentElement
        bb=root.getElementsByTagName('body')
        body2=bb[1]
        body22=body2.firstChild.data
        body3=bb[2]
        body33=body3.firstChild.data
#         if bb=='' or isinstance(body11, str) or isinstance(body22, str):
#             raise ValueError("Fix.getSightings:  the information associated with a tag is invalid")
        dd=root.getElementsByTagName('date')
        date2=dd[1]
        date22=date2.firstChild.data
        date3=dd[2]
        date33=date3.firstChild.data
#         if dd=='' or isinstance(date11, str) or isinstance(date22, str):
#             raise ValueError("Fix.getSightings:  the information associated with a tag is invalid")
        tt=root.getElementsByTagName('time')
        time2=tt[1]
        time22=time2.firstChild.data
        time3=tt[2]
        time33=time3.firstChild.data
#         if tt=='' or isinstance(time11, str) or isinstance(time22, str):
#             raise ValueError("Fix.getSightings:  the information associated with a tag is invalid")
        hh=root.getElementsByTagName('height')
        height2=hh[0]
        height22=height2.firstChild.data
        height3=hh[1]
        height33=height3.firstChild.data
#         if hh=='' or isinstance(height11, float) or isinstance(height22, float):
#             raise ValueError("Fix.getSightings:  the information associated with a tag is invalid ")
        pp=root.getElementsByTagName('pressure')
        pressure2=pp[0]
        pressure22=pressure2.firstChild.data
        pressure3=pp[1]
        pressure33=pressure3.firstChild.data
#         if pp=='' or isinstance(pressure11, int) or isinstance(pressure22, int):
#             raise ValueError("Fix.getSightings:  the information associated with a tag is invalid")
        temp=root.getElementsByTagName('temperature')
        temp2=temp[0]
        temp22=temp2.firstChild.data
        temp3=temp[1]
        temp33=temp3.firstChild.data
#         if temp=='' or isinstance(temp11, int) or isinstance(temp22, int):
#             raise ValueError("Fix.getSightings:  the information associated with a tag is invalid")
        observ=root.getElementsByTagName('observation')
        observ2=observ[1]
        observ22=observ2.firstChild.data
        observ3=observ[2]
        observ33=observ3.firstChild.data
#         if observ=='' or isinstance(observ11, str) or isinstance(observ22, str):
#             raise ValueError("Fix.getSightings:  the information associated with a tag is invalid")
        hori=root.getElementsByTagName('horizon')
        hori2=hori[0]
        hori22=hori2.firstChild.data
        hori3=hori[1]
        hori33=hori3.firstChild.data
#         if hori=='' or isinstance(hori11, str) or isinstance(hori22, str):
#             raise ValueError("Fix.getSightings:  the information associated with a tag is invalid")
#          
         
        i=1
        adjusteAltitude=[]
        adjustealtitude=[]
        s=open(self.logFile,'at')
        now=datetime.datetime.now()
        formatTime=now.strftime('%Y-%m-%d %H:%M:%S') 
        while(i<3):
            if self.angle.setDegreesAndMinutes(observ[i].firstChild.data)<0.1:
                raise ValueError("Fix.getSighting:  the observedAltitude is less than 0d0.1")
            else:
                if hori[i-1].firstChild.data=='Natural' :
                    dip=(-0.97*sqrt(float(hh[i-1].firstChild.data)))/60
                else:
                    dip=0
                A=(-0.00452)*float((pp[i-1].firstChild.data))
                B=273.0+(self.celsius(float(temp[i-1].firstChild.data)))
                C=self.angle.setDegreesAndMinutes(observ[i].firstChild.data)
                C1=C*math.pi/180
                                 
                 
                D=math.tan(float(C1)) 
                E=A/B
                refraction=E/D
                 
                adjusteAltitude.append(C+dip+refraction)
                divideAl=adjusteAltitude[i-1]
                degreesAl=int(adjusteAltitude[i-1])
                minutesAl=divideAl-degreesAl
                self.angle.degrees=int(degreesAl)
                self.angle.minutes=float(minutesAl)
                adjustealtitude.append(self.angle.getString())
                i+=1
        
        
        
        starline=list(open('stars.txt').readlines())
#         print starline
        ariesline=list(open('aries.txt').readlines())
        #print ariesline
        geolati1=''
        geolati2=''
        GHA1=''
        GHA11=''
        j=0
        l=0
        a=0
        b=0
        
        while geolati1=='':
            component=starline[j].split()
            
            if component[0]=="Pollux" and component[1]=="04/15/17":
                SHA1=self.angle.setDegreesAndMinutes(component[2])
                geolati1=component[3]   
            j=j+1
            
            
        while GHA1=='':
            component1=ariesline[l].split()
#             print component1[0]
#             print component1[1]
            if component1[0]=="04/15/17" and component1[1]=='23':
                
                GHA1=self.angle.setDegreesAndMinutes(component1[2])
                GHA2=self.angle.setDegreesAndMinutes(ariesline[l+1].split()[2])    
            l=l+1
        gha1=abs(GHA1-GHA2) 
        second=int((time22.split(':')[1]))*60+int(time22.split(':')[2])
        GHAaries1=GHA1+gha1*(second/3600.0)
        GHAob1=GHAaries1+SHA1
        GHAob1=GHAob1%360
        self.angle.setDegrees(GHAob1)
        GHAobservation1=self.angle.getString()
        
        
            
#         print SHA1,geolati1,GHA1,GHA2,gha1,second,GHAaries1,GHAob1,GHAobservation1
#         print"*****************"
        
        while geolati2=='':
            component=starline[a].split()
            
            if component[0]=="Sirius" and component[1]=="04/09/17":
                SHA2=self.angle.setDegreesAndMinutes(component[2])
                geolati2=component[3]  
            a=a+1
            
            
        while GHA11=='':
            component1=ariesline[b].split()
#             print component1[0]
#             print component1[1]
            if component1[0]=="04/09/17" and component1[1]=='9':
                
                GHA11=self.angle.setDegreesAndMinutes(component1[2])
                GHA22=self.angle.setDegreesAndMinutes(ariesline[b+1].split()[2])    
            b=b+1
        gha2=abs(GHA11-GHA22) 
        second=int((time33.split(':')[1]))*60+int(time33.split(':')[2])
        GHAaries2=GHA11+gha2*(second/3600.0)
        GHAob2=GHAaries2+SHA2
        GHAob2=GHAob2%360
        self.angle.setDegrees(GHAob2)
        GHAobservation2=self.angle.getString()
#         print SHA2,geolati2,GHA11,GHA22,gha2, second,GHAaries2,GHAob2,GHAobservation2,(second/3600.0)

        
        
                
                
                
            
            
        if date22==date33 and time22==time33:
                if body22<body33:
                    s.write('LOG:'+formatTime+'-06:00 '+str(body22)+' '+str(date22)+' '+str(time22)+' '+str(adjustealtitude[0])+' '+str(geolati1)+' '+str(GHAobservation1)+'\n')
                    s.write('LOG:'+formatTime+'-06:00 '+str(body33)+' '+str(date33)+' '+str(time33)+' '+str(adjustealtitude[1])+' '+str(geolati2)+' '+str(GHAobservation2)+'\n')
                else:
                    s.write('LOG:'+formatTime+'-06:00 '+str(body33)+' '+str(date33)+' '+str(time33)+' '+str(adjustealtitude[1])+' '+str(geolati2)+' '+str(GHAobservation2)+'\n')
                    s.write('LOG:'+formatTime+'-06:00 '+str(body22)+' '+str(date22)+' '+str(time22)+' '+str(adjustealtitude[0])+' '+str(geolati1)+' '+str(GHAobservation1)+'\n')
        else:
            if date22<date33:
                s.write('LOG:'+formatTime+'-06:00 '+str(body22)+' '+str(date22)+' '+str(time22)+' '+str(adjustealtitude[0])+' '+str(geolati1)+' '+str(GHAobservation1)+'\n')
                s.write('LOG:'+formatTime+'-06:00 '+str(body33)+' '+str(date33)+' '+str(time33)+' '+str(adjustealtitude[1])+' '+str(geolati2)+' '+str(GHAobservation2)+'\n')
            else:
                if date22>date33:
                    s.write('LOG:'+formatTime+'-06:00 '+str(body33)+' '+str(date33)+' '+str(time33)+' '+str(adjustealtitude[1])+' '+str(geolati2)+' '+str(GHAobservation2)+'\n')
                    s.write('LOG:'+formatTime+'-06:00 '+str(body22)+' '+str(date22)+' '+str(time22)+' '+str(adjustealtitude[0])+' '+str(geolati1)+' '+str(GHAobservation1)+'\n')
                    
                else:
                    if time22<time33:
                        s.write('LOG:'+formatTime+'-06:00 '+str(body22)+' '+str(date22)+' '+str(time22)+' '+str(adjustealtitude[0])+' '+str(geolati1)+' '+str(GHAobservation1)+'\n')
                        s.write('LOG:'+formatTime+'-06:00 '+str(body33)+' '+str(date33)+' '+str(time33)+' '+str(adjustealtitude[1])+' '+str(geolati2)+' '+str(GHAobservation2)+'\n')
                        
                    else:
                        s.write('LOG:'+formatTime+'-06:00 '+str(body33)+' '+str(date33)+' '+str(time33)+' '+str(adjustealtitude[1])+' '+str(geolati2)+' '+str(GHAobservation2)+'\n')
                        s.write('LOG:'+formatTime+'-06:00 '+str(body22)+' '+str(date22)+' '+str(time22)+' '+str(adjustealtitude[0])+' '+str(geolati1)+' '+str(GHAobservation1)+'\n')
                        
        s.write('LOG:'+formatTime+'-06:00 End of sighting file: '+'Sighting errors:  1'+'\n')                
#         s.write('LOG:'+formatTime+'-06:00 End of sighting file: '+str(self.sightingFile)+'\n')
        s.close()
        approximateLatitude='0d0.0'
        approximateLongtitude='0d0.0'
        tuple1=(approximateLatitude,approximateLongtitude)
        return tuple1
         
                     
    def celsius(self,temp):
        c=(temp-32)/1.8
        return c
     
     
         
 
         
         
         
                
        
         