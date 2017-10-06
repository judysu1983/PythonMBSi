import xml.etree.ElementTree as ETXML
import xml.etree.ElementTree as Element
import xml.etree.ElementTree as etree
import os


fullfilename=["EnvironmentAdminController.en-US.resx", "Error.en-US.resx", "_Layout.en-US.resx", "ComingSoon.en-US.resx", "Error.en-US.resx", "SharedResource.en-US.resx", "Index.en-US.resx", "Index.en-US.resx", "Legal.en-US.resx", "Provisioning.en-US.resx", "Index.en-US.resx"]
BaseName=["EnvironmentAdminController", "Error", "_Layout", "ComingSoon", "Error", "SharedResource", "Index", "Index", "Legal", "Provisioning", "Index"]
sourcelocation=["[git_OOBAPPs]\HCMFabric\Source\HCMLandingClientService\Resources\Controllers", "[git_OOBAPPs]\HCMFabric\Source\HCMMarketingClientService\Resources\Views\Shared", "[git_OOBAPPs]\HCMFabric\Source\HCMLandingClientService\Resources\Views\Shared", "[git_OOBAPPs]\HCMFabric\Source\HCMLandingClientService\Resources\Views\Shared", "[git_OOBAPPs]\HCMFabric\Source\HCMLandingClientService\Resources\Views\Shared", "[git_OOBAPPs]\HCMFabric\Source\HCMLandingClientService\Resources", "[git_OOBAPPs]\HCMFabric\Source\HCMMarketingClientService\Resources\Views\Home", "[git_OOBAPPs]\HCMFabric\Source\HCMLandingClientService\Resources\Views\Home", "[git_OOBAPPs]\HCMFabric\Source\HCMLandingClientService\Resources\Views\Home", "[git_OOBAPPs]\HCMFabric\Source\HCMLandingClientService\Resources\Views\Home", "[git_OOBAPPs]\HCMFabric\Source\HCMLandingClientService\Resources\Views\EnvironmentAdmin"]
ExtensionName="resx"
TargetLclLocation=["Source\HCMLandingClientService\Resources\Controllers", "Source\HCMMarketingClientService\Resources\Views\Shared", "Source\HCMLandingClientService\Resources\Views\Shared", "Source\HCMLandingClientService\Resources\Views\Shared", "Source\HCMLandingClientService\Resources\Views\Shared", "Source\HCMLandingClientService\Resources", "Source\HCMMarketingClientService\Resources\Views\Home", "Source\HCMLandingClientService\Resources\Views\Home", "Source\HCMLandingClientService\Resources\Views\Home", "Source\HCMLandingClientService\Resources\Views\Home", "Source\HCMLandingClientService\Resources\Views\EnvironmentAdmin"]

root=ETXML.Element('EOL')
for i in range(0,11):
    sub=ETXML.SubElement(root, "File", name=fullfilename[i], parser="[parser.Txt]", noType="Comments")
    #ETXML.SubElement(sub, "File", name="BusinessProcess.en-US.label.txt" parser="[parser.Txt]" noType="Comments").text='\n'
    #ETXML.SubElement(sub, "File", name=fullfilename, parser="[parser.Txt]", noType="Comments").text = "\n"
    ETXML.SubElement(sub, "Var", name="File.SourceBinary").text = sourcelocation[i]
    ETXML.SubElement(sub, "Var", name="File.BaseName").text = BaseName[i]
    ETXML.SubElement(sub, "Var", name="File.ExtensionName").text = ExtensionName
    ETXML.SubElement(sub, "Var", name="File.TargetLclLocation").text = TargetLclLocation[i]

rootWrite=ETXML.ElementTree(root)
rootWrite.write('aFile.xml')
