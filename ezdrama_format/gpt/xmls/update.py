import os
import xml.etree.ElementTree as ET

def update_title_in_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    # Find the <fileDesc> element or create it if it doesn't exist
    filedesc_elem = root.find(".//{http://www.tei-c.org/ns/1.0}fileDesc")
    if filedesc_elem is None:
        filedesc_elem = ET.Element("{http://www.tei-c.org/ns/1.0}fileDesc")
        root.append(filedesc_elem)

    # Find the <titleStmt> element inside <fileDesc> or create it if it doesn't exist
    titlestmt_elem = filedesc_elem.find(".//{http://www.tei-c.org/ns/1.0}titleStmt")
    if titlestmt_elem is None:
        titlestmt_elem = ET.Element("{http://www.tei-c.org/ns/1.0}titleStmt")
        filedesc_elem.append(titlestmt_elem)

    # Find the <title> element inside <titleStmt> or create it if it doesn't exist
    title_elem = titlestmt_elem.find("{http://www.tei-c.org/ns/1.0}title")
    if title_elem is None:
        title_elem = ET.Element("{http://www.tei-c.org/ns/1.0}title")
        titlestmt_elem.append(title_elem)

    # Set the text of the <title> element to the filename without the extension
    title_elem.text = os.path.splitext(os.path.basename(filename))[0]

    # Save the changes back to the XML file
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def main():
    directory_path = "C:\\Users\\Luca Giovannini\\Documents\\GitHub\\artificial-dramas\\ezdrama_format\\gpt\\xmls"
    for filename in os.listdir(directory_path):
        if filename.endswith(".xml"):
            file_path = os.path.join(directory_path, filename)
            print(f"Updating {filename}...")
            update_title_in_xml(file_path)
            print(f"{filename} updated.")

if __name__ == "__main__":
    main()
