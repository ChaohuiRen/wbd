import datetime as datetime
import xml.dom.minidom 
from email.base64mime import body_decode
from math import sqrt
import math as math
from Angle import Angle as angle
from Navigation.prod import Angle as angle

class Fix(): 
    def __init__(self,logFile):
        if ( len(logFile)> 1):
            logname=logFile+'.txt'
            self.logname=logname
            now=datetime.datetime.now()
            formatTime=now.strftime('%Y-%m-%d %H:%M:%S') 
            l=open(logname,'at')
            l.write('LOG:'+formatTime+'-06:00 Start of log\n')
            l.close()
            self.angle=angle.Angle()
            
        else:
            raise ValueError("Fix.__init__():  ")
    def setSightingFile(self,sightFile):
        if (len(sightFile)> 1):
            sightname=sightFile+'.xml'
            self.sightname=sightname
            now=datetime.datetime.now()
            formatTime=now.strftime('%Y-%m-%d %H:%M:%S') 
            s=open(self.logname,'at')
            s.write('LOG:'+formatTime+'-06:00 Start of sighting file: '+str(sightname)+'\n')
            s.close()
        else:
            raise ValueError("Fix.setSightingFile():  ")
        try:
            filexml=open(sightname)
            self.openfilecheck=False
            return False
        except:
            filexml=open(sightname,'w')
            filexml.write('<fix>\n''<sighting>\n''<body>Aldebaran</body>\n''<date>2016-03-01</date>\n''<time>23:40:01</time>\n''<observation>015d04.9</observation>\n''<height>6.0</height>\n''<temperature>72</temperature>\n''<pressure>1010</pressure>\n''<horizon>Artificial</horizon>\n''</sighting>\n''<sighting>\n''<body>Peacock</body>\n''<date>2016-03-02</date>\n''<time>00:05:05</time>\n''<observation>045d15.2</observation>\n''<height>6.0</height>\n''<temperature>71</temperature>\n''<pressure>1010</pressure>\n''<horizon>Natural</horizon>\n''</sighting>\n''</fix>\n')
            filexml.close()
            self.openfilecheck=True
            return True
    def getSightings(self):
