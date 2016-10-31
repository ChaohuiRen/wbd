import unittest
import Navigation.prod.Fix as F
import os


class Fixunittest(unittest.TestCase):
    
    def setup (self):
        pass
    
    def teardown(self):
        pass

#-------------Acceptance Tests---------------
#100 constructor
#    input-output analysis
#        inputs: logFile -> name is a String   optional ,  length. G.E. 1 , unvalidated
#                            defaults: log.txt if Missing.   
#        output: instance of Fix
#    Happy Path analysis:
#            omitted   -> Fix()
#            newfilename    -> Fix("myFile")
#            exsistingfile     -> Fix("myFile")  exist
#    Sad Path analysis:
#            non-string   name=4  
#                         name=3.62
#            the information not write in the file
#
#Happy path
    def test100_010_ShouldConstruct(self):
        self.assertIsInstance(F.Fix("logFile"), F.Fix)
    
    def test100_020_ShouldConstruct(self):
        self.assertIsInstance(F.Fix(), F.Fix)
        
    def test100_030_ShouldCreateNewFile(self):
        self.assertIsInstance(F.Fix("myFile"), F.Fix)
        
    def test100_040_ShouldAppendExistFile(self):
        self.assertIsInstance(F.Fix("myFile"), F.Fix) 
        
#Sad path
    def test100_910_CantBeCreatedOrAppended(self):
        expectedString="Fix.__init__:"
        with self.assertRaises(ValueError) as context:
            F.Fix(4)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def test100_920_CantBeCreatedOrAppended(self):
        expectedString="Fix.__init__:"
        with self.assertRaises(ValueError) as context:
            F.Fix(3.62)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
        
    def test100_930_CantBeCreatedOrAppended(self):
        myF=open("myFile",'r')
        expectedString="Fix.__init__:"
        with self.assertRaises(ValueError) as context:
            F.Fix(myF)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])



#200 constructor
#    input-output analysis
#        inputs: sightingFile -> name is a String , f length. G.E. 1 , ".xml" is file extension mandatory,unvalidated   
#        output: a string
#    Happy Path analysis:
#            name="peacock.xml"
#            name="StarSighting.xml"
#            name="f.xml"
#    Sad Path analysis:
#           non-string ->  name=32  
#                          name=4.6
#           string name length L.T. 1  ->     name=""    
#           string which doesn't contain ".xml"  ->     name="Sirius"
#           file is not exists  ->    n
#           file can't be opened  ->
#
#Happy path
    def test200_010_Source(self):
        myFile=F.Fix("logFile")
        self.assertEquals(myFile.setSightingFile("peacock.xml"),"peacock.xml")
        self.assertEquals(myFile.setSightingFile("StarSighting.xml"),"StarSighting.xml")       
        self.assertEquals(myFile.setSightingFile("f.xml"),"f.xml")
        
#Sad path
    def test200_910_FileNameIsWrong(self):
        myFile=F.Fix("LOGFILE")
        expectedString="Fix.setSightingFile"
        with self.assertRaises(ValueError) as context:
            myFile.setSightingFile("32")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
        
    def test200_920_FileNameIsWrong(self):
        myFile=F.Fix("LOGFILE")
        expectedString="Fix.setSightingFile"
        with self.assertRaises(ValueError) as context:
            myFile.setSightingFile("4.6")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
        
    def test200_930_FileNameIsWrong(self):
        myFile=F.Fix("LOGFILE")
        expectedString="Fix.setSightingFile"
        with self.assertRaises(ValueError) as context:
            myFile.setSightingFile("")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
        
    def test200_940_FileNameIsWrong(self):
        myFile=F.Fix("Star")
        expectedString="Fix.setSightingFile"
        with self.assertRaises(ValueError) as context:
            myFile.setSightingFile("Sirius")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])   

    def test200_950_FileNameIsWrong(self):
        myFile=F.Fix("Star")
        expectedString="Fix.setSightingFile"
        with self.assertRaises(ValueError) as context:
            myFile.setSightingFile("f.doc")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])         
#file can't be opened left

        
#300 constructor
#    input-output analysis
#        input: /
#        output: returns a tuple consists of latitude and longitude of location
#    Happy path
#        return tuple   ->0d0.0
#        file has been set  ->has content
#        
#    Sad path
#        no sightingFile    
#        without mandatory tag
#        observed altitude L.T. 0.1minite
#Happy path
        
    def test300_010_sightingFileIsSet(self):
        pass
        
        
#Sad path        
        
        
        