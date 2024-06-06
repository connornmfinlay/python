import xml.etree.ElementTree as ET
from xml.dom import minidom

def create_start_menu_xml():
    # Define the namespaces
    namespaces = {
        'defaultlayout': 'http://schemas.microsoft.com/Start/2014/FullDefaultLayout',
        'start': 'http://schemas.microsoft.com/Start/2014/StartLayout'
    }

    # Register the namespaces
    for prefix, uri in namespaces.items():
        ET.register_namespace(prefix, uri)

    # Create the root element
    root = ET.Element("LayoutModificationTemplate", 
                      Version="1", 
                      xmlns="http://schemas.microsoft.com/Start/2014/LayoutModification")

    # Add LayoutOptions element
    layout_options = ET.SubElement(root, "LayoutOptions", StartTileGroupCellWidth="6")

    # Add DefaultLayoutOverride element
    default_layout_override = ET.SubElement(root, "DefaultLayoutOverride")
    start_layout_collection = ET.SubElement(default_layout_override, "StartLayoutCollection")
    
    # Add StartLayout element
    start_layout = ET.SubElement(start_layout_collection, "{http://schemas.microsoft.com/Start/2014/FullDefaultLayout}StartLayout", 
                                 GroupCellWidth="6")
    
    # Define groups and tiles
    groups = {
        "Office 2019": [
            {"Size": "1x1", "Column": "2", "Row": "1", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\OneNote.lnk"},
            {"Size": "2x2", "Column": "0", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Word.lnk"},
            {"Size": "2x2", "Column": "3", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Excel.lnk"},
            {"Size": "1x1", "Column": "5", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Accessories\Calculator.lnk"},
            {"Size": "1x1", "Column": "5", "Row": "1", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Accessories\Snipping Tool.lnk"},
            {"Size": "1x1", "Column": "2", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"}
        ],
        "Browsers": [
            {"Size": "2x2", "Column": "4", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk"},
            {"Size": "2x2", "Column": "0", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Firefox.lnk"},
            {"Size": "2x2", "Column": "2", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"}
        ],
        "Development Tools": [
            {"Size": "1x1", "Column": "3", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Sublime Text.lnk"},
            {"Size": "1x1", "Column": "1", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\EUROMOD\EUROMOD.lnk"},
            {"Size": "1x1", "Column": "4", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Python 3.12\Python 3.12 (64-bit).lnk"},
            {"Size": "1x1", "Column": "5", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Git\Git GUI.lnk"},
            {"Size": "1x1", "Column": "0", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2023.3.4.lnk"},
            {"Size": "1x1", "Column": "2", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk"}
        ],
        "R": [
            {"Size": "2x2", "Column": "2", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\RStudio\RStudio.lnk"},
            {"Size": "2x2", "Column": "4", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Rtools 4.3\Rtools43 Bash.lnk"},
            {"Size": "2x2", "Column": "0", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\R\R 4.3.1.lnk"}
        ],
        "Misc Tools": [
            {"Size": "1x1", "Column": "2", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Adobe Acrobat.lnk"},
            {"Size": "1x1", "Column": "3", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Notepad++.lnk"},
            {"Size": "1x1", "Column": "1", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\MicroDicom DICOM Viewer (64-bit)\MicroDicom DICOM Viewer (64-bit).lnk"},
            {"Size": "1x1", "Column": "4", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\QGIS 3.34.4\QGIS Desktop 3.34.4.lnk"},
            {"Size": "1x1", "Column": "0", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\7-Zip\7-Zip File Manager.lnk"},
            {"Size": "1x1", "Column": "5", "Row": "0", "Path": r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\jamovi\jamovi 2.3.28.lnk"}
        ]
    }

    # Add groups and tiles to the XML
    for group_name, tiles in groups.items():
        group = ET.SubElement(start_layout, "{http://schemas.microsoft.com/Start/2014/StartLayout}Group", Name=group_name)
        for tile in tiles:
            ET.SubElement(group, "{http://schemas.microsoft.com/Start/2014/StartLayout}DesktopApplicationTile", 
                          Size=tile["Size"], 
                          Column=tile["Column"], 
                          Row=tile["Row"], 
                          DesktopApplicationLinkPath=tile["Path"])

    # Convert the XML tree to a string and pretty-print it
    xml_str = ET.tostring(root, encoding='utf-8', method='xml')
    parsed_xml = minidom.parseString(xml_str)
    pretty_xml_str = parsed_xml.toprettyxml(indent="  ")

    # Write the string to an XML file
    with open("StartMenuLayout.xml", "w", encoding='utf-8') as xml_file:
        xml_file.write(pretty_xml_str)

    print("Start Menu layout XML created successfully!")

if __name__ == '__main__':
    create_start_menu_xml()
