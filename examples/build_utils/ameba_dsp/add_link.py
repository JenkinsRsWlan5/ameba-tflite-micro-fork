import xml.etree.ElementTree as ET
import argparse

def add_linked_resources(original_file_path, add_file_path):
    # Parse the XML file
    origin_tree = ET.parse(original_file_path)
    origin_root = origin_tree.getroot()
    add_root = ET.parse(add_file_path).getroot()
    
    origin_lr_entry = origin_root.find(".//linkedResources/")
    for lr in list(add_root):
        origin_lr_entry.append(lr)
    
    origin_tree.write(original_file_path, encoding="utf-8", xml_declaration=True)
    print("Insert linkedResources successfully.")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Insert linkedResources into .project files.")
    parser.add_argument("--project_dir", help="Path to the project_dir.", required=True)
    parser.add_argument("--lr_xml", help="Path to the XML file containing example linked resources.", required=True)
    args = parser.parse_args()
    
    file_path = str(args.project_dir) + '.project'
    add_linked_resources(file_path, args.lr_xml)