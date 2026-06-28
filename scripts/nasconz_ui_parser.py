#!/usr/bin/env python3
"""NasConZ UI Dump Parser — parses Android UI hierarchy XML"""
import sys
import xml.etree.ElementTree as ET

def parse_ui(source):
    try:
        if source == '/dev/stdin':
            xml = sys.stdin.read()
            root = ET.fromstring(xml)
        else:
            tree = ET.parse(source)
            root = tree.getroot()
        results = []
        for node in root.iter('node'):
            text = node.get('text', '')
            desc = node.get('content-desc', '')
            bounds = node.get('bounds', '')
            label = text or desc
            if label.strip() and bounds:
                results.append(f"{bounds} {label}")
        return results
    except Exception as e:
        return [f"Parse error: {e}"]

if __name__ == '__main__':
    xml_file = sys.argv[1] if len(sys.argv) > 1 else '/sdcard/window_dump.xml'
    for line in parse_ui(xml_file):
        print(line)
