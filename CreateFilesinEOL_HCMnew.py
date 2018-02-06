import xml.etree.ElementTree as ETXML
import xml.etree.ElementTree as Element
import xml.etree.ElementTree as etree
import os
##fullfilename=["BusinessProcess.en-US.label.txt", "BusinessProcess.en-US.label.txt"]
##sourcelocation=["[git_OOBAPPs]\HCM\source\metadata\BusinessProcess\BusinessProcess\AxLabelFile\LabelResources\en-US","test"]
##BaseName=["BusinessProcess","testBasename"]
##ExtensionName="label.txt"
##TargetLclLocation= ["BusinessProcess\BusinessProcess\AxLabelFile\LabelResources","test2"]



#fullfilename=["PersonnelCore.en-US.label.txt", "HcmPeopleNavigatorControl.en-US.label.txt", "HcmPersonCard.en-US.label.txt", "TaxEngineConfiguration.en-US.label.txt", "TaxEngine.en-US.label.txt", "TaxEngineInterface.en-US.label.txt", "TaxSettlement.en-US.label.txt", "GetStarted.en-US.label.txt", "SysBasicUpgrade.en-US.label.txt"]
fullfilename=["Ledger.en-us.label.txt", "Measurement.en-us.label.txt", "AccountingFramework.en-us.label.txt", "SourceDocumentation.en-us.label.txt", "TaxEngineIntegration_SourceDoc.en-us.label.txt", "TaxEngineIntegration_SourceDocTypes.en-us.label.txt", "Subledger.en-us.label.txt"]
sourcelocation=["[git_OOBAPPs]\HCM\source\metadata\PersonnelCore\PersonnelCore\AxLabelFile\LabelResources\en-US", "[git_OOBAPPs]\HCM\source\metadata\PersonnelManagement\PersonnelManagement\AxLabelFile\LabelResources\en-us", "[git_OOBAPPs]\HCM\source\metadata\PersonnelManagement\PersonnelManagement\AxLabelFile\LabelResources\en-us", "[git_OOBAPPs]\ElectronicReporting\source\metadata\TaxEngine\TaxEngine\AxLabelFile\LabelResources\en-US", "[git_OOBAPPs]\ElectronicReporting\source\metadata\TaxEngine\TaxEngine\AxLabelFile\LabelResources\en-US", "[git_OOBAPPs]\ElectronicReporting\source\metadata\TaxEngine\TaxEngine\AxLabelFile\LabelResources\en-US", "[git_OOBAPPs]\ElectronicReporting\source\metadata\TaxEngine\TaxEngine\AxLabelFile\LabelResources\en-US", "[git_OOBAPPs]\ApplicationCommon\source\metadata\ApplicationCommon\ApplicationCommon\AxLabelFile\LabelResources\en-US", "[git_OOBAPPs]\ApplicationCommon\source\metadata\SysBasicUpgrade\SysBasicUpgrade\AxLabelFile\LabelResources\en-US"]
#BaseName=["PersonnelCore", "HcmPeopleNavigatorControl", "HcmPersonCard", "TaxEngineConfiguration", "TaxEngine", "TaxEngineInterface", "TaxSettlement", "GetStarted", "SysBasicUpgrade"]
BaseName=["Ledger", "Measurement", "AccountingFramework", "SourceDocumentation", "TaxEngineIntegration_SourceDoc", "TaxEngineIntegration_SourceDocTypes", "Subledger"]
ExtensionName="label.txt"
TargetLclLocation= ["HCM\source\metadata\PersonnelCore\PersonnelCore\AxLabelFile\LabelResources", "HCM\source\metadata\PersonnelManagement\PersonnelManagement\AxLabelFile\LabelResources", "HCM\source\metadata\PersonnelManagement\PersonnelManagement\AxLabelFile\LabelResources", "ElectronicReporting\source\metadata\TaxEngine\TaxEngine\AxLabelFile\LabelResources", "ElectronicReporting\source\metadata\TaxEngine\TaxEngine\AxLabelFile\LabelResources", "ElectronicReporting\source\metadata\TaxEngine\TaxEngine\AxLabelFile\LabelResources", "ElectronicReporting\source\metadata\TaxEngine\TaxEngine\AxLabelFile\LabelResources", "ApplicationCommon\source\metadata\ApplicationCommon\ApplicationCommon\AxLabelFile\LabelResources", "ApplicationCommon\source\metadata\SysBasicUpgrade\SysBasicUpgrade\AxLabelFile\LabelResources"]

root=ETXML.Element('EOL')
for i in range(0,7):
    sub=ETXML.SubElement(root, "File", name=fullfilename[i], parser="[parser.Txt]", noType="Comments")
    #ETXML.SubElement(sub, "File", name="BusinessProcess.en-US.label.txt" parser="[parser.Txt]" noType="Comments").text='\n'
    #ETXML.SubElement(sub, "File", name=fullfilename, parser="[parser.Txt]", noType="Comments").text = "\n"
    ETXML.SubElement(sub, "Var", name="File.SourceBinary").text = sourcelocation[i]
    ETXML.SubElement(sub, "Var", name="File.BaseName").text = BaseName[i]
    ETXML.SubElement(sub, "Var", name="File.ExtensionName").text = ExtensionName
    ETXML.SubElement(sub, "Var", name="File.TargetLclLocation").text = TargetLclLocation[i]

rootWrite=ETXML.ElementTree(root)
rootWrite.write('aFile.xml')
