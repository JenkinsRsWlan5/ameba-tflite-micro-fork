import xml.etree.ElementTree as ET
import argparse

def insert_base_entries_to_xml(file_path, entries):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Iterate over the entries to add
    for entry in entries:
        path, key_name, list_entry_value = entry

        # Find the specified <key>
        target_entry = root.find(f".//{path}/[key='{key_name}']")
        if target_entry is None:
            print(f"Target <{path}> with <key>{key_name}</key> not found. Skipping...")
            continue
        else:
            value_element = target_entry.find("value")
            if value_element is None:
                print(f"<value> element not found inside for key '{key_name}'. Skipping...")
                continue

        # Add a new <ListEntry> element
        new_entry = ET.SubElement(value_element, "ListEntry")
        if isinstance(list_entry_value, dict):  # Handle key-value pairs for Defines
            for k, v in list_entry_value.items():
                new_entry.set(k, v)
        else:  # Handle plain text values for Includes, Libraries, etc.
            new_entry.text = list_entry_value

    # Write the updated XML back to the file
    tree.write(file_path, encoding="utf-8", xml_declaration=True)
    print("Insert Base Settings successfully.")

def add_overridden_settings_to_xml(file_path, overridden_xml_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    add_root = ET.parse(overridden_xml_path).getroot()
    
    build_settings_entry = root.find(".//BuildSettings")
    build_settings_entry.append(add_root)

    # Write the updated XML back to the file
    tree.write(file_path, encoding="utf-8", xml_declaration=True)
    print("Add Overridden Settings successfully.")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Insert dependencies into Release.bts files.")
    parser.add_argument("--project_dir", help="Path to the project_dir." ,required=True)
    parser.add_argument("--deps_xml", help="Path to the XML file containing example dependencies.", required=True)
    args = parser.parse_args()
    
    file_path = str(args.project_dir) + '.settings/targets/xtensa/Release.bts'

    # all tflm examples' common dependencies
    base_entries_to_insert = [
        ["BuildSettings/BaseSettings/PreprocessorOptions/StringListMapOptions/StringListMapEntry", "Includes", "${workspace_loc}/../lib/tflite_micro"],
        ["BuildSettings/BaseSettings/PreprocessorOptions/StringListMapOptions/StringListMapEntry", "Includes", "${workspace_loc}/../lib/tflite_micro/third_party/flatbuffers/include"],
        ["BuildSettings/BaseSettings/PreprocessorOptions/StringListMapOptions/StringListMapEntry", "Includes", "${workspace_loc}/../lib/tflite_micro/third_party/gemmlowp"],

        ["BuildSettings/BaseSettings/PreprocessorOptions/KeyValueListMapOptions/KeyValueListMapEntry", "Defines", {"key": "TF_LITE_STATIC_MEMORY", "value": ""}],

        ["BuildSettings/BaseSettings/LinkerOptions/StringListMapOptions/StringListMapEntry", "Libraries", "tensorflow-microlite"],
        ["BuildSettings/BaseSettings/LinkerOptions/StringListMapOptions/StringListMapEntry", "Libraries", "xa_nnlib"],

        ["BuildSettings/BaseSettings/LinkerOptions/StringListMapOptions/StringListMapEntry", "LibrarySearchPath", "${workspace_loc}/../lib/tflite_micro/amebalite_dsp-out/$(TARGET_CONFIG)"],
        ["BuildSettings/BaseSettings/LinkerOptions/StringListMapOptions/StringListMapEntry", "LibrarySearchPath", "${workspace_loc}/../lib/xa_nnlib/v2.3.0/bin/$(TARGET_CONFIG)/Release"],
    ]
    insert_base_entries_to_xml(file_path, base_entries_to_insert)
    
    # add example-specific overridden settings
    add_overridden_settings_to_xml(file_path, args.deps_xml)