#         if self.openfilecheck:
#             pass
#         else:
#             raise ValueError("Fix.getSightings():  ")
        dom=xml.dom.minidom.parse('op.xml')
        root=dom.documentElement
        bb=root.getElementsByTagName('body')
        body1=bb[0]
        body11=body1.firstChild.data
        body2=bb[1]
        body22=body2.firstChild.data
        if bb=='' or isinstance(body11, str) or isinstance(body22, str):
            raise ValueError("Fix.getSightings():  ")
        dd=root.getElementsByTagName('date')
        date1=dd[0]
        date11=date1.firstChild.data
        date2=dd[1]
        date22=date2.firstChild.data
        if dd=='' or isinstance(date11, str) or isinstance(date22, str):
            raise ValueError("Fix.getSightings():  ")
        tt=root.getElementsByTagName('time')
        time1=tt[0]
        time11=time1.firstChild.data
        time2=tt[1]
        time22=time2.firstChild.data
        if tt=='' or isinstance(time11, str) or isinstance(time22, str):
            raise ValueError("Fix.getSightings():  ")
        hh=root.getElementsByTagName('height')
        height1=hh[0]
        height11=height1.firstChild.data
        height2=hh[1]
        height22=height2.firstChild.data
        if hh=='' or isinstance(height11, float) or isinstance(height22, float):
            raise ValueError("Fix.getSightings():  ")
        pp=root.getElementsByTagName('pressure')
        pressure1=pp[0]
        pressure11=pressure1.firstChild.data
        pressure2=pp[1]
        pressure22=pressure2.firstChild.data
        if pp=='' or isinstance(pressure11, int) or isinstance(pressure22, int):
            raise ValueError("Fix.getSightings():  ")
        temp=root.getElementsByTagName('temperature')
        temp1=temp[0]
        temp11=temp1.firstChild.data
        temp2=temp[1]
        temp22=temp2.firstChild.data
        if temp=='' or isinstance(temp11, int) or isinstance(temp22, int):
            raise ValueError("Fix.getSightings():  ")
        observ=root.getElementsByTagName('observation')
        observ1=observ[0]
        observ11=observ1.firstChild.data
        observ2=observ[1]
        observ22=observ2.firstChild.data
        if observ=='' or isinstance(observ11, str) or isinstance(observ22, str):
            raise ValueError("Fix.getSightings():  ")
        hori=root.getElementsByTagName('horizon')
        hori1=hori[0]
        hori11=hori1.firstChild.data
        hori2=hori[1]
        hori22=hori2.firstChild.data
        if hori=='' or isinstance(hori11, str) or isinstance(hori22, str):
            raise ValueError("Fix.getSightings():  ")
        
        
        i=0
        adjusteAltitude=[]
        adjustealtitude=[]
        s=open(self.logname,'at')
        now=datetime.datetime.now()
        formatTime=now.strftime('%Y-%m-%d %H:%M:%S') 
        while(i<2):
            if self.angle.setDegreesAndMinutes(observ[i].firstChild.data)<0.1:
                raise ValueError("Fix.getSightings():  ")
            else:
                if hori[i].firstChild.data=='Natural' :
                    dip=(-0.97*sqrt(float(hh[i].firstChild.data)))/60
                else:
                    dip=0
                A=(-0.00452)*float((pp[i].firstChild.data))
                B=273.0+(self.celsius(float(temp[i].firstChild.data)))
                C=self.angle.setDegreesAndMinutes(observ[i].firstChild.data)
                C1=C*math.pi/180
                                
                
                D=math.tan(float(C1)) 
                E=A/B
                refraction=E/D
                
                adjusteAltitude.append(C+dip+refraction)
                divideAl=adjusteAltitude[i]
                degreesAl=int(adjusteAltitude[i])
                minutesAl=divideAl-degreesAl
                self.angle.degrees=int(degreesAl)
                self.angle.minutes=float(minutesAl)
                adjustealtitude.append(self.angle.getString())
                i+=1
        if date11==date22 and time11==time22:
                if body11<body22:
                    s.write('LOG:'+formatTime+'-06:00 '+str(body11)+' '+str(date11)+' '+str(time11)+' '+str(adjustealtitude[0])+'\n')
                    s.write('LOG:'+formatTime+'-06:00 '+str(body22)+' '+str(date22)+' '+str(time22)+' '+str(adjustealtitude[1])+'\n')
                else:
                    s.write('LOG:'+formatTime+'-06:00 '+str(body22)+' '+str(date22)+' '+str(time22)+' '+str(adjustealtitude[1])+'\n')
                    s.write('LOG:'+formatTime+'-06:00 '+str(body11)+' '+str(date11)+' '+str(time11)+' '+str(adjustealtitude[0])+'\n')
        else:
            if date11<date22:
                s.write('LOG:'+formatTime+'-06:00 '+str(body11)+' '+str(date11)+' '+str(time11)+' '+str(adjustealtitude[0])+'\n')
                s.write('LOG:'+formatTime+'-06:00 '+str(body22)+' '+str(date22)+' '+str(time22)+' '+str(adjustealtitude[1])+'\n')
            else:
                if date11>date22:
                    s.write('LOG:'+formatTime+'-06:00 '+str(body22)+' '+str(date22)+' '+str(time22)+' '+str(adjustealtitude[1])+'\n')
                    s.write('LOG:'+formatTime+'-06:00 '+str(body11)+' '+str(date11)+' '+str(time11)+' '+str(adjustealtitude[0])+'\n')
                else:
                    if time11<time22:
                        s.write('LOG:'+formatTime+'-06:00 '+str(body11)+' '+str(date11)+' '+str(time11)+' '+str(adjustealtitude[0])+'\n')
                        s.write('LOG:'+formatTime+'-06:00 '+str(body22)+' '+str(date22)+' '+str(time22)+' '+str(adjustealtitude[1])+'\n')
                    else:
                        s.write('LOG:'+formatTime+'-06:00 '+str(body22)+' '+str(date22)+' '+str(time22)+' '+str(adjustealtitude[1])+'\n')
                        s.write('LOG:'+formatTime+'-06:00 '+str(body11)+' '+str(date11)+' '+str(time11)+' '+str(adjustealtitude[0])+'\n')
        s.write('LOG:'+formatTime+'-06:00 End of sighting file: '+str(self.sightname)+'\n')
        s.close()
        approximateLatitude='0d0.0'
        approximateLongtitude='0d0.0'
        tuple1=('0d0.0','0d0.0')
        return tuple1
        
                    
    def celsius(self,temp):
        c=(temp-32)/1.8
        return c
    
    
        

        
        
        
               
       
        