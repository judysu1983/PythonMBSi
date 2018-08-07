import xml.etree.ElementTree as ETXML
import xml.etree.ElementTree as Element
import xml.etree.ElementTree as etree
import os


fullfilename=["Index.resx", "Index.resx", "Index.resx", "SubPagesNavigation.resx", "Offers.resx", "CallToAction.resx", "Index.resx", "Index.resx", "Index.resx", "Jobroles.resx", "CompanySize.resx", "Index.resx", "Index.resx"]
BaseName=["Index", "Index", "Index", "SubPagesNavigation", "Offers", "CallToAction", "Index", "Index", "Index", "Jobroles", "CompanySize", "Index", "Index"]
sourcelocation=["dynamics365-shared\Dynamics365.Resources\Pages\Sales\Capabilities", "dynamics365-shared\Dynamics365.Resources\Pages\Retail\Resources", "dynamics365-shared\Dynamics365.Resources\Pages\AI", "dynamics365-shared\Dynamics365.Resources\Controls", "dynamics365-shared\Dynamics365.Resources\Controls", "dynamics365-shared\Dynamics365.Resources\Controls", "dynamics365-shared\Dynamics365.Resources\Pages\Request-Trial\Thank-You", "dynamics365-shared\Dynamics365.Resources\Pages\Request-Trial", "dynamics365-shared\Dynamics365.Resources\Pages\Talent\Core-HR", "dynamics365-shared\Dynamics365.Resources\Shared", "dynamics365-shared\Dynamics365.Resources\Shared", "dynamics365-shared\Dynamics365.Resources\Pages\Sales\Role\Sales-Leaders", "dynamics365-shared\Dynamics365.Resources\Pages\Sales\Overview"]
ExtensionName="resx"
AreaPath=["Dynamics365.Resources_Pages_Sales_Capabilities", "Dynamics365.Resources_Pages_Retail_Resources", "Dynamics365.Resources_Pages_AI", "Dynamics365.Resources_Controls", "Dynamics365.Resources_Controls", "Dynamics365.Resources_Controls", "Dynamics365.Resources_Pages_Request-Trial_Thank-You", "Dynamics365.Resources_Pages_Request-Trial", "Dynamics365.Resources_Pages_Talent_Core-HR", "Dynamics365.Resources_Shared", "Dynamics365.Resources_Shared", "Dynamics365.Resources_Pages_Sales_Role_Sales-Leaders", "Dynamics365.Resources_Pages_Sales_Overview"]

root=ETXML.Element('EOL')
for i in range(0,13):
    sub=ETXML.SubElement(root, "Area", name=AreaPath[i])
    itemgroup=ETXML.SubElement(sub, "ItemGroup")
    locextent=ETXML.SubElement(itemgroup,"LocExtent",derivation="Translate").text ="[lg.1]"
    locextent=ETXML.SubElement(itemgroup,"LocExtent",derivation="Adapt", parentCulture="en-US").text ="en-AU;en-CA;en-GB;en-IE;en-IN;en-MY;en-NZ;en-SG;en-ZA"
    locextent=ETXML.SubElement(itemgroup,"LocExtent",derivation="Adapt", parentCulture="es").text ="es-MX"
    locextent=ETXML.SubElement(itemgroup,"LocExtent",derivation="Adapt", parentCulture="it").text ="it-CH"
    locextent=ETXML.SubElement(itemgroup,"LocExtent",derivation="Adapt", parentCulture="nl").text ="nl-BE"
    locextent=ETXML.SubElement(itemgroup,"LocExtent",derivation="Adapt", parentCulture="fr").text ="fr-BE;fr-CA;fr-CH"
    locextent=ETXML.SubElement(itemgroup,"LocExtent",derivation="Adapt", parentCulture="de").text ="de-CH;de-AT"
    
    fileitem=ETXML.SubElement(itemgroup,"File", name=fullfilename[i], parser="[parser.Managed]")
    #ETXML.SubElement(sub, "File", name="BusinessProcess.en-US.label.txt" parser="[parser.Txt]" noType="Comments").text='\n'
    #ETXML.SubElement(sub, "File", name=fullfilename, parser="[parser.Txt]", noType="Comments").text = "\n"
    ETXML.SubElement(fileitem, "Var", name="File.SourceLCG").text = sourcelocation[i]
    ETXML.SubElement(fileitem, "Var", name="File.SourceBinary").text = sourcelocation[i]
    ETXML.SubElement(fileitem, "Var", name="File.TargetCheckInLocation").text = sourcelocation[i]
    ETXML.SubElement(fileitem, "Var", name="File.BaseName").text = BaseName[i]
    ETXML.SubElement(fileitem, "Var", name="File.ExtensionName").text = ExtensionName
    ETXML.SubElement(fileitem, "Var", name="File.Branch").text = "master"

rootWrite=ETXML.ElementTree(root)
rootWrite.write('aaFile.xml')
