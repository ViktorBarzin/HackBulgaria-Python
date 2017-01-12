import json
import xml.etree.ElementTree as ET


class Jsonable(object):
    serializable_types = (int, float, str, bool, None, list, tuple)

    def to_json(self, indent=4):
        data = self.__dict__
        result = {'classname': type(self).__name__,
                'data': {}}

        for k, v in data.items():
            if type(v) in self.serializable_types:
                result['data'][k] = v
            elif isinstance(v, Jsonable):
                # print(v, k)
                result['data'][k] = json.loads(v.to_json())
        return json.dumps(result, indent=4)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        classname = data['classname']

        if classname != cls.__name__:
            raise ValueError('{} != {}'.format(classname, cls))
        return cls(**data['data'])


class Xmlable():
    def to_xml(self):
        root = ET.Element(type(self).__name__)
        for k, v in self.__dict__.items():
            child = ET.SubElement(root, str(k), {'type': type(v).__name__})
            child.text = str(v)
        return ET.tostring(root).decode('utf8')

    @classmethod
    def from_xml(cls, xml_string):
        root = ET.fromstring(xml_string)

        if root.tag != cls.__name__:
            raise ValueError('{} != {}'.format(root.tag, cls))
        res = {}

        for child in root:
            res[child.tag] = child.text
        return cls(**res)

