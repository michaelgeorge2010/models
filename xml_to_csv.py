import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        h = os.path.basename(xml_file)
        t = os.path.splitext(h)[0] 
        t = t + '.jpg'
        for member in root.findall('.//bndbox'):
            value = (t,
                     int(root.find('.//size/width').text),
                     int(root.find('.//size/height').text),
                     'pedestrian',
                     int(float(member.find('xmin').text)),
                     int(float(member.find('ymin').text)),
                     int(float(member.find('xmax').text)),
                     int(float(member.find('ymax').text))
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for directory in ['train','test']:
        image_path = os.path.join(os.getcwd(), 'images/{}'.format(directory))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv('dat/{}_labels.csv'.format(directory), index=None)
        print('Successfully converted xml to csv.')

main()
