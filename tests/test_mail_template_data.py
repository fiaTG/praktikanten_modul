from pathlib import Path
import xml.etree.ElementTree as ET


def test_intern_invitation_template_exists():
    template_path = Path(__file__).resolve().parents[1] / "data" / "mail_template_data.xml"
    tree = ET.parse(template_path)
    root = tree.getroot()

    records = [record for record in root.findall("record") if record.get("id") == "mail_template_intern_invitation"]

    assert records, "mail_template_intern_invitation template should exist"
    assert records[0].get("model") == "mail.template", "Template must target mail.template model"
